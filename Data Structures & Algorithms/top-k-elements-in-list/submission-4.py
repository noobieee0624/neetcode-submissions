class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of frequencies for all elements
        frequencies = {}
        # maps a frequency to its element
        buckets = [[] for _ in range(len(nums) + 1)]
        output = []

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        for num, freq in frequencies.items():
            buckets[freq].append(num)

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                if k == 0:
                    return output
                output.append(num)
                k -= 1
        return output





                
