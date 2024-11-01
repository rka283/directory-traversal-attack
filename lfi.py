import requests
response = None 
with open("payload.txt","r") as f:
    attack=f.read()
with open("value.txt","r") as fi:
    value=fi.read()
a=input("enter the url")
try:
  response=a.head(a)
except:
    print("its not vulnerable ")
if response == 200:
 a=a.remove(response)
 for i in attack:
   k=a+i
   url=requests.get(k)
   if url == 200:
    if value in url.txt:
      print("its vulnerable")
   else:
      print("its not")
      
  


