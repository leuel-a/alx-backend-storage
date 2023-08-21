#!/usr/bin/env python3
"""Defines the update_topics function"""
from typing import List
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection, name: str, topics: List[str]) \
                                                                    -> None:
    """Changes all topics of a school document based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
