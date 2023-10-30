import logging
import requests
import os 
from pyrogram import Client, filters

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your own values
api_id = "7565664"
api_hash = "a7a22b0f30b45dc64973ad11461325dc"

# Replace 'YOUR_BOT_TOKEN' with your Bot's API token
bot_token = "6122580053:AAGXTbIpRLp62ELc0VozRiz78crTgOhfo_A"
base_url = "https://consumet-api-nuuv.onrender.com/"
# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a handler for the /start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I'm your Telegram bot.")

# Define a handler for the /search command
@app.on_message(filters.command("search"))
def search(client, message):
    # Your code to fetch data from the API
    #url = "https://consumet-api-nuuv.onrender.com/anime/gogoanime/watch/spy-x-family-episode-1";
    path = "anime/gogoanime/watch/spy-x-family-episode-1"
    url = base_url + path
    response = requests.get(url, params={"server": "gogocdn"})
    data = response.json()
    
    # Send the API response as a message
    message.reply(str(data))

# Define a handler for incoming text messages
@app.on_message(filters.text)
def echo(client, message):
    message.reply(message.text)

if __name__ == "__main__":
    logger.info("Bot started!")
    port = int(os.environ.get("PORT", 8080))
    app.run(port=port)