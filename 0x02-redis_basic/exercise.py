#!/usr/bin/env python3
"""Defines the Cache class"""
from uuid import uuid4
from redis import Redis


class Cache:
    """Simple cache using redis-server"""
    def __init__(self):
        """Instantiates a new cache object"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Stores the data with a uniquely generated id using
        an id generator and returns the key where the data is
        stored at"""
        key = str(uuid4())  # The key where the data will be stored at
        self._redis.set(key, data)
        return key
