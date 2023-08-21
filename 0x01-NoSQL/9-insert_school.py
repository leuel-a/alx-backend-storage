#!/usr/bin/env python3
"""Defines the insert_school function"""
from typing import List


def insert_school(mongo_collection, **kwargs):
    """Inserts the new document to the collection that is
    passed as an argument"""
    _id = mongo_collection.insert_one(kwargs)
    return _id.inserted_id
