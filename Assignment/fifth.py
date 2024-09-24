# create a set calculator

# solution
"""
"""
set1=input('Enter your first set: ')
set2=input('Enter your second set: ')
print("\nset operations:")
print("""                                   1: union
                                            2: intersection
                                            3: difference(set2 - set1)
                                            4: difference(set1 - set2)
                                            5: superset(set2 - set1)
                                            6: subset(set2 - set1)
                                            7: superset(set1 - set2)
                                            8: subset(set1 - set2)
        """)
operation1 =input("\nChoose a set operation by entering number (1-8): ")
result = operation1(set1, set2, operation1)
print("\nResult of the operation: ", result)



# def input_set():
#     elements = input("Enter elements of the set separated by space: ").split()
#     return set(elements)

# set1 = input_set()
# set2 = input_set()

# print("\nSet 1:", set1)
# print("Set 2:", set2)

# print("\nUnion of Set 1 and Set 2:", set1.union(set2))
# print("Intersection of Set 1 and Set 2:", set1.intersection(set2))
# print("Difference (Set 1 - Set 2):", set1.difference(set2))
# print("Difference (Set 2 - Set 1):", set2.difference(set1))
# print("Symmetric Difference:", set1.symmetric_difference(set2))

list_of_sets =[]
num_of_sety=int(input('how many set do you want to work with: '))
for each_set in range(1, num_of_set+1):
    set_items=[]
    items==int(input(f'how many value are in each set {each_set}: '))
    for itm in range(1, items+1):
        item=input(f'enter value {itm}: ')
set_items.append(item)
list_of_sets.append(set(set_items))
print(list_of_sets)

