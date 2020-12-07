from proxy_requests import ProxyRequests
import time
import os

os.system('cls')
os.system('title IPLoggers Are Gay, Lets Spam This One')
url = input('URL: ')
os.system('cls')
reqcount = int(input('Number Of Requests To Send: '))
os.system('cls')
uagent = input('User Agent: ')

os.system('cls')
print('Sending Requests, This May Take A While')
for i in range(reqcount):
    headers = {
        'User-agent': f'{uagent}',
    }
    r = ProxyRequests(url)
    r.set_headers(headers)
    r.get_with_headers()
