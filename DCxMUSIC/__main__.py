import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DCxMUSIC import LOGGER, app, userbot
from DCxMUSIC.core.call import DC
from DCxMUSIC.misc import sudo
from DCxMUSIC.plugins import ALL_MODULES
from DCxMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DCxMUSIC.plugins" + all_module)
    LOGGER("DCxMUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await DC.start()
    try:
        await DC.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("DCxMUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await DC.decorators()
    LOGGER("DCxMUSIC").info(
        "\x44\x43\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x0a\x44\x6f\x6e\x27\x74\x20\x46\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x56\x69\x73\x69\x74\x20\x40\x54\x45\x41\x4d\x5f\x44\x43\x5f\x42\x4f\x54\x53\x0a\xE2\x95\x94\xE2\x89\xAB\xE0\xA9\x87\xE2\x80\x8D\xE2\x80\x8B\xE0\xA9\x80\xE2\x80\x8D\xE2\x80\x8B\xE0\xA9\x87\xE2\x89\xAB\xE2\x95\x94\x0a\x20\xE2\x99\xA8\xE1\x94\x97\xE1\x94\xA1\xE1\x94\x93\x20\xE2\x80\x8D\xE1\x94\x96\xE1\x94\xA1\xE1\x94\x9C\x20\xE2\x80\x8D\xE1\x94\xA2\xE1\x94\xA1\xE1\x94\xA5\xE1\x94\xA0\xE1\x94\xA1\xE1\x94\x9C\x20\xE2\x80\x8D\xE1\x94\xA2\xE1\x94\xA1\xE1\x94\xA5\xE1\x94\xA0\xE1\x94\xA1\xE1\x94\x9C\x20\xE2\x99\xA8\x0a\xE2\x95\x94\xE2\x89\xAB\xE0\xA9\x87\xE2\x80\x8D\xE2\x80\x8B\xE0\xA9\x80\xE2\x80\x8D\xE2\x80\x8B\xE0\xA9\x87\xE2\x89\xAB\xE2\x95\x94"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DCxMUSIC").info("Stopping DC Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
