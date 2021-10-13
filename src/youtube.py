import youtube_dl
import discord

YTDL_OPTIONS = {
	'format': 'bestaudio/best',
	'extractaudio': True,
	'audioformat': 'mp3',
	'outtmpl': './music/%(extractor)s-%(id)s-%(title)s.%(ext)s',
	'restrictfilenames': True,
	'noplaylist': True,
	'nocheckcertificate': True,
	'ignoreerrors': False,
	'logtostderr': False,
	'quiet': True,
	'no_warnings': True,
	'default_search': 'auto',
	# 'source_address': '0.0.0.0',
}

FFMPEG_OPTIONS = {
	'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
	'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

class YTDLSource(discord.PCMVolumeTransformer):
	def __init__(self, source, *, data, volume=0.5):
		super().__init__(source, volume)
		self.data = data
		self.title = data.get('title')
		self.url = ""

	@classmethod
	async def from_url(cls, url, *, loop=None, stream=False):
		loop = loop or asyncio.get_event_loop()
		data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
		if 'entries' in data:
			# take first item from a playlist
			data = data['entries'][0]
		filename = data['title'] if stream else ytdl.prepare_filename(data)
		return filename