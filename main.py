# Please don't touch the code if you don't know!
# All rights reserved to YonatanDEV - yonatanyh (915624756055801896)
import discord, os
from datetime import datetime
from discord import app_commands, utils, Webhook
from discord.ext import commands
import aiohttp
import asyncio
import json
import datetime
import time

with open('./config.json') as f:
  data = json.load(f)
  print("Welcome to Yonatan Bot! Checking the config.json")
  for c in data['botConfig']:
    os.system('color a')
    os.system('cls')
    if c['guildid'] == '0':
        os.system('color a')
        print("Make Sure the config is right!")
        time.sleep(1)
        print("Exiting...")
        time.sleep(2)
        exit()
    elif c['token'] == 'token':
        os.system('color a')
        print("Make Sure the config is right!")
        time.sleep(1)
        print("Exiting...")
        time.sleep(2)
        exit()
    elif c['blacklistchannel'] == '0':
        os.system('color a')
        print("Make Sure the config is right!")
        time.sleep(1)
        print("Exiting...")
        time.sleep(2)
        exit()
    else:
        print("Welcome to Yonatan Bot! Checking the config.json")
        time.sleep(2)
        os.system('cls')
        os.system('color b')
        print('Guild ID: ' + c['guildid'])
        print('Token: ' + c['token'])
        guild_id = c['guildid']
        token = c['token']
        blacklistchannel = c['blacklistchannel']
        blacklistmessageid = c['blacklistmessageid']






blacklistchn = int(blacklistchannel)
class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced = False
        self.added = False
        self.ticket_mod = 1

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=guild_id))
            self.synced = True
        if not self.added:
            self.added = True
        print(f"We have logged in as {self.user}.")
        print("Bot started!")
        channel = client.get_channel(blacklistchn)
        await start_blacklist_updates(channel)
        




client = aclient()
tree = app_commands.CommandTree(client)



def get_updated_embed():
    with open('blacklist.json', 'r') as f:
        blacklist = json.load(f)

    embed = discord.Embed(title="Blacklisted Users:")
    embed.set_author(name="Blacklist System by Yonatan")
    date = datetime.datetime.now()
    embed.set_footer(text=f'Last Update: {date:%d/%m/%y %H:%M}') 
    for user in blacklist:
        userid = user['user_id']
        embed.add_field(name=f"Discord ID: {userid}", value=f"**Discord Mention:** <@{userid}>\n**Reason:** " + user['reason'], inline=False)

    return embed


blacklistmsg = int(blacklistmessageid)
async def start_blacklist_updates(channel):
    message = await channel.fetch_message(blacklistmsg)
    while True:
        await message.edit(embed=get_updated_embed())
        await asyncio.sleep(10)

def add_to_blacklist(user_id, reason):
    with open('blacklist.json', 'r') as f:
        blacklist = json.load(f)

    blacklist.append({
        "user_id": user_id,
        "reason": reason
    })

    with open('blacklist.json', 'w') as f:
        json.dump(blacklist, f)


@tree.command(guild=discord.Object(id=guild_id), name='show_blacklist', description='Launches the blacklist system')
@app_commands.default_permissions(administrator=True)
async def show_blacklist(interaction: discord.Interaction):
    embed = get_updated_embed()
    await interaction.channel.send(embed=embed)

    await interaction.response.send_message("blacklist system launched!", ephemeral=True)

@tree.command(guild=discord.Object(id=guild_id), name='add_blacklist', description='add member to blacklist')
@app_commands.default_permissions(administrator=True)
async def add_blacklist(interaction: discord.Interaction, member: discord.Member, *, reason: str):
    add_to_blacklist(member.id, reason)
    await interaction.response.send_message(f"{member.name} has been added to the blacklist for the following reason: {reason}", ephemeral=True)

@tree.command(guild=discord.Object(id=guild_id), name='update_blacklist', description='developer tool')
@app_commands.default_permissions(administrator=True)
async def update_blacklist(interaction: discord.Interaction):
    get_updated_embed()
    await interaction.response.send_message(f"updated sir", ephemeral=True)




@tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        return await interaction.response.send_message(error, ephemeral=True)
    elif isinstance(error, app_commands.BotMissingPermissions):
        return await interaction.response.send_message(error, ephemeral=True)
    else:
        await interaction.response.send_message("An error occurred!", ephemeral=True)
        raise error


client.run(token)