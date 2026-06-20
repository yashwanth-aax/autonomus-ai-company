# forge/memory/memory_store.py

class MemoryStore:

    def __init__(self):

        self.store = {}

    def write(self, key, value):

        self.store[key] = value

    def read(self, key):

        return self.store.get(key)

    def delete(self, key):

        if key in self.store:

            del self.store[key]

    def exists(self, key):

        return key in self.store

    def clear(self):

        self.store.clear()

    def get_all(self):

        return dict(self.store)