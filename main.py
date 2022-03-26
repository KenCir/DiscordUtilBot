import os
from os.path import join, dirname
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

allowed_mentions = discord.AllowedMentions(roles=False, everyone=False, users=False)
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', description="Ken_CirのDiscordUtilBot", intents=intents,
                   allowed_mentions=allowed_mentions)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command(name='rename',description='チャンネル名を変更する')
async def rename(ctx: commands.Context, new_channel_name: str):
    await ctx.channel.edit(name=new_channel_name)
    await ctx.send(f"チャンネル名を**{new_channel_name}**に変更しました")


@bot.command(name='purge', description='メッセージを一括削除')
async def purge(ctx: commands.Context, purge_count: int = 1):
    await ctx.channel.purge(limit=purge_count)
    await ctx.send(f"Delete {purge_count} Messages")


bot.run(os.environ.get("DISCORD_TOKEN"))
