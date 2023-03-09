# ChatGPTAccountCreator
Account creator for ChatGPT - OpenAI - Supports Proxies

This is a python script bot, that creates automatically accounts for Chatgpt.

It supports proxies, loading them from an external list "proxies.txt" and a list of email addresses/passwords "list.txt".

Proxies format must be: proxies:port
Email/pass format must be : email:password

This code reads each line from list.txt and splits it into email and password fields using the split() method. It then sends an HTTP POST request to the registration form with the email field data, extracts the URL of the "Continue" button using BeautifulSoup, and sends a second HTTP POST request to submit the password and complete the registration process.

Note that this code assumes that each line in list.txt contains only one email address and password pair in the format email:password. If the file contains additional information, you may need to modify the code to handle it appropriately.

You would still need a phone number (you can use the ones for free on internet to receive sms) to valide your accounts.

Enjoy :)
