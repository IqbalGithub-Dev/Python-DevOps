import requests

print("send the waiter to bring the joke")

url = "https://official-joke-api.appspot.com/random_joke"
waiter_response = requests.get(url)
joke =  waiter_response.json()
print("\n Here is your joke ")
print("- " + joke['setup'])
print("- " + joke['punchline'])