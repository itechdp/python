def game():
    return 600

score = game()
with open('hiscore.txt') as f:
    hiscore = f.read()

if hiscore=='':
    with open('hiscore.txt','w') as f:
        f.write(str(score))

elif int(hiscore)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))

# first of all we are returning one value which is more than the high score and then we are assigning that value to 
# score varialbe and then we are opening the file and reading the hiscore and then if the hiscore is empty we are writing
# our score in the file and another condition is if our socre is greater than the hiscore then the score value will be 
# write in the hiscore file