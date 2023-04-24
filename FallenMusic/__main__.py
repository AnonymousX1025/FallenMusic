# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import importlib
import os

from pyrogram import idle

from FallenMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from FallenMusic.Modules import ALL_MODULES


async def fallen_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            SUNAME,
            f"✯ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ✯\n\n𖢵 ɪᴅ : `{5853751357}`\n𖢵 ɴᴀᴍᴇ : {xᴏxᴏ ☊ ᴍᴜsɪᴄ}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{XoXo_MuSicBoT}",
        )
    except:
        LOGGER.error(
            f"{xᴏxᴏ ☊ ᴍᴜsɪᴄ} failed to send message at @{XoXo_MuSicBoT}, please go & check."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"✯ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : `{5827163072}`\n𖢵 ɴᴀᴍᴇ : {❛✘❍✘❍❟ ☊ ❛𝘼𝙎𝙎𝙞𝙎𝙏𝘼𝙉𝙏❟}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{L2F_XOXO_MUSIC}",
        )
    except:
        LOGGER.error(
            f"{❛✘❍✘❍❟ ☊ ❛𝘼𝙎𝙎𝙞𝙎𝙏𝘼𝙉𝙏❟} failed to send message at @{L2F_XOXO_MUSIC}, please go & check."
        )

    await app2.send_message(XoXo_MuSicBoT, "/start")

    LOGGER.info(f"[•] Bot Started As {xᴏxᴏ ☊ ᴍᴜsɪᴄ}.")
    LOGGER.info(f"[•] Assistant Started As {❛✘❍✘❍❟ ☊ ❛𝘼𝙎𝙎𝙞𝙎𝙏𝘼𝙉𝙏❟}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fallen_startup())
    LOGGER.error("Fallen Music Bot Stopped.")
