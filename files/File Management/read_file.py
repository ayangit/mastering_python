# Using Open Keyword
# file = open('sample.txt',"r")
# print(file.read())
# file.close()


#Reading file using the with keyword
#Advantage is that is automatically close the file for us 
if __name__ == '__main__':

    with open('sample.txt','r') as text:
        #Reading the whole file
        # t: str = text.read()
        # print(t)

        #Reading file line by line
        # t: str = text.readline()
        # t2: str = text.readline()
        # print(t)
        # print(t2)

        #Making a list of lines
        t: list[str] = text.readlines()
        print(t)