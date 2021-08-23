from dotenv import dotenv_values
config = dotenv_values(".env")

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        if message.channel.id == int(config.get("CHANNEL_ID")):
            await message.add_reaction("⬆")
            await message.add_reaction("⬇")

client = MyClient()
client.run(config.get("TOKEN"))