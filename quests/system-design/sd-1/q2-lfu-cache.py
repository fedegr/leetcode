from dataclasses import dataclass
from collections import deque


@dataclass
class LFUCacheItem:
    key: int
    value: int
    frequency_item: "LFUFreqItem"
    next_item: "LFUCacheItem" = None
    prev_item: "LFUCacheItem" = None

    def print_node(self, is_current=False, frequency_item = None):
        return f'<{"*" if is_current else ""}k={self.key} v={self.value}' + (f' f={self.frequency_item.freq}' if frequency_item is not None and self.frequency_item != frequency_item else '') + '>'

    def __repr__(self):
        data = deque()

        data.append(self.print_node(True))

        node = self

        while node.prev_item is not None:
            connection = ''
            if node.prev_item.next_item == node:
                connection = f' <-> '
            else:
                connection = f' <- '
            node = node.prev_item
            data.append(f'{connection}{node.print_node(frequency_item = self.frequency_item)}')
        
        node = self
        while node.next_item is not None:
            connection = ''
            if node.next_item.prev_item == node:
                connection = f' <-> '
            else:
                connection = f' -> '
            node = node.next_item
            data.append(f'{connection}{node.print_node(frequency_item = self.frequency_item)}')
            

        return "".join(data)


@dataclass
class LFUFreqItem:
    freq: int
    first_cache_item: "LFUCacheItem" = None
    last_cache_item: "LFUCacheItem" = None
    next_item: "LFUFreqItem" = None
    prev_item: "LFUFreqItem" = None

    def __repr__(self):
        data = deque()
        node = self
        connection = ''
        while node is not None:
            data.append(f'{connection}<f={node.freq} items={node.first_cache_item}>')
            if node.next_item is not None:
                if node.next_item.prev_item == node:
                    connection = f' <==> '
                else:
                    connection = f' ==> '
            node = node.next_item

        return "".join(data)


class LFUCache:
    def __init__(self, capacity: int):
        self.frequency = None
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        cache_item = self.cache.get(key, None)
        if cache_item is None:
            return -1
        
        self.__update_cache_item(cache_item)
        return cache_item.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node is None:
            self.__add_cache_item(key, value)
        else:
            node.value = value
            self.__update_cache_item(node)

    def __add_cache_item(self, key, value):
        if len(self.cache) >= self.capacity:
            self.__evict()

        if self.frequency is None or self.frequency.freq > 1:
            self.frequency = self.__insert_frequency_item(1, None, self.frequency)
        
        cache_item = LFUCacheItem(key=key, value=value, frequency_item=self.frequency)
        
        cache_item.prev_item = self.frequency.last_cache_item

        if self.frequency.last_cache_item is not None:
            self.frequency.last_cache_item.next_item = cache_item
        else:
            self.frequency.first_cache_item = cache_item
        self.frequency.last_cache_item = cache_item
        
        self.cache[key] = cache_item


    def __evict(self):
        cache_item = self.frequency.first_cache_item
        self.cache.pop(cache_item.key)
        self.__remove_cache_item_from_frequency_list(cache_item)

    def __insert_frequency_item(self, frequency, prev_frequency_item, next_frequency_item):
        f =  LFUFreqItem(
            freq=frequency,
            next_item=next_frequency_item,
            prev_item=prev_frequency_item,
        )
        if next_frequency_item is not None:
            next_frequency_item.prev_item=f
        if prev_frequency_item is not None:
            prev_frequency_item.next_item=f
        return f

    def __update_cache_item(self, cache_item):
        old_frequency_item = cache_item.frequency_item
        new_frequency_item = old_frequency_item.next_item

        if new_frequency_item is None or new_frequency_item.freq > old_frequency_item.freq + 1:
            new_frequency_item = self.__insert_frequency_item(old_frequency_item.freq + 1, old_frequency_item, new_frequency_item)
        
        self.__remove_cache_item_from_frequency_list(cache_item, new_frequency_item)
        cache_item.frequency_item = new_frequency_item
        cache_item.prev_item = new_frequency_item.last_cache_item
        if cache_item.prev_item is not None:
            cache_item.prev_item.next_item = cache_item
        cache_item.next_item = None
        new_frequency_item.last_cache_item = cache_item
        new_frequency_item.first_cache_item = new_frequency_item.first_cache_item or cache_item
        

    def __remove_cache_item_from_frequency_list(self, cache_item, new_frequency_item=None):
        frequency_item = cache_item.frequency_item

        cache_item.print_node()

        if cache_item.prev_item is None:
            frequency_item.first_cache_item = cache_item.next_item
        else:
            cache_item.prev_item.next_item = cache_item.next_item

        if cache_item.next_item is None:
            frequency_item.last_cache_item = cache_item.prev_item
        else:
            cache_item.next_item.prev_item = cache_item.prev_item

        if frequency_item.first_cache_item is None:
            if frequency_item.prev_item is not None:
                frequency_item.prev_item.next_item = frequency_item.next_item
            else:
                self.frequency = new_frequency_item or frequency_item.next_item

            if frequency_item.next_item is not None:
                frequency_item.next_item.prev_item = frequency_item.prev_item 


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)