nums = [0,0,1,1,1,2,2,3,3,4]

for i in range(0,len(nums)):
            for j in range(i+1,len(nums)-1):
                if nums[i] == nums[j]:
                    del nums[j]
            print(nums,i,j)
        