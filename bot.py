import os
from pyrogram import Client

# Import configuration based on environment variable
from sample_config import Config  # Adjust this import as per your actual configuration setup

if __name__ == "__main__":
    # Your configuration setup code here
    
    async def start():
        print("Starting bot...")
        await app.start()
        await app.stop()
        await app.start()
        print("Bot started.")

    app = Client(
        "Mega_Link_Downloader_Bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
    )

    app.on_startup(start)

    app.run()
    app.idle()
