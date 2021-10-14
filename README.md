Python version -> 3.9.7

# Initiate project
1. Check version python `python --version`
	1. If you have 2.x then try using `python3 --version` and check if you have 3.9.x, then you have to use `python3` instead of `python` in the initialization of the project.
2. `git clone https://github.com/blitty-codes/ElPanadero.git`
3. Create an enviroment `python -m venv ElPanadero`
4. `cd ElPanadero`
5. `source ./bin/activate`
6. Install dependencies `pip install -r requirements.txt`
7. Create a `.env` file and add the env variables (an example down)
8. Run the bot `python main.py`

# Start bot
Start running the bot:
`nodemon main.py`
or
`python main.py`

# .env example
.env example:
```
DISCORD_BOT = <discord bot token>
DISCORD_GUILD = <discord server name>
```
