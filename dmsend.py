
# 봉순#4888 : MASS DM BOT SOURCE
# Made with Open Source


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Your Bot is working.")
    game = discord.Game('ℭ𝔞𝔯𝔱𝔢𝔩 ')
    await client.change_presence(status=discord.Status.online, activity=game)

#Send dm to "/dm {message}"
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 704558203136114711:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="ℭ𝔞𝔯𝔱𝔢𝔩 공지봇")
                        embed.add_field(name="필독", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/JZQqs2K")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzE3MTMzNDE4MTM5MjIyMDM3.XtV4oQ.MtLvNAiDecFLlLXRgs91mwYulac')
