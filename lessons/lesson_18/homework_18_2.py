import requests

BASE_URL = "http://127.0.0.1:8080"

with open("mars_photo1.jpg", "rb") as image_file:
    files = {'image': image_file}

    post_response = requests.post(url=f"{BASE_URL}/upload", files=files)

print(post_response.status_code)
print(post_response.text)

print('='*25)
headers = {"Content-Type": "text"}
get_response = requests.get(url=f"{BASE_URL}/image/mars_photo1.jpg", headers=headers)
print(get_response.status_code)
print(get_response.text)

print('='*25)
delete_response = requests.delete(url=f"{BASE_URL}/delete/mars_photo1.jpg")
print(delete_response.status_code)
print(delete_response.text)