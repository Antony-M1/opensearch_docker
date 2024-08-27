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