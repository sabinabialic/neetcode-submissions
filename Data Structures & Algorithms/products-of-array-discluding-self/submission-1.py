class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Left array is built from front to back and contains the product of everything before the current index
        left = [0] * len(nums)

        # Right array is built from back to front and contains the product of everything after the current index
        right = [0] * len(nums)

        # Results array
        res = [0] * len(nums)

        # Since we will build the right array from back to front, we need a var to track the current index
        j = len(nums)

        # These are running products
        # l_mult for everything to the left of the current index, and r_mult for everything to the right of the current index
        # Initially when i=0, there is nothing to the left of that spot so we default left[i] to 1
        # Similairly when i=0 that means j=len(nums)-1 and there is nothing to the right of that spot so we default right[j] to 1
        l_mult, r_mult = 1, 1

        # Only once we are done updating left and right should we update the multiplier values
        # l_mult will then be nums[i] and r_mult will be nums[j]
        # Then on the next pass through nums once i and j are updated, we will have values to use for multiplication

        # ex: i=0, j=3
        # l_mult = 1, r_mult = 1
        # update left and right 
        # left = [1, 0, 0, 0] right = [0, 0, 0, 1]
        # update l_mult *= nums[0] = 1
        # update r_mult *= nums[3] = 4

        # i=1, j=2
        # l_mult = 1, r_mult = 4
        # update left and right
        # left = [1, 1, 0, 0] right = [0, 0, 4, 1]
        # update l_mult *= nums[1] -> 1*2 = 2
        # update r_mult *= nums[2] -> 4*3 = 12

        # i=2, j=1
        # l_mult= 2, r_mult = 312
        # left = [1, 1, 2, 0] right = [0, 12, 4, 1]
        # etc.

        # forwards is i, backwards is j
        for i in range(len(nums)):
            j -= 1

            left[i] = l_mult
            right[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

        i, j = 0, len(nums)-1

        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        return res


