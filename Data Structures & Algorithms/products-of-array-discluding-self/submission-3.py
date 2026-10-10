class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        output = []
        num_of_zeros = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                num_of_zeros += 1
                if num_of_zeros >= 2:
                    return [0] * len(nums)

        for num in nums:
            if num == 0:
                output.append(total_product)
            elif num_of_zeros > 0:
                output.append(0)
            else:
                output.append(total_product // num)
        
        return output