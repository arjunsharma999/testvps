import requests

new_server = "http://103.174.102.113/home.php"

# Sam
params = {
    "id": "TIH_AGRI1",
    "data": "0912221305,21.27,24.88,00320,0018,0026,0012,06.99,0.3,12.4"
}

try:
    # Make request to new server
    response = requests.get(new_server, params=params)
    
    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    
    # Check if response contains "ACK"
    if "ACK" in response.text:
        print("Success! New server is returning ACK as expected.")
    else:
        print("Warning: New server response does not contain ACK.")
        
except Exception as e:
    print(f"Error occurred: {e}")