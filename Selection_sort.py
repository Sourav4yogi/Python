
def smallest_num(array):
    return array.index(min(array))

def selection_sort(array):

    newlist=[]

    for i in range(len(array)):
        newlist.append(array[smallest_num(array)])
        array.remove(min(array))
    
    return newlist

print(selection_sort([22,21,33,65,211,333,2123,1,21,7622,1002]))