class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use an array of arrays to store the frequencies
        # since elements can have the same freq
        # use a dictionary to store each number's frequency, then we
        # can loop through dictionary and store the element into
        # its array by indexing the freq as the index to the array

        res = []
        freq = {}
        # this bucket gives us a range of freq from 0 to len + 1
        bucket = [[] for _ in range(0, len(nums)+1)] 

        # increment frequencies for each unique element
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # adds elements to the array of their respective frequencies
        for num, freq in freq.items():
            bucket[freq].append(num)
        
        # loop through the buckets k times until k is 0
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                if k == 0:
                    return res
                res.append(num)
                k -= 1
        
        return res