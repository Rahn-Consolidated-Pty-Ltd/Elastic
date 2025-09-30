from elasticsearch import Elasticsearch
import os
import datetime

# Connect to Elasticsearch
ES_HOST = os.environ.get("ES_HOST", "http://localhost:9200")
es = Elasticsearch(ES_HOST)

def send_ci_result(job_name, status, duration_seconds):
    doc = {
        "job_name": job_name,
        "status": status,
        "duration_seconds": duration_seconds,
        "timestamp": datetime.datetime.utcnow()
    }
    es.index(index="ci_results", document=doc)
