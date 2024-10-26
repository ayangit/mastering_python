if __name__ == '__main__':
    # with open('sample.txt','a') as text:
    #     text.write("\n5th Line")
    #     #in "a" mode we cannnot read we need to use a+ mode
    #     print(text.read())
    #If I gibe text.read outside the with block will give ValueError: I/O operation on closed file.
    # print(text.read())

    # with open('sample.txt','a+') as text:
    #     text.write("\n6th Line")
    #     #the write operation brings the  cursor to the end of the file
    #     # we need to do seek operation to  bring it to the begining
    #     text.seek(0)
    #     print(text.read())

    #While append mode appends at the last of the file
    #Write mode always replaces the text
    with open('sample.txt','w+') as text:
        text.write("REPLACED")
        text.seek(0)
        print(text.read())