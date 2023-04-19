list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    
    list_1.extend(list_2) 
    list_1 = sorted(list_1, key=lambda i: i['id'])  # Sorting based on id

    len1 = len(list_1)
    list_3 = []
    i=0
    while i<len1-1:
        if list_1[i]['id'] == list_1[i+1]['id']: 
            res = list_1[i]
            res.update(list_1[i+1])
            list_3.append(res)
            i+=2
        else:
            list_3.append(list_1[i])
            i+=1
    if list_1[len1-2]['id'] != list_1[len1-1]['id'] :
        # if the last element is not equal to previous one then append
        list3.append(list_1[len1-1])
    
    return list_3
    


list_3 = merge_lists(list_1, list_2)
print(list_3)
