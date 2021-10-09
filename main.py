# Python list method pop() removes
# and returns last object or obj from the list.
# .pop() last element .pop(0) first element

my_list = [123, 'Add', 'Grepper', 'Answer'];
print "Pop default: ", my_list.pop()
> Pop default:  Answer
# List updated to [123, 'Add', 'Grepper']
print "Pop index: ", my_list.pop(1)
> Pop index: Add
# List updated to [123, 'Grepper']