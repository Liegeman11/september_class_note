import os
from pathlib import Path
import glob

# myfile=open("note.txt", 'r')
# print(myfile.read())
# myfile.close()

# myfile=open(r"C:\Users\pc\OneDrive\Documents\note\mynote.txt", 'r')
# myfile=open("C:\\Users\\pc\\OneDrive\\Documents\\note\\mynote.txt", 'r')      
# print(myfile.read())
# myfile.close()

# with open(r"C:\Users\pc\OneDrive\Documents\note\mynote.txt", 'r') as file:
#     content=file.read()
#     print(content)
    
# with open("example.txt", 'w+') as file:
#     content=file.write('i am the eraser you are looking for...')
#     print('job done')
#     content=file.read()
#     print(content)
    
# with open ('example.txt', 'r') as file:
# # with open ('example.txt', 'r+') as file:
#     content= file.write('one day one day one day pamilekeji...')
#     print('job done')
#     content=file.read()
#     print(content)

# with open(r"C:\Users\pc\OneDrive\Documents\note\mynote.txt", 'x') as file:
#     file.write("hellooo i am the new file")
#     print ('done')
    
# # pip install PyPDF2
# from PyPDF2 import PdfReader
# reader = PdfReader(r"C:\Users\pc\OneDrive\Documents\note\mynote.txt", 'r')


"""

"""
# num_of_dir = os.scandir()
# for files in num_of_dir:
#     print('files name: ', files)
# print(num_of_dir)

# list_my_files= os.scandir()
# with os.scandir(r"C:\Users\pc\OneDrive\Documents\note") as list_dir_content:
#     for files in list_dir_content:
#         print('files name: ',files)
# print(type(files))
# print(list_dir-content)

# all_path=Path()
# list_dir_content=Path(r"C:\Users\pc\OneDrive\Documents\note")
# for entry in list_dir_content.iterdir():
#     print(entry)
# print(type(entry))

# new_dir=os.mkdir('first_folder')
# print('done')

# new_dir2=os.mkdir(r'C:\Users\pc\OneDrive\Documents\note\newfolder2')
# print('done')

# os.mkdir(r'C:\Program Files\goodness\example4.pdf')
# print('done')
# my_file2=

directory_path='folder3'

if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    with open("folder3\myFiles1", 'w') as file:
        file.write('This is a py file created using python!')
    print('file successfully created')
else:
    print('file already exist')
    
    
# file_path=os.path.join(r"C:\Users\pc\OneDrive\Documents\note")

# filename pattern matching using glob

# print(glob.glob('*.txt')) 
# for file in glob.iglob('**/*.py', recursive=True):
#     print(file)
    
    
# for dirpath, dirnames, files in os.walk('.'):
#     print(f'i am : {dirnames}')
#     print(f'Available directory: {dirpath}')
#     for file_name in files:
#         print(file_name, 'files')
#     print()