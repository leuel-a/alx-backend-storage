#!/usr/bin/env python3
"""Defines the update_topics function"""
from typing import List
from pymongo.collection import Collection


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
