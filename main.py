import asyncio

from tgbot.loader import bot
from tgbot.handlers import dp

from colorama import Fore, Style, init

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    init()

    print(f""" {Fore.RED + Style.BRIGHT}
    ██╗░░██╗██╗░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
    ╚██╗██╔╝██║░░░██║████╗░██║██║░░░██║╚██╗██╔╝
    ░╚███╔╝░╚██╗░██╔╝██╔██╗██║╚██╗░██╔╝░╚███╔╝░
    ░██╔██╗░░╚████╔╝░██║╚████║░╚████╔╝░░██╔██╗░
    ██╔╝╚██╗░░╚██╔╝░░██║░╚███║░░╚██╔╝░░██╔╝╚██╗
    ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝ {Fore.YELLOW}
    
    ░█████╗░░█████╗░██████╗░███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝
    ██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗
    ╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║ {Fore.RESET}

    Telegram: @VHVH00
    Topic: https://zelenka.guru/threads/5872770/ {Style.RESET_ALL}
    """)
    
    asyncio.run(main())