#!/usr/bin/env python3
"""Defines the schools_by_topic function"""
from pymongo.collection import Collection
from typing import List


def schools_by_topic(mongo_collection: Collection, topic: str):
    """Searchs for schools if they have paritcular topic in their
    topics list"""
    return mongo_collection.find({"topics": topic})
