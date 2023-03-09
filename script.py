import requests
from bs4 import BeautifulSoup

# Set the URL of the registration form
# You can update this URL with the one you get on your own machine, usually it's something like "https://auth0.openai.com/u/signup/identifier?state=XXXXXXXX"
form_url = 'https://chat.openai.com/auth/login?next=/chat'

# Read email addresses and passwords from the file
with open('list.txt') as f:
    lines = f.readlines()

# Read proxies from the file
with open('proxies.txt') as f:
    proxies = [{'http': line.strip()} for line in f]

# Loop over each line in the file and submit a registration request
for line in lines:
    # Split the line into email and password fields
    email, password = line.strip().split(':')

    # Set the data for the initial email submission
    email_data = {
        'email': email
    }

    # Send an HTTP POST request to submit the email and get the next form
    response = requests.post(form_url, data=email_data, proxies=proxies)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the "Continue" button and extract its URL
    continue_url = soup.find('button', {'type': 'submit'}).get('formaction')

    # Set the data for the password submission
    password_data = {
        'password': password
    }

    # Send an HTTP POST request to submit the password and complete registration
    response = requests.post(continue_url, data=password_data, proxies=proxies)

    # Check the response status code to see if the request was successful
    if response.status_code == 200:
        print(f'Account created successfully for {email}!')
    else:
        print(f'Error creating account for {email}: {response.text}')
