#!/usr/bin/python3
print('Content-type: text/html\r\n\r')
import os, makePizza, cgi

os.environ["PYTHONIOENCODING"] = "utf-8"

loc = os.path.dirname(os.path.abspath(__file__))
arguments = cgi.FieldStorage()
if arguments.has_key("ing1"):
    ingredient1 = arguments["ing1"].value
if arguments.has_key("ing2"):
    ingredient1 = arguments["ing2"].value
if arguments.has_key("ing3"):
    ingredient1 = arguments["ing3"].value
if arguments.has_key("ing4"):
    ingredient1 = arguments["ing4"].value
#print(arguments["horse"].value)

#this is a test API KEY (not required)
#apiKey = '<YOUR_TEST_API_KEY>'
#this is a real API KEY
#apiKey = '<YOUR_API_KEY>'

#facebook = facebook.GraphAPI(apiKey)

message = makePizza.makePizza(ingredient1="", ingredient2="", ingredient3="", ingredient4="")[0]
print(message)

#response = facebook.put_photo(image=open(os.path.join(loc, 'pizza2.png'), 'rb'), message=message)
#postId = response['post_id']
#print("Photo posted with id: " + postId)
