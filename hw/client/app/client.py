import requests

def main():
    url = "http://server:5000" #server is on port 5000
    coords = {"latitude": 17.375, "longitude": 78.5} #place holder vals

    response = requests.get(url, params=coords) #get requested data

    print(response.json()) #print json

if __name__ == "__main__":
    main()