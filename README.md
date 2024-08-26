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