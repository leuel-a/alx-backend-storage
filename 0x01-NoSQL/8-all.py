#!/usr/bin/env python3
"""Defines the list_all function"""
from typing import List


def list_all(mongo_collection) -> List:
    """Lists all documents in a collection"""
    return list(mongo_collection.find())
