import requests

def send_msg(text):
    token = "1735947787:AAGURO9Lc3LVNvxsvofZN1mXZgZf69Kbc9A"
    chat_id = "1556934687"

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())
    
send_msg("Beeilung!")