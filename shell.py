#!/usr/bin/python3
# Code by PosiX and Science64

from threading import Thread
import requests

class ZeroScann():

    def __init__(self):
        site = input('Please enter website link: ')
        print("\n\033[96m[?] \033[0mStart Crawling...")
        print("\033[96m[!] \033[0mWait a sec!","\n")

        wordlist = open('wordlist.txt', "r").readlines()
        for psx in wordlist:
            url = f'{site}/{psx.strip()}'
            Thread(target=self.scan, args=(url,)).start()

    def scan(self, url):

        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"

        #list to hold the results we find
        #found = []

        try:
            req = requests.get(url, headers={"User-Agent": user_agent}, timeout=60)

            if req.status_code == 200:
                print(f'[*] Found {url}')
                #found.append(url)
            else:
                #print(url)
                pass

        except Exception as e:
            print(f'[!] There is error at requesting {e}')

        # if found:
        #     print("\n\033[96m[+] \033[0mResult Found\033[92m")
        #     print("\n".join(found))
        #     print("\033[96m[?] \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        # else:
        #     print("\n\033[96m[!] \033[0mCould Not Find Any Shell Backdoor")
        #     print("\033[96m[?] \033[0mTime Elasped: \033[33m%.2f\033[0m Seconds" % float(time.time()-starttime))

if __name__ == '__main__':
    ZeroScann()
