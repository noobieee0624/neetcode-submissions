class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add one to the number of buckets, since list 
        # starts at 0, so we store the maximum freq of a number in a list
        # as the len+1 value's index, otherwise out of bounds
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}
        ans = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                if k == 0:
                    return ans
                ans.append(n)
                k -= 1
        
        return ans