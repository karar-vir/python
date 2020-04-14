#creating a file with the help of funtion
def createfile(fname):
    txt=open(fname)
    txt.write('hello createfuntion')
    txt.close()
createfile('createfile.txt')
