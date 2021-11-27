#!/usr/bin/python3
print('Content-type: text/html\r\n\r')
import os, makePizza, cgi

os.environ["PYTHONIOENCODING"] = "utf-8"

loc = os.path.dirname(os.path.abspath(__file__))
arguments = cgi.FieldStorage()
for i in arguments.keys():
    print(arguments[i].key + ":" + arguments[i].value)

#this is a test API KEY (not required)
#apiKey = '<YOUR_TEST_API_KEY>'
#this is a real API KEY
#apiKey = '<YOUR_API_KEY>'

#facebook = facebook.GraphAPI(apiKey)

#message = makePizza.makePizza(loc, False)[0]
#print(message)

#response = facebook.put_photo(image=open(os.path.join(loc, 'pizza2.png'), 'rb'), message=message)
#postId = response['post_id']
#print("Photo posted with id: " + postId)
