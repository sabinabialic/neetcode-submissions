class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Wnat the k most frequent elements in the array

        # Iterate through the array and create a map with key=the number and value how many occurances
        # Return the keys associated with the top k values

        my_dict = {}

        for i in nums:
            # If the key already exists, increment the value
            if my_dict.get(i):
                my_dict[i] += 1

            # Otherwise, add as new entry
            else:
                my_dict[i] = 1

        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[:k]



