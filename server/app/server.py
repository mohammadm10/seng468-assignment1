import requests
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

def server():
    class RequestHandler(SimpleHTTPRequestHandler):
        #Takes incoming traffic as the input to extract the latitude and longitude from the request
        def do_GET(self):
            parsed_path = urlparse(self.path)
            #Check if the request contains both the parameters we want
            if('latitude' in parsed_path.query and 'longitude' in parsed_path.query):
                latitude = parse_qs(parsed_path.query).get('latitude')
                longitude = parse_qs(parsed_path.query).get('longitude')
                print("Received request with latitude=" + str(latitude) + " and longitude=" + str(longitude))
                data = fetchWeather(latitude, longitude) #get json data from the api request
                if data:
                    response = json.dumps(data).encode('utf-8')
                    self.send_response(200) #Successful request
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Content-Length', len(response))
                    self.end_headers()
                    self.wfile.write(response)
                
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, RequestHandler)

    print('Server listening on port 5000')
    httpd.serve_forever()#listen on port 5000
        
#This function is called after a successful request is sent to the server 
#It accepts the latitued and longitude values to make a request to the
#OpenWeatherMap api
def fetchWeather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "cb6fa3ab0249e0e985302fa62ebd7323"

    params = {"lat": lat, "lon": lon, "appid": api_key}

    res = requests.get(url, params=params)
    
    if res.status_code == 200:
        data = json.loads(res.content)
        return data
    else:
        print("Request failed with status code {res.status_code}")
    
def main():
    server()

if __name__ == "__main__":
    main()
