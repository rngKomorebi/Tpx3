import requests 
from webbot import Browser
web = Browser()

session_requests = requests.session()
login_url = "https://logbook.tok.ipp.cas.cz/index.php?action=login"
# login_url = "https://www.tok.ipp.cas.cz/webcdb"
# login_url = "https://www.google.com/"

result = session_requests.get(login_url)

payload = {
    'name': 'kulkov',
    'pass': 'nejakejTenVUL168'
}

with requests.Session() as session:
    post = session.post(login_url, data=payload)
    
web.click("WEB CDB")

if result:
    print('Response OK')
else:
    print('Response Failed')
    
print (post.cookies)