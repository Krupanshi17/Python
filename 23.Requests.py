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