import os

#print(dir(os))
print(os.getcwd()) #get current working directory
#os.chdir("c://") #change current dirctory
f = open('Kumar.txt')
print(f)

#listdir function
print(os.listdir("C://")) #print all files situated in the folder
#print(os.listdir())
print(type(os.listdir("C://"))) #This is the type of list

#make new folder in the directory
#os.makedirs('Nishant/that') #this command will make directories 
#os.mkdirs('Raj') #this folder will make a single directory
#os.rename('Kumar.txt','Kuma.txt')

#Enviroment Variable
#print(os.environ.get('Path'))
print(os.path.join('C://',"harry.txt"))

print(os.path.exists("C://")) #It will true if the dircetory exist
print(os.path.isfile("C://Program Files2")) #it will return false because this file not exist in this
