import time

def quicksort(items):
    #print(f"SORTING: {items}")
    if len(items) <= 1:
        return items
    # 1. Select the last element as the pivot.
    pivot = items[-1]
    left = []
    right = []
    for i in range(len(items) - 1):
        item = items[i]
        if item < pivot:
            # 2. Move all elements smaller than the pivot to the left.
            left.append(item)
        else:
            # 3. Move all elements greater than the pivot to the right.
            right.append(item)
    #print(f"LEFT: {left}, PIVOT: {pivot}, RIGHT: {right}")
    # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
    return quicksort(left) + [pivot] + quicksort(right)


start_time = time.time()

f = open('/Users/ljohnson/repos/CS/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/Users/ljohnson/repos/CS/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

def find_dups(list_1, list_2):
    i = j = 0
    duplicates = []

    while i < len(list_1) and j < len(list_2):
        if list_1[i] > list_2[j]:
            j += 1
        elif list_1[i] < list_2[j]:
            i += 1
        else:
            duplicates.append(list_1[i])
            i += 1
            j += 1

    return duplicates

# quicksort : O(n log(n) 
# After sorted, this solution requires a single traversal, O(n)

duplicates = find_dups(quicksort(names_1), quicksort(names_2))

#duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
