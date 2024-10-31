import re


text = """ the value of a thing will be determine the capacity you put in """.strip()
print(text.startswith("the"))

val = re.search("^the.*it$")
print(val)
print(val.group())



comment =""" of the value of a thing will determine the capacity you put in. the value of 2019 is what you get in 2020 and now you get the value of 2020 in 2021""".strip()

# match =re.search("\wof*", comment)
# print(match)
# if match:
#     print("we have a match")
# else:
#     print("no match detected")
    
# match = re.findall('of', comment)
# print(match)
# if match:
#     print("we have a match")
# else:
#     print("no match detected")

x = re.findall(r'you', comment)
print(x)
x = re.search(r'you', comment)
print(x)
print(x.span())
print(x.group())
print(x.string)
print(re.search(r'\bt', comment))
z= re.split(r'\s', comment)
print(z)
z = re.split(r'\s', comment, 5)
print(z)

tx = re.sub(r'\d{4}', '1980', comment)
print(tx)

tx = re.sub(r'[0-9][0-9],[0-9][0-9]', '1980', comment)
print(tx)
tx = re.sub(r'capacity')