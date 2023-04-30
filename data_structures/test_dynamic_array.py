from utils.dynamic_array import DynamicArray

arr = DynamicArray()

# test push_back
print("Pushing back")
for i in range(10):
    arr.push_back(i)
    print('Size: {} Capacity: {}'.format(arr.get_size(), arr.get_capacity()))

# test pop_back
print("Popping back")
for i in range(10):
    arr.pop_back()
    print('Size: {} Capacity: {}'.format(arr.get_size(), arr.get_capacity()))

# test insert'
print("filling")
for i in range(10):
    arr.push_back(i)
    print('Size: {} Capacity: {}'.format(arr.get_size(), arr.get_capacity()))

print(arr.get_arr())
print("Inserting")
for i in range(3):
    arr.insert(1, i)
    print(arr.get_arr())
    print('Size: {} Capacity: {}'.format(arr.get_size(), arr.get_capacity()))
    
# test delete
print("Deleting")
for i in range(3):
    arr.delete(1)
    print(arr.get_arr())
    print('Size: {} Capacity: {}'.format(arr.get_size(), arr.get_capacity()))
    
# fill array with 0, 1, 2
for i in range(10):
    arr.push_back(i%3)
    print('Size: {} Capacity: {}'.format(arr.get_size(), arr.get_capacity()))
    
# test remove
arr.remove(2)
print(arr.get_arr())

# test find
assert arr.find(3) == 2