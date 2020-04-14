#read the file using the help of funtion
def readfile(myfirstfile):
    txt=open(myfirstfile)
    print(txt.read())
readfile('test.txt')
