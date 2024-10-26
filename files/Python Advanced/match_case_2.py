if __name__ == '__main__':
    input_string = input("Enter Command: ")
    input_array : list[str] = input_string.split()

    """
        Expected Input: 
        Create : 
        Read:
        Update : 
        Delete :
        
    """

    match input_array:
        case ["create",*images]:
            print("Creating Images")
        case ["read",*images]:
            print("Reading Images")
        case ["update",*images] if(len(images)>1):
            print("Updating Images")
        case ["delete",*images] if(len(images)==1):
            print("Deleting Image")
        case _:
            print("Command not recognized")