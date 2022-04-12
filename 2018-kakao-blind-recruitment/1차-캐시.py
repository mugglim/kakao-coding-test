class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.burst_time = 0
        self.maxSize = maxSize

    def is_empty(self):
        return len(self.cache) == 0

    def pop_left(self):
        if self.is_empty():
            return

        deleted_page = next(iter(self.cache))
        del self.cache[deleted_page]
        return deleted_page

    def is_hit(self, page):
        return page in self.cache

    def is_full(self):
        return len(self.cache) == self.maxSize

    def add(self, page):
        # 캐시 크기가 0인 경우
        if self.maxSize == 0:
            self.burst_time += 5
            return

        # when cache hit
        if self.is_hit(page):
            del self.cache[page]
            self.burst_time += 1
        else:
            # when cache miss
            if self.is_full():
                # when cache full
                self.pop_left()
            self.burst_time += 5

        self.cache[page] = True


def solution(cacheSize, cities):
    lru_cache = LRUCache(cacheSize)

    for city in cities:
        lru_cache.add(city.lower())

    return lru_cache.burst_time
