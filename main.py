import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from opensearchpy import OpenSearch


load_dotenv()
username = os.environ.get('OPENSEARCH_USERNAME')
password = os.environ.get('OPENSEARCH_PASSWORD')
OPENSEARCH_CLIENT = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=(username, password),
    use_ssl=True,
    verify_certs=False
)


def get_indices():
    return OPENSEARCH_CLIENT.cat.indices(format="json")


def search_opensearch(index_name, query):
    response = OPENSEARCH_CLIENT.search(index=index_name, body={"query": {"match": {"content": query}}})
    return response['hits']['hits']


st.title("RAG Chat Application")
rag_option = st.radio("Choose RAG Method:", ("Use RAG", "No RAG"))

index_names = [index['index'] for index in get_indices()]
selected_index = st.selectbox(
        "Choose an index:",
        index_names,
        placeholder="Choose frappe_framework_v1"
    )

model_name = st.selectbox(
    "Choose a model:",
    [
        "llama-3.2-1b-preview",
        "llama-3.2-3b-preview",
        "llama-3.1-8b-instant",
        "gemma-7b-it",
    ]
)

user_query = st.text_input("Enter your Query:", "what is python?")

submit_button = st.button("Submit")

messages = [
    (
        "system",
        "You are a helpful assistant.",
    ),
    ("human", user_query),
]

if submit_button:
    if user_query:

        llm = ChatGroq(
            model=model_name,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        if rag_option == "Use RAG":
            results = search_opensearch(selected_index, user_query)
            retrieved_docs = [result["_source"]["content"] for result in results]
            
            # Combine retrieved documents with query
            prompt = f"Context: {retrieved_docs}\nUser Query: {user_query}"
            answer = llm(prompt)
            
            # Display the answer
            st.write("RAG Response:", answer)
        else:
            # Handle non-RAG query
            ai_msg = llm.invoke(messages)
            st.write("LLM Response:", ai_msg.content)