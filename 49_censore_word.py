with open('sample.txt','r') as f:
    censor = f.read()
    
with open('sample.txt','w') as f:
    if 'gadhe' in censor:
        newword =  censor.replace('gadhe','******')
        f.write(newword)

# in this program we are open on file which is contain some word which are going to be censor by the programmer so first we open that file which we want to 
# use then read the content of that file and then open that file to replace the censor word with the new another word, for that open that file and 
# just store into newword and just write that file 