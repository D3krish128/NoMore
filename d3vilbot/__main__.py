import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from d3vilbot import LOGS, bot, tbot
from d3vilbot.config import Config
from d3vilbot.utils import load_module
from d3vilbot.version import __d3vil__ as d3vilver
hl = Config.HANDLER
D3VIL_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"

# let's get the bot ready
async def d3vil_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"D3VILBOT_SESSION - {str(e)}")
        sys.exit()


# Userbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("ΰΌπππ°πππΈπ½πΆ πππ΄ππ±πΎπΰΌ")
            bot.loop.run_until_complete(d3vil_bot(Config.BOT_USERNAME))
            LOGS.info("β΅π³3ππΈπ»π±πΎπ πππ°ππππΏ π²πΎπΌπΏπ»π΄ππ΄π³β΅")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "d3vilbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/TEAM-D3VIL/D3VILADDONS"
 if Config.EXTRA == "True":
     try:
         os.system(f"git clone https://github.com/TEAM-D3VIL/D3VILADDONS")
     except BaseException:
         pass
     LOGS.info("Installing Extra Plugins")
     path = "d3vilbot/plugins/*.py"
     files = glob.glob(path)
      for name in files:
         with open(name) as ex:
             path2 = Path(ex.name)
             shortname = path2.stem
             load_module(shortname.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print ('INSTALLING ALL MODULES', plugin_name)
            except:
                pass

else:
  path = 'd3vilbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
      with open(name) as f:
          path1 = Path(f.name)
          shortname = path1.stem
          load_module(shortname.replace(".py", ""))




# let the party begin...
LOGS.info("βͺ πππ°πππΈπ½πΆ π±πΎπ πΌπΎπ³π΄")
tbot.start()
LOGS.info("ββββββββββββββββββββ")
LOGS.info(
    "π§πΎπΊπ½ ππ @D3VIL_SUPPORT πΏππ π΄ππΊπ½ππΎ π­πΎπ. π πππ ππππ πΌππΊπππΎπ to ππΎπ πππ½πΊππΎ ππΎππΊππ½πππ ππ π£3ππππ‘ππ."
)
LOGS.info("ββββββββββββββββββββ")

# that's life...
async def d3vil_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                D3VIL_PIC,
                caption=f"α΄α΄α΄Κα΄Κα΄α΄ α΄3α΄ ΙͺΚΚα΄α΄ sα΄α΄α΄α΄ss?α΄ΚΚΚ\n\n**ππ΄πππΈπΎπ½ βͺ {d3vilver}**\n\nππ²π©π `{hl}ping` or `{hl}alive` π­π¨ ππ‘πππ€! \n\nJoin [π‘3π³π¦π©π²π°π’π―ππ¬π±](t.me/D3VIL_SUPPORT) for Updates & [π3π³π¦π©π²π°π’π―ππ¬π± π π₯ππ±](t.me/D3VIL_BOT_SUPPORT) ππ¨π« ππ§π² πͺπ?ππ«π² π«ππ ππ«ππ’π§π  π‘3π³π¦π©ππ¬π±",
            )
    except Exception as e:
        LOGS.info(str(e))


    try:
        await bot(JoinChannelRequest("@D3VIL_SUPORT"))
    except BaseException:
        pass


bot.loop.create_task(d3vil_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()


