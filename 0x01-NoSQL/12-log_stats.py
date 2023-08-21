#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
nginx_collection = client.logs.nginx

if __name__ == "__main__":
    total = nginx_collection.count_documents({})

    print(f"{total} logs")
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check = nginx_collection.count_documents({
            "method": "GET",
            "path": "/status"
        })
    print(f"{status_check} status check")
