from heapq import *


class Solution:
    def sortCharacterByFrequency(self, str):
        char_freq_map = {}
        max_heap = []
        for char in str:
            char_freq_map[char] = char_freq_map.get(char, 0) + 1

        for character, frequency in char_freq_map.items():
            heappush(max_heap, (-frequency, character))

        result = []
        while max_heap:
            pair = heappop(max_heap)
            result.append(pair[1] * -pair[0])

        return ''.join(result)
