def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # Step 1: Prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Step 2: Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# ----------- Driver Code (VS Code) -----------
if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    result = productExceptSelf(nums)
    print("Output:", result)
