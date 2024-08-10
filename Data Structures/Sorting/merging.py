def merge(nums1, nums2, depth=0):
    print('  '*depth, 'merge:', nums1, nums2)
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]
        
def merge_sort(nums, depth=0):
    print('  '*depth, 'merge_sort:', nums)
    if len(nums) < 2: 
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth+1), 
                 merge_sort(nums[mid:], depth+1), 
                 depth+1)
