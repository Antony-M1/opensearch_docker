![image](https://github.com/user-attachments/assets/4180c52b-cee8-4f4a-a671-a93d50a0b8b8)

# OpenSearch
OpenSearch is a family of software consisting of a `search engine`, and `OpenSearch Dashboards`, a data `visualization dashboard` for that search engine. The software started in 2021 as a fork of `Elasticsearch` and `Kibana`, with development led by `Amazon Web Services`.

**Reference Links**
* [Opensearch - Dockerhub](https://hub.docker.com/r/opensearchproject/opensearch)
* [Sample docker-compose.yml](https://opensearch.org/samples/docker-compose.yml)
* [Password Test](https://lowe.github.io/tryzxcvbn/)
* [Dashboards Query Language (DQL)](https://opensearch.org/docs/2.16/dashboards/dql)
* [Managing ML models in OpenSearch Dashboards](https://opensearch.org/docs/latest/ml-commons-plugin/ml-dashboard/)
* [Opensearch - Langchain](https://python.langchain.com/v0.2/docs/integrations/vectorstores/opensearch/)

**Python Packages**
* [opensearch-py](https://pypi.org/project/opensearch-py/)
* [langchain](https://pypi.org/project/langchain/)

# How to use this image?
**Run a single node for local development.**
```cmd
docker run -it -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" \
--name opensearch-node -d opensearchproject/opensearch:latest
```
*Note: For OpenSearch 2.12 and later, a custom password for the admin user is required to be passed to set-up and utilize demo configuration.*
```cmd
docker run -it -p 9200:9200 -p 9600:9600 -e OPENSEARCH_INITIAL_ADMIN_PASSWORD=<strong-password> \
-e "discovery.type=single-node"  --name opensearch-node opensearchproject/opensearch:latest
```
**Send requests to the OpenSearch REST API to verify that OpenSearch is working.** By default, OpenSearch uses `self-signed TLS certificates`. The `-k` short option skips the certificate verification step so requests don't fail. The default username is `admin` and the password will be `admin` for OpenSearch 2.12 and earlier. For `OpenSearch 2.12` and `later`, the password will be the `custom value`, which is required to be provided during the demo configuration setup for security plugin.
```
curl -X GET "https://localhost:9200" -ku admin:<password>
curl -X GET "https://localhost:9200/_cat/nodes?v" -ku admin:<password>
curl -X GET "https://localhost:9200/_cat/plugins?v" -ku admin:<password>
```
You can stop, start, and restart your container by passing either the container ID or the container name as an argument. For example, to stop the container use the following command.
```
docker stop opensearch-node
```
# .env
this file is used to store the credentials, create a `.env` file and add the below options
```env
OPENSEARCH_INITIAL_ADMIN_PASSWORD=<YOUR_PASSWORD>
```

# Quick Start

### Step 1 : Clone the repository
```cmd
git clone https://github.com/Antony-M1/opensearch_docker.git
```

### Step 2 : Up the container
```cmd
export OPENSEARCH_INITIAL_ADMIN_PASSWORD=Dragon@75845567
```
Username : `admin`

Password : `Dragon@75845567`

```
docker compose up -d
```

### Step 3 : Login Page

Go to this url [0.0.0.0:5601](http://0.0.0.0:5601/) and login with username and password.

# Response Explanation

Below explanations are used to understand Response values json keys.

<details>
  <summary><b>took</b></summary>

  The `took` field in the OpenSearch response indicates the amount of time (in milliseconds) that the server took to process the query. In your example, `"took": 2` means that the search query took 2 milliseconds to complete. This value helps gauge the performance of your search query execution.
</details>

<details>
  <summary><b>timed_out</b></summary>


  The `timed_out` field in the OpenSearch response indicates whether the search query timed out. 

- If `"timed_out": false`, it means the query completed within the allowed time.
- If `"timed_out": true`, it means the query took longer than the specified timeout duration and did not complete within that time frame.

A timeout could occur if the query is too complex, the dataset is large, or the server is under heavy load.
</details>


<details>
  <summary><b>_shards</b></summary>
  
  The `_shards` field in the OpenSearch response provides information about the status of the shards that were queried during the search. Shards are smaller portions of the entire index, which allow the system to parallelize the search.

Here are the details:

- **total**: The total number of shards that were involved in the search.
- **successful**: The number of shards that successfully completed the search.
- **skipped**: The number of shards that were skipped during the search (typically due to optimizations).
- **failed**: The number of shards that encountered errors or failed during the search.

In a typical response, all shards should be successful, meaning they returned data without issues. If there are failed shards, it might indicate issues like network failures, corrupted data, or heavy loads on specific nodes.
</details>


<details>
  <summary><b>hits</b></summary>
  
  The `hits` field in the OpenSearch response contains the search results and associated metadata. Here's a breakdown of its components:

- **total**: Contains the total number of documents that match the search query.
  - **value**: The number of documents matching the query.
  - **relation**: Indicates how the `value` should be interpreted (usually "eq" for an exact count).

- **max_score**: The highest score among the search results. This score reflects the relevance of the documents to the search query, with higher scores indicating higher relevance.

- **hits**: An array of documents that match the query. Each item in this array includes:
  - **_index**: The name of the index where the document is stored.
  - **_id**: The unique identifier of the document.
  - **_score**: The relevance score of the document based on the query.
  - **_source**: The actual content of the document. This is the data you indexed and queried against.

This field provides the detailed results of your search query, including the documents that matched, their relevance scores, and their metadata.
</details>

### Example Response

Please fine the below example for the Response

<details>
  <summary><b>Example</b></summary>

```json
    {
    "took": 1,
    "timed_out": false,
    "_shards": {
        "total": 46,
        "successful": 46,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
        "value": 9,
        "relation": "eq"
        },
        "max_score": 7.341767,
        "hits": [
        {
            "_index": "frappe_framework_v1",
            "_id": "479",
            "_score": 7.341767,
            "_source": {
            "system": "You are a Frappe Framework expert.",
            "user": "How do I make an AJAX request to the server using Frappe?",
            "assistant": "You can use the `frappe.call` method to make an AJAX request to the server. This method allows you to execute a whitelisted Python method and receive its return value as a response. For example, you can call the `ping` method with `frappe.call('ping')` which will return a response with `message: 'pong'`. You can also pass arguments to the method. For example, to call the `frappe.core.doctype.user.user.get_role_profile` method with the `role_profile` argument set to 'Test', you would use `frappe.call('frappe.core.doctype.user.user.get_role_profile', { role_profile: 'Test' })`."
            }
        },
        {
            "_index": "frappe_framework_v1",
            "_id": "555",
            "_score": 7.301902,
            "_source": {
            "system": "You are a Frappe framework expert.",
            "user": "How do I call whitelisted functions in Frappe using frappe.call?",
            "assistant": """To call custom server-side functions using frappe.call, you need to make sure those functions are whitelisted. This is essential for security. Here's how it works:

    1. **Whitelist the Server-Side Function:**
    * In your server-side Python code (usually a file within your custom app), use the `@frappe.whitelist()` decorator above the function you want to make accessible through frappe.call.

    ```python
    @frappe.whitelist()
    def get_all_roles():
        # Business logic to fetch all roles
        # ...
        return value  # Return the data you want to send back to the client
    ```

    2. **Call the Function from the Client (JavaScript):**
    * In your client-side JavaScript, use frappe.call to call the whitelisted function. The `method` parameter should be the dotted path to the server-side function. For example:

    ```javascript
    frappe.call({
        method: "frappe.core.doctype.user.user.get_all_roles",  // Dotted path to the server-side function
        callback: function(r) {
        if (!r.exc) {
            // Process the returned data (r.message) if the request was successful
        }
        }
    });
    ```

    **Key Points:**
    * Whitelisting ensures that only authorized functions are accessible via frappe.call.
    * The `method` parameter in frappe.call should match the dotted path of the whitelisted function.
    * The whitelisted function on the server-side should return the data you want to send back to the client."""
            }
        },
        {
            "_index": "frappe_framework_v1",
            "_id": "552",
            "_score": 5.1666327,
            "_source": {
            "system": "You are a Frappe framework expert.",
            "user": "What is Frappe.call?",
            "assistant": "Frappe.call is a method in the Frappe framework used to manage AJAX calls, allowing asynchronous communication between the client (browser) and the server. It enables you to send requests to the server and handle responses via a callback mechanism. This makes it easier to update parts of a web page without needing to reload the entire page."
            }
        }
        ]
    }
    }
```
</details>

# Interview Questions

<details>
  <summary><b>How a vectore database can sync each other with mongo DB</b></summary>

Synchronizing a vector database with MongoDB can be accomplished by regularly updating both databases to keep the data consistent across them. Here's a typical approach for syncing:

### 1. **Schema Mapping and Transformation:**
   - **Vector Database**: These databases store embeddings or feature vectors, typically using data structures that allow efficient similarity searches (e.g., FAISS, Milvus, Pinecone).
   - **MongoDB**: A document-based NoSQL database, which stores data in JSON-like BSON format.

   To sync, the schema from MongoDB (usually documents) must be transformed into vectors to be inserted into the vector database. Similarly, the vector database data might need to be transformed into document-like structures to be pushed to MongoDB.

### 2. **Data Transformation Logic:**
   - Ingest MongoDB documents and convert certain fields into vector representations using an embedding model (e.g., Sentence Transformers, OpenAI, Hugging Face models).
   - Insert these vectors into the vector database.
   - Store a reference in MongoDB to the corresponding vector stored in the vector database (e.g., an ID).

### 3. **Sync Strategies:**
   There are different ways to keep MongoDB and the vector database in sync:
   
   - **Real-time Sync**:
     - Use a change stream in MongoDB (available for replica sets or sharded clusters) to listen to real-time changes (insert, update, delete). Whenever a new document is inserted or updated, you can:
       1. Extract the relevant fields.
       2. Compute the embeddings (vectors) using a pre-trained model.
       3. Insert/update the vector in the vector database and update the document in MongoDB with a reference to the vector.

     MongoDB's [Change Streams](https://www.mongodb.com/docs/manual/changeStreams/) allow you to react to changes without polling.

   - **Batch Sync**:
     - Periodically batch sync documents from MongoDB to the vector database by:
       1. Querying the documents added or modified since the last sync.
       2. Computing vectors for new or updated documents.
       3. Pushing the vectors to the vector database.
     - You can schedule this using a cron job or other scheduling mechanisms.

### 4. **Conflict Resolution:**
   - Ensure that each system has a version control mechanism or timestamp field to resolve conflicts, ensuring that only the most up-to-date version of a document is kept.

### 5. **APIs for Sync:**
   - **MongoDB**: Use MongoDB drivers in Python, Node.js, or your preferred language to query data, retrieve change streams, and push updates.
   - **Vector Database**: Depending on your choice (e.g., FAISS, Milvus, Pinecone), you can use the respective API to insert and update vectors.

### Example: Real-Time Sync (with Change Streams)
Here's a simplified Python example using MongoDB and a vector database (like Milvus or FAISS):

```python
from pymongo import MongoClient
from transformers import AutoModel, AutoTokenizer
import numpy as np
from vector_db import VectorDB  # Placeholder for your vector database API

# Initialize MongoDB and vector database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

vector_db = VectorDB()

# Load embedding model
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-mpnet-base-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-mpnet-base-v2')

# Helper function to compute embeddings
def compute_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings.detach().numpy()

# Real-time sync with MongoDB change stream
with collection.watch() as stream:
    for change in stream:
        if change['operationType'] == 'insert':
            doc = change['fullDocument']
            text = doc['text']  # Assuming you want to embed the 'text' field
            embedding = compute_embedding(text)
            
            # Insert vector into vector database
            vector_id = vector_db.insert(embedding)
            
            # Update MongoDB document with vector ID reference
            collection.update_one({'_id': doc['_id']}, {'$set': {'vector_id': vector_id}})
```

### 6. **Two-Way Sync (Vector DB to MongoDB):**
   - You can also reverse the sync, where changes in the vector database are pushed back to MongoDB. For example, if you're updating vector metadata in the vector database, you can propagate that to MongoDB.

### 7. **Error Handling and Logging:**
   - Ensure error handling is in place to manage any failures in syncing, and log all sync actions for debugging and monitoring.

This approach can help you maintain consistency between MongoDB and a vector database for hybrid applications involving both document and vector-based retrieval.
</details>

<details>
  <summary><b>Example for real time sync</b></summary>

In this file uploading system, once a file is successfully uploaded, it is read and divided into smaller chunks. These chunks are then processed and uploaded to a vector database for storage. The entire operation occurs asynchronously after the file upload, ensuring smooth user experience and efficient real-time processing of the file into a vectorized format. This approach helps in managing large files and enables efficient similarity search or retrieval in the vector database.
</details>
