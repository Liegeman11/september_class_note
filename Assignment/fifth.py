# create a set calculator

# solution
"""
"""
# set1=input('Enter your first set: ')
# set2=input('Enter your second set: ')
# print("\nset operations:")
# print("""                                   1: union
#                                             2: intersection
#                                             3: difference(set2 - set1)
#                                             4: difference(set1 - set2)
#                                             5: superset(set2 - set1)
#                                             6: subset(set2 - set1)
#                                             7: superset(set1 - set2)
#                                             8: subset(set1 - set2)
#         """)
# operation1 =input("\nChoose a set operation by entering number (1-8): ")
# if operation1 == '1':
#     result = set1.union(set2)
# elif operation1 == '2':
#     result=set1.intersection(set2)
# elif operation1 == '3':
#     result=set1.different(set2)
# elif operation1 == '4':
#     result=set2.different(set1)
# print("\nResult of the operation: ", result)



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

# list_of_sets =[]
# num_of_set=int(input('how many set do you want to work with: '))
# for each_set in range(1, num_of_set+1):
#     set_items=[]
#     item ==int(input(f'how many value are in each set {each_set}: '))
#     for itm in range(1, item+1):
#         item=input(f'enter value {itm}: ')
# set_items.append(item)
# list_of_sets.append(set(set_items))
# print(list_of_sets)



print("Hello, you are welcome!")
sets = []
num_of_set = int(input("Enter the number of sets you want to work with: "))
for each in range(1, num_of_set + 1):
    print(f"\nEntering the details for set {each}")
    num_element = int(input(f"Enter the number of elements in set {each}: "))
    set_info = set()
    for all in range(1,num_element+1):
        enter_element = int(input(f"Enter element {all} in set {each}: "))
        set_info.add(enter_element)
    sets.append(set_info)
print(sets)
while True:
    print("""               
    1. Intersection
    2. Union
    3. Difference
    4. Symmetric Difference
    5. Check if Disjoint
    6. subset
    7. superset
    """)

    choice = input("Choose the operation you want to perform (1-7): ")
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        selected_indices = input("Enter the indices of sets to work with (e.g., 1 2): ")
        selected_sets=[]
        for index in selected_indices.split():
            if index.isdigit(): 
                index_int = int(index) 
                if 1 <= index_int <= num_of_set:
                    selected_sets.append(sets[index_int - 1]) 
        if len(selected_sets) < 2:
            print("Please select at least two valid sets.")
            continue
        
        if choice == '1':  
            result = set.intersection(*selected_sets)
            print("Intersection of selected sets:", result)
        elif choice == '2':  
            result = set.union(*selected_sets)
            print("Union of selected sets:", result)
        elif choice == '3':
            result = selected_sets[0].difference(*selected_sets[1:])
            print("Difference of selected sets:", result)
        elif choice == '4':
            result = set.symmetric_difference(*selected_sets)
            print("Symmetric Difference of selected sets:", result)
        elif choice == '5':
            result = all(selected_sets[i].isdisjoint(selected_sets[j]) for i in range(len(selected_sets)) for j in range(i + 1, len(selected_sets)))
            print("Are the selected sets pairwise disjoint?", result)
        elif choice == '6':
            result = all(selected_sets[0].issubset(s) for s in selected_sets[1:])
            print("Is the first set a subset of all selected sets?", result)
        elif choice == '7':
            result = all(selected_sets[0].issuperset(s) for s in selected_sets[1:])
            print("Is the first set a superset of all selected sets?", result)
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

    another = input("Do you want to perform another operation (yes/no)? ").strip().lower()
    if another != 'yes':
        print('Exiting the program')
        break