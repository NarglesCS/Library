class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zedStack = []
        numStack = []
        #not sure if recalculated with changes.
        for i in range(len(nums)):
            if nums[i] == 0:
                zedStack.append(nums[i])
            elif nums[i] != 0:
                numStack.append(nums[i])


        nums.clear()
        nums.extend(numStack)
        nums.extend(zedStack)
