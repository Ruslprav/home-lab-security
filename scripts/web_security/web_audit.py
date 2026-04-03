import requests
import os

WORDLIST_PATH = os.path.join(os.path.dirname(__file__), "wordlist.txt")
TARGET_URL = "http://127.0.0.1:8080"

def scan_web(url, directory_list):
    print(f"--- Starting Web Audit for {url} ---")
    for path in directory_list:
        full_url = f"{url}/{path}"
        try:
            response = requests.get(full_url, timeout=2)
            if response.status_code == 200:
                print(f"[!!!] VULNERABILITY FOUND: Accessible path {full_url}")
            elif response.status_code == 403:
                print(f"[OK] {path}: Forbidden (Protected)")
        except requests.exceptions.ConnectionError:
            print("[ERROR] Server is offline. Check your target.")
            break

if __name__ == "__main__":
    scan_web(TARGET_URL, WORDLIST_PATH) 
