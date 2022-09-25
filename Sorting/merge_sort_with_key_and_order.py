def merge_sort(arr, key, descending=False):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_lists(left, right, arr, key, descending)

def merge_two_sorted_lists(a,b,arr, key, descending):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if (not descending and a[i][key] <= b[j][key]) or (descending and a[i][key] >= b[j][key]):
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    elements = [
        { 'name': 'test4',   'age': 27, 'time_hours': 2},
        { 'name': 'test3', 'age': 21,  'time_hours': 5},
        { 'name': 'test2',  'age': 23,  'time_hours': 0.5},
        { 'name': 'test1',  'age': 20,  'time_hours': 1},
    ]

    merge_sort(elements, key='time_hours')
    print('Sort by time_hours -> \n', elements, end='\n\n\n')
    merge_sort(elements, key='name')
    print('Sort by name -> \n', elements, end='\n\n\n')
    merge_sort(elements, key='age', descending=True)
    print('Sort by age and order by descending -> \n', elements, end='\n\n\n')
    
