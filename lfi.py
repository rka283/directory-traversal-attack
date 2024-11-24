import requests
from urllib.parse import urlparse
a=input("enter any url")
with open("payload.txt","r") as f:
   attack=f.read()
with open("value.txt","r") as f1:
  value=f1.read() 
parsed_url=urlparse(a)
path=urlparse(a)
path=parsed_url.path
directory=path.rstrip('/').rsplit('/',1)[0]
if directory:
   url=a+attack
   response=requests.get(url)
   if value in response.text:
      print("url is vulnerable",response)
   else:
      print("url is not vulnerable")
