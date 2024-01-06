#Bubble Sort with early end if no swaps within a pass 

nums = [5,4,3,2,1]
endEarly = False

for i in range(len(nums) - 1):
    if(endEarly): 
        break 
    endEarly = True
    for j in range(len(nums) - 1): 
        if(nums[j] > nums[j+1]):
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            endEarly = False 


print(nums)


    