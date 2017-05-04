import os

numFile = 25
listaNomi= []
i = 1
f = open('immagini.txt')
lines = f.readlines()
f.close()
for line in lines:
    listaNomi+= [line[0:line.find(" ")]+" -"+line[line.find(" "):line.find("\n")]] #:line.find("-")

while i<=numFile:
    os.rename(str(i)+".png", listaNomi[i-1]+".png")
    print str(i)+" fatto"
    i+=1
    print str(i)+" da fare"
###
#for path in os.listdir(os.getcwd()+"\s1"):
#    print path
#    os.rename(path,listaNomi[int(path[0:path.find(".")])-1]+".flv")
#    
#    print path[0:path.find(".")]+"fatto"
###

