def find_length_of_lcis(nums)
    if nums.length() == 0
        puts 0
    end
    count = 1
    max = 0
    for i in 0..(nums.length()-1)
        if nums[i] < nums[i+1]
            count+=1
        
        elsif nums[i] > nums[i+1]
            max = count
            count = 1
        end
        puts max
    end
    
end

find_length_of_lcis([3,0,6,2,4,7,0,0])
