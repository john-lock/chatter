# Overview:
Chatter is an implementation of a Pusher powered chat service to a central admin. Example uses to this would be on a site to handle customer service or support. Much of this code base can be easily sliced into a further project for usage. 

Users can enter a name, and provide a (unique) email address. The admin will see all active conversation and will be able to reply back instantly. Messages from the admin view have a constantly visable time & date stamp for reference. 

# Usage:
- Open the Admin view (at localhost:5000/admin).
- Start a chat in the client window (at localhost:5000/) to chat with the admin.
- Reply back from the admin window.
- Open more instances of this window to add more client conversations.

# Installation Instructions:
git clone https://github.com/john-lock/chatter.git
Setup virtualenv with `virtualenv venv` then activate with `source venv/bin/activate`
Install the requirements with `pip install -r requirements.txt`

Get API credentials from `pusher.com`. Once you sign up, create an app and you will get an App ID, Key & Secret. 

Set environment variables:
PUSHER_APP_ID 
PUSHER_APP_KEY
PUSHER_APP_SECRET
To do so use the following command format:
`$ export <var>=<value>`

Run the application with `flask run`

# TODO:
- Add Selenium tests for integration of client/admin connection
