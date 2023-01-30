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

import os

from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import app


@app.on_message(filters.command(["clearcache", "rmdownloads"]) & filters.user(OWNER_ID))
async def clear_misc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg *.png")
    await message.reply_text("» ᴀʟʟ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴄʟᴇᴀɴᴇᴅ.")
