if __name__ == '__main__':
    status : int = 4

    match status:
        case 200:
            print("Success!")
        case 404:
            print("Not Found...")
        case 500 :
            print("Internal Server Error...")
        case _:
            print("Code not recognized")