![image](https://github.com/user-attachments/assets/4180c52b-cee8-4f4a-a671-a93d50a0b8b8)

# OpenSearch
OpenSearch is a family of software consisting of a `search engine`, and `OpenSearch Dashboards`, a data `visualization dashboard` for that search engine. The software started in 2021 as a fork of `Elasticsearch` and `Kibana`, with development led by `Amazon Web Services`.

**Reference Links**
* [Opensearch - Dockerhub](https://hub.docker.com/r/opensearchproject/opensearch)

# How to use this image?
**Run a single node for local development.**
```cmd
docker run -it -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" --name opensearch-node -d opensearchproject/opensearch:latest
```
*Note: For OpenSearch 2.12 and later, a custom password for the admin user is required to be passed to set-up and utilize demo configuration.*
```cmd
docker run -it -p 9200:9200 -p 9600:9600 -e OPENSEARCH_INITIAL_ADMIN_PASSWORD=<strong-password>\
-e "discovery.type=single-node"  --name opensearch-node opensearchproject/opensearch:latest
```
