import networkx as nx
import matplotlib.pyplot as plt
import time
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
    
    def displayPreReqGraph(self, course, G=None, parent=None, draw=False, visited=None):
        if G is None:
            G = nx.DiGraph()
            visited = set()

        # Avoid circular dependencies
        if course in visited:
            return G
        visited.add(course)

        prereqs = self.get_prereqs(course)

        # Add the course as a node to the graph. If it has a parent, add an edge.
        if course not in G:
            G.add_node(course)
        if parent is not None:
            G.add_edge(parent, course)

        if not prereqs or prereqs == [None]:
            return G

        for prereq in prereqs:
            if prereq is not None:
                self.displayPreReqGraph(prereq, G, course, draw=False, visited=visited)

        if draw:
            # Add drawing logic here if needed
            pass

        return G
        
    def draw_graph(self, G):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G)  # or any other layout you prefer
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', node_size=2000, font_size=10)
        plt.title("Map Prerequisite Graph")
        plt.show()

    def getTimeAndGraph(self, course):
        start_time = time.perf_counter()
        graph = self.displayPreReqGraph(course, None, draw=True)
        end_time = time.perf_counter()
        totalTime = end_time - start_time
        self.draw_graph(graph)
        print(f"The map took {totalTime / 10:.3e} decaseconds to get all prerequisites.")
