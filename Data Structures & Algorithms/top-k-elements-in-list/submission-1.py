class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        output = []

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        for num, frequency in frequencies.items():
            bucket[frequency].append(num)
        
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output
        
        return output
                



