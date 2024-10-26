import os
from os import remove

if __name__ == '__main__':
    #Note os is a powerful module it can delete file  from anywhere in the computer
    # Use it with caution
    # os.remove('test2.txt')
    folder_name :str  = 'sample_folder/'
    for file in os.listdir(folder_name):
        print(file)
        if(os.path.exists(folder_name+file)):
            print(f'{file} exists')
            print(f'Now deleting {file}')
            #we need to give folder_name + file name only file name won't work
            #because the file is inside that folder
            os.remove(folder_name+file)
    # Now deleting the folder :
    if os.path.exists('sample_folder'):
        os.rmdir('sample_folder')
