import requests

if __name__ == "__main__":

    r=requests.get("https://wwww.atentus.com/")
    print (r.text)