import re

url = input("Enter the Twitter URL? ").strip()

matches = re.search(r"^https?://twitter\.com/([a-zA-Z0-9]+)", url)

if matches:
    print(f"UserName: {matches.group(1)}")

#https://twitter.com/karthik2sekhar