import discord
from discord.utils import get
from discord.ext.commands import Bot

from src.config import GUILD
from src.youtube import YTDLSource

bot = Bot(command_prefix='trigo?')
bot.remove_command('help')

voice = None

@bot.event
async def on_ready():
	guild = discord.utils.get(bot.guilds, name=GUILD)
	print(f'{bot.user.name} is connected to the following guild:\n{guild.name}(id: {guild.id})')

@bot.command(name='help')
async def help_command(ctx):
	embed = discord.Embed(title='Commands (trigo?<command>)', description='Commands the bot responds to', color=discord.Color.green())

	embed.add_field(name='g', value='Get gilds', inline=False)
	embed.add_field(name='join', value='Tells the bot to join the voice channel', inline=False)
	embed.add_field(name='play', value='Play a song', inline=False)
	embed.add_field(name='leave', value='To make the bot leave the voice channel', inline=False)
	embed.add_field(name='play_song', value='To play song', inline=False)
	embed.add_field(name='pause', value='This command pauses the song', inline=False)
	embed.add_field(name='resume', value='Resumes the song', inline=False)
	embed.add_field(name='stop', value='Stop a song', inline=False)

	await ctx.send(embed=embed)

@bot.command(name='g', help='Get guilds')
async def guilds(ctx):
	guilds = ''
	for guild in bot.guilds:
		guilds += f'{guild.name}\n'

	embed = discord.Embed(title="Guilds",
		description=guilds,
		color=discord.Color.blue())

	await ctx.send(embed=embed)

# music
@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
	try:
		if not ctx.message.author.voice:
			await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
		else:
			channel = ctx.message.author.voice.channel
			await channel.connect()
	except:
		await ctx.send("I am already connected to a voice channel")


@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
	try:
		voice_client = ctx.message.guild.voice_client
		await voice_client.disconnect(force=True)
	except:
		await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play', help='Play a song')
async def play(ctx, url):
	try:
		voice_channel = ctx.message.guild.voice_client

		filename = await YTDLSource.from_url(url, loop=bot.loop)
		voice_channel.play(discord.FFmpegPCMAudio(source=filename))
		await ctx.send('**Now playing:** {}'.format(filename.split('/')[2]))
	except:
		await ctx.send('Try to add the bot to the channel')

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_playing():
		voice_client.pause()
	else:
		await ctx.send("The bot is not playing anything at the moment.")

@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_paused():
		voice_client.resume()
	else:
		await ctx.send("The bot was not playing anything before this. Use play <yt_url> command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
	voice_client = ctx.message.guild.voice_client
	if voice_client.is_playing():
		voice_client.stop()
	else:
		await ctx.send("The bot is not playing anything at the moment.")
