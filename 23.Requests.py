import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response)
print(response.text)

#Example of https methods

payload={
    'title':'Learning RestAPI',
    'body':'This is a test post',
    'id':1
}

response_post=requests.post("https://jsonplaceholder.typicode.com/posts",
                            json=payload)

print(response_post.status_code)
print(response_post.json)

update={
    'title':'Updated Title'
}

response_put=requests.put("https://jsonplaceholder.typicode.com/posts/1",json=update)

print(response_put.status_code)
print(response_put.json)

responce_delete=requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(responce_delete.status_code)
