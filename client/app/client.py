import requests
import sys

def main():
    url = "http://localhost:5000" #server is on port 5000
    query_string = {"latitude": 42.3601, "longitude": -71.0589} #place holder vals

    response = requests.get(url, params=query_string) #get requested data

    print(response.json()) #print json

if __name__ == "__main__":
    main()