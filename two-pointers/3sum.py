def three_sum(nums):
    # Sort the array to make it easier to handle duplicates and find triplets
    nums.sort()
    result = []

    # Iterate through the array
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize left and right pointers
        left, right = i + 1, len(nums) - 1

        # Check for triplets
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1  # Move left pointer to increase the sum
            elif total > 0:
                right -= 1  # Move right pointer to decrease the sum
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for both left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move pointers to the next unique elements
                left += 1
                right -= 1

    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)

