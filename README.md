# ChatGPT Account Creator Bot OpenAI - For BlackHatProTools.info

Account creator for ChatGPT - OpenAI - Supports Proxies

This is a python script bot, that creates automatically accounts for Chatgpt.

It supports proxies, loading them from an external list "proxies.txt" and a list of email addresses/passwords "list.txt".

Proxies format must be: proxies:port
Email/pass format must be : email:password

This code reads each line from list.txt and splits it into email and password fields using the split() method. It then sends an HTTP POST request to the registration form with the email field data, extracts the URL of the "Continue" button using BeautifulSoup, and sends a second HTTP POST request to submit the password and complete the registration process.

Note that this code assumes that each line in list.txt contains only one email address and password pair in the format email:password. If the file contains additional information, you may need to modify the code to handle it appropriately.

You would still need a phone number (you can use the ones for free on internet to receive sms) to valide your accounts.


This code reads the list of proxies from a file named proxies.txt in the current directory, and constructs a list of dictionaries containing the proxy information in the format expected by the requests library.

The proxies parameter is then passed to the requests.post() method to use the proxy for the requests.

Note that this code assumes that each line in proxies.txt contains only one proxy in the format proxy:port. If the file contains additional information, you may need to modify the code to handle it appropriately. Additionally, keep in mind that not all proxies may work, and some may be slow or unreliable.


Enjoy :)
