"""HTTP stands for HyperText Transfer Protocol. It is the foundation of any data exchange on the 
Web and it is a protocol used for transmitting hypertext requests and information on the internet.
HTTP follows a classical client-server model where the client sends a request to the server, and 
the server responds with the requested resource or an error message.
In Python, the `requests` library is a popular choice for making HTTP requests. It provides a 
simple and intuitive API for sending HTTP requests and handling responses."""

#Get-to fetch data from a specified resource
#Post-to submit data to be processed to a specified resource
#Put-to update a current resource with new data
#Delete-to delete a specified resource




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
