# val=6
# if val < 8:
#     print('correct')
#     if val == 6:
#         print('the value is 6')
#     if val >= 6:
#         print('the value is 66')
#     if val <= 6:
#         print('the value is 6')
# elif val % 2 ==0:
#     print('this is an even number')
# else:
#     print('incorrect')

# turns=0
# list_itm=['mango', 'orange', 'apple', 'pineapple', 'cashew']
# # print(type(list_itm))
# for fruits in list_itm:
#     turns+=1
#     print("This is {}".format(fruits))
#     print("round {} >>> This is{}".format(turns, fruits))
    
    
    # list_itm1=['mango', 'orange', 'apple', 'pineapple', 'cashew']
    # list_itm2=['basket', 'container', 'bucket']
    # for fruits in list_itm:
    #     turns+=1
    #     print("This is{}".format(fruits))
    #     print("round {} >>> This is{}".format(turns, fruits))
    
for i in range(1,13):
    for j in range(1, 16):
        print(i*j, end='\t')
    print()
    
# multiplication Table

# for i in range (1,13):
#     for j in range (1,15):
#         print(i*j,end='\t')
#     print()
    
    
for num1 in range(1, 6):
    for num2 in range(1,13):
        res=num1 * num2
        # print(f"{num1} * {num2} ={res}", end='\t')
        print(f"{res}" , end='\t')
    print()




#while loop or while True

# num=0
# while True:
#     num+=1
#     print('Welcome!!!')
#     if num==5:
#         break

# num=0
# while num <= 5:
#     num+=1
#     print('number{}'.format(num))
#     print('Hello')
    
    
# num=0
# while num <= 5:
#     print('Hello')
#     num+=1
#     print('number{}'.format(num))

# ternary statement

# num=4
# print('hello') if num <=4 else print('error')