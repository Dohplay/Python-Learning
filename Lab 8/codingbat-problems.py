def first_last6(nums):
    """
    detect if first or last number is "6" when defining a list
    """
    
    num6 = False
    if nums[0] == 6:
        num6 = True
    elif nums[len(nums)-1] == 6:
        num6 = True
        
    return num6


def common_end(a, b):
    """
    Check if list a & b have the same first values or last values
    """
    
    firstLastSame = False
    if a[0] == b[0]:
        firstLastSame = True
        
    elif a[len(a)-1] == b[len(b)-1]:
        firstLastSame = True
        
    return firstLastSame
  

def reverse3(nums):
    """
    Return the reverse of an array with 3 indices
    """
    reverse = [nums[2], nums[1], nums[0]]
    return reverse  

def middle_way(a, b):
    """
    Return a list that has the middle values of lists a & b that have 3 indices
    """
    middleList = [a[1], b[1]]
    return middleList

def same_first_last(nums):
    """
    Return true if the list is not empty and the first & last indices are equal
    """
    len_and_firstLast = False
    
    if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
        len_and_firstLast = True
    return len_and_firstLast  

def sum3(nums):
    """
    Return the sum of a list with three indices
    """
    sum = nums[0] + nums[1] + nums[2]
    return sum
    
def max_end3(nums):
    """
    Find if first or last is larger and create an array that is set to that
    value
    """
    if nums[0] >= nums[2]:
        value = nums[0]
    else:
        value = nums[2]
    newArray = [value, value, value]
    return newArray
  
def make_ends(nums):
    """
    return a length 2 array with the first and last index values in num
    """
    makeEnds = [nums[0], nums[len(nums)-1]]
    return makeEnds
    
def make_pi():
    """
    pi list
    """
    pi = [3,1,4]
    return pi    

def rotate_left3(nums):
    """
    rotate left length 3 llist
    """
    rotate = [nums[1], nums[2], nums[0]]
    return rotate

def sum2(nums):
    """
    return sum of first two indices
    """
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        sum = nums[0] + nums[1]
        return sum

def has23(nums):
    """
    check if the number is 2 or 3 in a list with 2 indices
    """
    has23 = False
    if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
        has23 = True
    return has23

def count_evens(nums):
    """
    check the number of even numbers in the list
    """
    count = 0
    for items in nums:
        if items % 2 == 0:
            count += 1
    return count

def big_diff(nums):
    """
    Calculates the difference between the largest and smallest values in
    a list
    """
    largest = nums[0]
    smallest = nums[0]
    for items in nums:
        if items > largest:
            largest = items
        if items < smallest:
            smallest = items       
    difference = largest - smallest
    return difference

def has22(nums):
    """
    check if there are two consecutive 2's
    """
    has22 = False
    for items in range(len(nums)-1):
        if nums[items] == 2 and nums[items+1] == 2:
            has22 = True
    return has22

def centered_average(nums):
    """
    find the centered average of a list
    """
    largest = max(nums)
    smallest = min(nums)
    sum = 0
    for items in nums:
        sum += items
    finalSum = sum - largest - smallest
    average = finalSum/(len(nums)-2)
    return average
         
