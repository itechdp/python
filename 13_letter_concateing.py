name = input("Enter your name :")
date = input("Enter a date: ")

letter = '''Dear <name> 
            
            You are selected!
            <Date>'''

letter = letter.replace("<name>",name)
letter = letter.replace("<Date>",date)

print(letter)