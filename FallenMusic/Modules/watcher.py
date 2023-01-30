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

from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio, Update

from FallenMusic import BOT_ID, BOT_USERNAME, app, app2, fallendb, pytgcalls
from FallenMusic.Helpers import _clear_, buttons, gen_thumb

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    try:
        await _clear_(message.chat.id)
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass


@app.on_message(filters.left_chat_member)
async def ub_leave(_, message: Message):
    if message.left_chat_member.id == BOT_ID:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
        except:
            pass
        try:
            await app2.leave_chat(message.chat.id)
        except:
            pass


@pytgcalls.on_left()
@pytgcalls.on_kicked()
@pytgcalls.on_closed_voice_chat()
async def swr_handler(_, chat_id: int):
    try:
        await _clear_(chat_id)
    except:
        pass


@pytgcalls.on_stream_end()
async def on_stream_end(pytgcalls, update: Update):
    chat_id = update.chat_id

    get = fallendb.get(chat_id)
    if not get:
        try:
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)
        except:
            return
    else:
        process = await app.send_message(
            chat_id=chat_id,
            text="» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɴᴇxᴛ ᴛʀᴀᴄᴋ ғʀᴏᴍ ᴏ̨ᴜᴇᴜᴇ...",
        )
        title = get[0]["title"]
        duration = get[0]["duration"]
        file_path = get[0]["file_path"]
        videoid = get[0]["videoid"]
        req_by = get[0]["req"]
        user_id = get[0]["user_id"]
        get.pop(0)

        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())

        try:
            await pytgcalls.change_stream(
                chat_id,
                stream,
            )
        except:
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)

        img = await gen_thumb(videoid, user_id)
        await process.delete()
        await app.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=f"**➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ**\n\n‣ **ᴛɪᴛʟᴇ :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n‣ **ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` ᴍɪɴᴜᴛᴇs\n‣ **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {req_by}",
            reply_markup=buttons,
        )
