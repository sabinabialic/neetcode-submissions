class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Min heaps keep the smallest element at the top
        # By pushing (frequecy, value) pairs into the heap and removing the smallest element whenevr the heap grows beyond size k, we can make sure the heap always contains only the top k most frequent elements
        # At the end, the heap holds exactly k values along with their frequencies

        # Build a frequency map that counts how many times each number appears
        # Create an empty min heap
        # For each number in the frequency map
            # Push (frequency, number) into the heap
            # If the heap size > k, pop once to remove the smallest frequency
        # After processing all numbers the heap contains the k most frequent elements
        # Pop all elements from the heap and collect their numbers into the result list
        # Return result

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res