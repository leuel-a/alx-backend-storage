#!/usr/bin/env python3
"""Defines the update topics function"""


def update_topics(mongo_collection, name, topics):
    """update a collection based on the name specified"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
