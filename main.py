import requests

# Target server
new_server = "http://103.174.102.113/"

# Append %22 (which is URL encoded for double quote) at the end of the data string
params = {
    "id": "TIH_AGRI1",
    "data": '0912221305,21.27,24.88,00320,0018,0026,0012,06.99,0.3,12.4"'  # <-- literal double quote at the end
}

try:
    # Send GET request
    response = requests.get(new_server, params=params)
    
    # Print response status and content
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    
    # Check if ACK is received
    if "ACK" in response.text.upper():
        print("✅ Success! ACK received from server.")
    else:
        print("⚠️ No ACK in response.")
        
except Exception as e:
    print(f"❌ Error occurred: {e}")
