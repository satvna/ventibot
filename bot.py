import discord
from discord.ext import commands
import random
from Google import Create_Service

#<---------------- Youtube API Information ---------------->
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#Insert your playlist's ID here. It's the string of letters at the end of your
#playlist link.
playlist_id = 'your-playlist-id'

#------------------------------------------------
#               Functions
#------------------------------------------------

#<---------------- Add video to playlist ---------------->
def addToPlaylist(str):
    request = service.playlistItems().insert(
    part="snippet",
    body={
      "snippet": {
        "playlistId": playlist_id,
        "position": 0,
        "resourceId": {
          "kind": "youtube#video",
          "videoId": str
                      }
                 }
          }
    )
    response = request.execute()
    print(response)

client = commands.Bot(command_prefix = '.') #set command prefix

@client.event
async def on_ready():
    print('Bot is ready.')
    await bot.change_presence(activity = discord.Game('Yahoo!'))

#<---------------- Scan Messages For Links ---------------->
@client.event
async def on_message(message):
    messageContent = message.content
    if message.author == client.user: #if the bot sent this message
        return

    elif messageContent.startswith('https://youtu.be/'): #if it's a youtube link...

        messageContentList = messageContent.split()
        ytLink = messageContentList[0] #store link
        ytLink = ytLink.split("/") #then separate the video id
        ytLink_id = ytLink[-1]

        addToPlaylist(ytLink_id) #now add the video to the playlist!

    elif messageContent.startswith('https://www.youtube.com/'):
        messageContentList = messageContent.split()
        ytLink = messageContentList[0] #store link on its own
        ytLink = ytLink.split("v=") #then separate the video id
        ytLink_id = ytLink[-1]

        addToPlaylist(ytLink_id) #now add the video to the playlist!

    else: #otherwise, message does not contain yt link
        return

client.run('your-bot-token-here') #<--- insert your bot's unique token here
