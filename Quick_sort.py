def quick(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        
        return quick(less)+[pivot]+quick(greater)
    
    
print(quick([9,6,4,3,7,1]))

