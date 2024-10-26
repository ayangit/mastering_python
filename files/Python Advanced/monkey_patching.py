import requests

def get(url: str):
    return ("Requesst Success!")



if __name__ == '__main__':
    requests.get = get
    data = requests.get('https://www.google.com')
    print(data)