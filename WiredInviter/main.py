from telethon import *
import modules.config 
from modules.adder import *
from colorama import *
from modules.banner import *
banner()
source = input(f"{Fore.LIGHTGREEN_EX}Insert Source Group Username > {Fore.RESET}")
target = input(f"{Fore.LIGHTGREEN_EX}Insert Target Group Username > {Fore.RESET}")
client = TelegramClient("TheWired", modules.config.API_ID, modules.config.API_HASH)
async def run(): 
    await client.start(modules.config.PHONE)
    await adder(client, source, target)
with client: 
   client.loop.run_until_complete(run())
