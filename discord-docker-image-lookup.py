import discord
import json
import os
import urllib3
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$docker'):
        message_content_words = message.content.split()
        message_content_image = message_content_words[-1]

        http = urllib3.PoolManager()

        auth_fields = json.dumps({
            "username": os.environ['DOCKER_USERNAME'],
            "password": os.environ['DOCKER_TOKEN']
        })

        auth_url = "https://hub.docker.com/v2/users/login"
        auth_resp = http.request(
            "POST",
            auth_url,
            headers={
            "Content-Type": "application/json"
            },
            body=auth_fields
        )

        auth_token = json.loads(auth_resp.data)["token"]

        image_url = "https://hub.docker.com/v2/repositories/"+message_content_image+"/tags"

        image_resp = http.request(
            'GET',
            image_url,
            headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer "+auth_token
            }
        )

        message_content = "\n"
        for result in json.loads(image_resp.data)["results"]:
            for image in result["images"]:
                if result["name"] == "latest":
                    message_content += result["name"]+" "+image["architecture"]+str("" if image["variant"] is None else ":"+image["variant"])+" "+image["last_pushed"]+"\n\n"

        await message.reply(message_content)

client.run(os.environ['DOCKER_BOT_TOKEN'])
