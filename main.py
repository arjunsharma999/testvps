import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.text == "ACK":
            print("Received ACK from the server")
        else:
            print("Did not receive ACK from the server. Response was:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending request:", e)

new_server_ip = "103.174.102.113"
url = f"https://{new_server_ip}/home.php?id=TIH_AGRI1&data=0912221305,21.27,24.88,00320,0018,0026,0012,06.99,0.3,12.4"
check_url(url)
