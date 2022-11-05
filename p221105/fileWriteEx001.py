import requests
import os

r = requests.get("https://images.unsplash.com/photo-1452857576997-f0f12cd77844?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80")
print(type(r))
# requests.models.Response 
with open("photo.jpg", "wb") as f:
    print(type(f))
    print(type(r.content))
    f.write(r.content)