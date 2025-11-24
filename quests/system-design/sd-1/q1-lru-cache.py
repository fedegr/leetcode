from dataclasses import dataclass

@dataclass
class Node:
    key: int
    value: int
    older: "Node" = None
    newer: "Node" = None

class LRUCache:

    def __init__(self, capacity: int):
        self.__cache = {}
        # Trick to avoid handling None cases on every insert and remove
        self.__oldest = Node(None, None) 
        self.__newest = Node(None, None)
        self.__oldest.newer = self.__newest
        self.__newest.older = self.__oldest
        self.__capacity = capacity
        
    def get(self, key: int) -> int:
        elem = self.__cache.get(key, None)
        if elem is None:
            return -1
        
        self.__remove(elem)
        self.__insert(elem)
        
        return elem.value

    def put(self, key: int, value: int) -> None:
        node = self.__cache.get(key, None)
        if node is not None:
            self.__remove(node)
        node = Node(key=key, value=value)
        self.__cache[key] = node
        self.__insert(node)
        if len(self.__cache) > self.__capacity:
            node_to_remove = self.__oldest.newer
            self.__remove(node_to_remove)
            del self.__cache[node_to_remove.key]

    def __insert(self, node: Node):
        self.__newest.older.newer = node
        node.older = self.__newest.older
        node.newer = self.__newest
        self.__newest.older = node


    def __remove(self, node: Node):
        nn, no = node.newer, node.older
        nn.older, no.newer = no, nn
        
    def print_nodes(self, prefix = ""):
        if len(prefix) > 0:
            prefix += " "
        i = 0
        n = self.__newest
        values = []
        while n is not None and i < 10:
            values.append(n.key)
            n = n.older
            i+=1
        print(prefix + "new > old", values)

        i = 0
        n = self.__oldest
        values = []
        while n is not None and i < 10:
            values.append(n.key)
            n = n.newer
            i+=1
        print(prefix + "old > new", values)