def binary_search(array,item):
    high=len(array)-1
    low=0

    
    while high>=low:
        mid=int((high+low)/2)
        guess=array[mid]
        
        if guess==item:
            return mid
        
        if guess>item:
            high=mid-1
            
        else:
            low=mid+1
    return None


array=[1,3,5,7,9]

print(binary_search(array, -1))