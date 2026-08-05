class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        counter = 0
        product = 1
        for i, num in enumerate(nums):
            if num == 0:
                counter += 1
                if counter >= 2:
                    return [0] * len(nums)
            else:
                product = product * num

                
        for i in range(0, len(nums), +1):
            if nums[i] != 0:
                if counter == 1:
                    output[i] = 0
                else: 
                    output[i] = int(product/nums[i])
            else:
                output[i] = product
        return output
            
            