'''

First Part:

Extract (Reader)
• Read a file from a directory.
• It can have any text.
• Provide that data to transformation part.

Transformation
• Apply below transformation on data provided by Reader.
• Capitalize the contents of the Data.
• Provide transformed data to writer.
Load (Writer)
• Write data provided by transformer into another output file in a different directory

• It should be easy to add or remove transformations
• Input source could change i.e. In future we could read contents from a SQL table
• Output source could also change i.e In future we could write contents to a SQL table

'''

#First Part

'''
Extract function is taking 3 argumets for file name as data , hard drive name as hdr_name and folder name as folder_name, after the collcting these information
function is reading the file, and returning to the function transformer().
'''
from soupsieve import select


def extract(data,folder_name,hdr_name,choice):

        if choice ==1:
            try:
                with open(f"{hdr_name}:\{folder_name}\{data}.txt",'r') as f:
                    content= f.read()
                    print(f"File Content: {content}")
                    return str(content)
            except: 
                print("Error: File or folder not found.")
        elif choice ==2: 
            # try:
                with open(f"{hdr_name}:\{folder_name}\{data}.sql",'r') as f:
                    f = f.readlines()
                    for i in f:
                        print(i)
                    return str(f)
            # except: 
            #     print("Error: File or folder not found.")


#Transformer function is converting all the data in uppercase and printing the data. 
def transformer(file_content):
    select = input("Do you want to use a transforamtion? y/n: ")
    if select == 'y' or select == 'Y':
        f_upr = str(file_content).upper()
        return str(f_upr)
    else: 
        return(file_content)

'''
To count the words of the given string we are converting, entire string to lower case then we are converting lower cased string into list and 
counting the words and again sending to the new generated file
'''
def transformer2(file_content):
    str1 = " "
    new_str1 = str1.join(file_content)
    converted_str = new_str1
    for i in converted_str: 
        j =converted_str.lower()
    return j

def convert(ol_str):
    new_str = str(ol_str)
    print(new_str)
    new_lis = list(new_str.split(" "))
    for i in new_lis: 
        j = new_lis.count(i)
        print(f"{i}->{j}")
    return j

'''
load function is taking one argument, as load_file which is returned by the fucntion transformer(), after taking the content of the file,
function is taking three user input first for New file name to store the transformed data, second hard drive name to select the hard drive for saving of file, 
and third one is folder which is working for saving the file at, accurate folder. 
'''
def load_txt(load_file):
    try: 
        name = input("\nGive name to new load file: ")
        print("\nEnter a name of Hard drive to save the file, for example: S: , W: , C: etc.")
        hd = input("Enter Hard Drive Name: ")

        print("\nTo save the file, enter your main folder name, and seprate the sub folder name with ' \ ' to save the file in folder, For Example: S:\dp\disk then press enter.")
        folder = input("\nEnter folder name where you want to save this file: ")

        with open(f"{hd}:\{folder}\{name}.txt",'w') as f:
            file = f.writelines(load_file)
            print(f"\nYour new data file has been created, with name {name}.txt")
            return str(file)
    except:
        print("Error: Check the file or folder name, and enter valid folder name and file name.")
        
#load_sql function is writing a new sql at given location from the user.
def load_sql(load_sql):
    try: 
        name = input("\nGive name to new load file: ")
        print("\nEnter a name of Hard drive to save the file, for example: S: , W: , C: etc.")
        hd = input("Enter Hard Drive Name: ")

        print("\nTo save the file, enter your main folder name, and seprate the sub folder name with ' \ ' to save the file in folder, For Example: S:\dp\disk then press enter.")
        folder = input("\nEnter folder name where you want to save this file: ")

        with open(f"{hd}:\{folder}\{name}.sql",'w') as f:
            file = f.writelines(list(load_sql))
            print(f"\nYour new data file has been created, with name {name}.sql")
            return str(file)
    except:
        print("Error: Check the file or folder name, and enter valid folder name and file name.")


#Second part

'''
Transformation
• Apply below transformation on data provided by Reader.
• Read all the unique words from the file. For each word calculate the word count
• For eg: for a file containing the content “Hello world, hello”
• In this case the summary would be
• hello -> 2
• world -> 1
• For simplicity cases should be ignored Hello and hello mean the same word.
• Provide thistransformed data to writer.
Load (Writer)
• Write data provided by transformer into another output file in a different directory
'''

print('''(1)
Transformation
• Apply below transformation on data provided by Reader.
• Capitalize the contents of the Data.
• Provide transformed data to writer.
Load (Writer)
• Write data provided by transformer into another output file in a different directory
''')

print('''(2)
Transformation
• Apply below transformation on data provided by Reader.
• Read all the unique words from the file. For each word calculate the word count
• For eg: for a file containing the content “Hello world, hello”
• In this case the summary would be
• hello -> 2
• world -> 1
• For simplicity cases should be ignored Hello and hello mean the same word.
• Provide thistransformed data to writer.''')


select = int(input("\nChoose Transformation part: "))

if select == 1:
    
    choice = int(input("Enter file type to proceed further, (1) .txt file (2) .sql file: "))

    if choice == 1:
        try:
            f_name = input("Enter text file name to extract: ")
            print("\nEnter a name of Hard drive to open the file, for example: S: , W: , C: etc.")

            dirN = input("Enter Hard Drive Name In uppercase: ")

            print("\nTo open the file, enter your main folder name, and seprate the sub folder name with ' \ ' to open the file in folder, For Example: S:\dp\disk then press enter.")
            folder = input("\nEnter folder name where you want to open that file: ")

            ext_file = extract(f_name,folder,dirN,choice)
            trans_file = transformer(ext_file)
            loaded_file = load_txt(trans_file)
        except: 
            print("Error: Check the file or folder name, and enter valid folder name and file name.")

    elif choice ==2:
        try:
            f_name = input("Enter text file name to extract: ")
            print("\nEnter a name of Hard drive to open the file, for example: S: , W: , C: etc.")

            dirN = input("Enter Hard Drive Name In uppercase: ")

            print("\nTo open the file, enter your main folder name, and seprate the sub folder name with ' \ ' to open the file in folder, For Example: S:\dp\disk then press enter.")
            folder = input("\nEnter folder name where you want to open that file: ")

            ext_file = extract(f_name,folder,dirN,choice)
            trans_file = transformer(ext_file)
            loaded_file_sql = load_sql(trans_file)
        except: 
            print("Error: Check the file or folder name, and enter valid folder name and file name.")

    else: 
        print("Choose a valid file type.")

elif select ==2:

    choice2 = int(input("Enter file type to proceed further, (1) .txt file (2) .sql file: "))
    if choice2 == 1:
        try:
            f_name = input("Enter text file name to extract: ")
            print("\nEnter a name of Hard drive to open the file, for example: S: , W: , C: etc.")

            dirN = input("Enter Hard Drive Name In uppercase: ")

            print("\nTo open the file, enter your main folder name, and seprate the sub folder name with ' \ ' to open the file in folder, For Example: S:\dp\disk then press enter.")
            folder = input("\nEnter folder name where you want to open that file: ")

            ext_file = extract(f_name,folder,dirN,choice2)
            trans_file = transformer2(ext_file)
            convert2 = convert(trans_file)
            loaded_file = load_txt(convert2)
        except: 
            print("Error: Check the file or folder name, and enter valid folder name and file name.")

    elif choice2 ==2:
        try:
            f_name = input("Enter text file name to extract: ")
            print("\nEnter a name of Hard drive to open the file, for example: S: , W: , C: etc.")

            dirN = input("Enter Hard Drive Name In uppercase: ")

            print("\nTo open the file, enter your main folder name, and seprate the sub folder name with ' \ ' to open the file in folder, For Example: S:\dp\disk then press enter.")
            folder = input("\nEnter folder name where you want to open that file: ")

            ext_file = extract(f_name,folder,dirN,choice2)
            trans_file = transformer2(ext_file)
            convert2 = convert(trans_file)
            loaded_file_sql = load_sql(convert2)

        except: 
            print("Error: Check the file or folder name, and enter valid folder name and file name.")

    else: 
        print("Choose a valid file type.")

#Github profile : www.github.com/itechdp