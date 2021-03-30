								+------------------+
								|	  Ventibot     |
								|	  version      |
								|	    1.0        |
								+------------------+
								(\__/) ||
								(•ㅅ•) ||
								/ 　 づ
+-------------------------+
		 About
+-------------------------+
Ventibot is a simple bot that uses the Youtube API to store Youtube links in a single playlist.
It requires you to create a project in the Google Developer's Console with O2Auth.

The heroku folder contains the Procfile and requirements.txt needed to host this bot on heroku.
If you don't need them, feel free to delete the folder.

!! Ventibot will read all of the Youtube links sent to your server.
	If you don't want Ventibot to read YT links from a channel, you have to disable its ability
	to read from that channel via server permissions. 

!! Ventibot will only store a link if the message begins with that link.
	
If you need any help setting this up, message me on Discord:
i refuse to divorce my wife#9496

+-------------------------+
 Installation Instructions
+-------------------------+

1. Create your bot in the Discord developer console.

2. Set up your Youtube API:
		- Create an account in the Google Developer Console. Create a project.
		- Click on "ENABLE APIS AND SERVICES", and enable Youtube Data API v3.
		- Create credentials:
			- Where will you be calling the API from? 	Web server (e.g. node.js, Tomcat)
			- What data will you be accessing?			User  data
		- Create OAuth consent screen:
			- Enter whatever you want for App Data
			- Ignore scopes.
			- !! Add the account with your playlist as a test user.
		- Go back to the credentials tab in the sidebar:
			- Create OAuth client ID:
				- App type: Desktop app
				- Name it anything you want.
				- Download the file from under OAuth 2.0 Client IDs.
				- Rename the file "client_secret.json" and place it in your bot's directory.
				
3. In bot.py, add the following to the code:
		- On line 16, add your playlist ID.
		- On line 74, add your bot's unique token. You can get this from the Discord developer console.
		
	I would recommend running it locally first, to go through the authorization steps.
	
Here are libraries you need to install:
		- google-api-python-client 
		- google-auth-httplib2 
		- google-auth-oauthlib
		
You can install all three with this command:
	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


+-------------------------+
  Extra information
+-------------------------+
This bot was created so that I wouldn't have to go back and click on all the links my friends
send to our music channel one by one. 
...but it turns out this bot is cursed! After you go through all the trouble to set this up,
nobody will every send Youtube links to your chat again!