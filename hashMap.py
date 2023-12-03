# import networkx as nx

class HashMap:

    # adding class to the map:
    # map.insert("ABC1234", ["prereq1", "prereq2", ...] )
    # 
    # extracting vector of prereqs:
    # map.get_prereqs("ABC1234")

    def __init__(self, capacity=10, max_load_factor=0.8):
        self.capacity = capacity
        self.max_load_factor = max_load_factor
        self.count = 0
        self.buckets = [[] for i in range(capacity)]
        
    def hash_function(self, courseCode):
        return hash(courseCode) % self.capacity

    def rehash(self):
        new_cap = self.capacity * 2
        new_buckets = [[] for i in range(new_cap)]

        # Rehash all pairs in the map 
        for bucket in self.buckets:
            for old_courseCode, old_value in bucket:
                new_index = hash(old_courseCode) % new_cap
                new_buckets[new_index].append((old_courseCode, old_value))
        self.capacity = new_cap
        self.buckets = new_buckets

    def insert(self, courseCode, vector):
        index = self.hash_function(courseCode)
        bucket = self.buckets[index]

        # check for duplicate
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == courseCode:
                return
            
        # append new courseCode-value pair
        bucket.append((courseCode, vector))
        self.count += 1

        # Check load factor and rehash if necessary
        load_factor = self.count / self.capacity
        if load_factor >= self.max_load_factor:
            self.rehash()

    def get_prereqs(self, courseCode):
        index = self.hash_function(courseCode)
        bucket = self.buckets[index]

        # Search for the courseCode in the bucket
        for old_courseCode, vector in bucket:
            if old_courseCode == courseCode:
                return vector

        # courseCode not found
        return None

    def remove(self, courseCode):
        index = self.hash_function(courseCode)
        bucket = self.buckets[index]

        # search the bucket and remove item
        for i in range(len(bucket)):
            if bucket[i][0] == courseCode:
                del bucket[i]
                self.count -= 1
                return


custom_map = HashMap()
custom_map.insert("key1", ["value1", "value2", "value3"])
custom_map.insert("key2", ["value4", "value5"])
custom_map.insert("key2", ["value9", "value9"])

custom_map.insert("key3", ["value6"])

print(custom_map.get_prereqs("key2"))  

