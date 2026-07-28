class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        output = []
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for num, freq in frequency.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                if k == 0:
                    return output
                output.append(num)
                k-=1
        return output

        
        
        
