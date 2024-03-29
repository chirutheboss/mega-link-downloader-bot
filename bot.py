import asyncio
from pyrogram import Client

# Import configuration based on environment variable
from sample_config import Config  # Adjust this import as per your actual configuration setup

async def start(app):
    print("Starting bot...")
    await app.start()
    print("Bot started.")

async def main():
    app = Client(
        "Mega_Link_Downloader_Bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
    )

    # Add your message handlers and other bot functionality here

    # Start the bot
    await start(app)

if __name__ == "__main__":
    asyncio.run(main())
