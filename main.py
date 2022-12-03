# import requests

# def handler(event, context):
#     response = get_url("http://checkip.amazonaws.com")
#     print("My IP is:", response.text)


# def get_url(url):
#     try:
#         response = requests.get(url)
#     except:
#         response = None

#     return response

# handler(None, None)
import os

def main():
    # reading the NAME environment variable
    # if it doesn't exist, we will use "stranger" as default
    name = os.getenv("NAME", "stranger")
    print(f"Hello bro, {name}!")

if __name__ == "__main__":
    main()