import requests
import json

# Joke API URL
ENDPOINT = 'https://official-joke-api.appspot.com/random_joke'

def get_joke(name):
    response = requests.get(ENDPOINT)
    # print(f"Response: {response}")

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    if response.status_code == 200:
        data = response.json()
        # print(f"Data: {data}")

        # Extract and print out joke
        joke = data['setup'] 
        punchline = data['punchline']

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Hi, {name}")
        guess = input(f"{joke} ")
        if (guess.lower() == punchline.lower()):
            print("That's right!")
        else:
            print(f"{punchline}")

    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if (response.status_code == 400): 
            print(f"Error: {response.status_code}. Bad request")
        elif (response.status_code == 401): 
            print(f"Error: {response.status_code}. Unauthorized access")
        elif (response.status_code == 404): 
            print(f"Error: {response.status_code}. Not found")
        else: 
            print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    name = input('Enter your name: ')
    get_joke(name)
