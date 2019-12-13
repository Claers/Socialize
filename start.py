"""The start file for the application
"""
import server
import bot
import multiprocessing

if __name__ == "__main__":
    server_p = multiprocessing.Process(target=server.launch)
    bot_p = multiprocessing.Process(target=bot.launch)
    server_p.start()
    bot_p.start()
    