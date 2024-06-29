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
import os

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, UnMuteNeeded
from pytgcalls.types import AudioPiped, HighQualityAudio
from youtube_search import YoutubeSearch

from config import DURATION_LIMIT
from FallenMusic import (
    ASS_ID,
    ASS_MENTION,
    ASS_NAME,
    ASS_USERNAME,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    app,
    app2,
    fallendb,
    pytgcalls,
)
from FallenMusic.Helpers.active import add_active_chat, is_active_chat, stream_on
from FallenMusic.Helpers.downloaders import audio_dl
from FallenMusic.Helpers.errors import DurationLimitError
from FallenMusic.Helpers.gets import get_file_name, get_url
from FallenMusic.Helpers.inline import buttons
from FallenMusic.Helpers.queue import put
from FallenMusic.Helpers.thumbnails import gen_qthumb, gen_thumb


@app.on_message(
    filters.command(["play", "vplay", "oynat"])
    & filters.group
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    fallen = await message.reply_text("» Lütfen bekleyin...")
    try:
        await message.delete()
    except:
        pass

    try:
        try:
            get = await app.get_chat_member(message.chat.id, ASS_ID)
        except ChatAdminRequired:
            return await fallen.edit_text(
                f"» Kullanıcıları davet etmek için bağlantı iznim yok {BOT_NAME} asistani davet edin{message.chat.title}."
            )
        if get.status == ChatMemberStatus.BANNED:
            unban_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"ᴜɴʙᴀɴ {ASS_NAME}",
                            callback_data=f"unban_assistant {message.chat.id}|{ASS_ID}",
                        ),
                    ]
                ]
            )
            return await fallen.edit_text(
                text=f"» {BOT_NAME} asistan ban yemiş kiral {message.chat.title}\n\n𖢵 id : `{ASS_ID}`\n𖢵 isim : {ASS_MENTION}\n𖢵 kullanıcı adı: @{ASS_USERNAME}\n\nLütfen asistan banını kaldırın...",
                reply_markup=unban_butt,
            )
    except UserNotParticipant:
        if message.chat.username:
            invitelink = message.chat.username
            try:
                await app2.resolve_peer(invitelink)
            except Exception as ex:
                LOGGER.error(ex)
        else:
            try:
                invitelink = await app.export_chat_invite_link(message.chat.id)
            except ChatAdminRequired:
                return await fallen.edit_text(
                    f"» kullanıcıları davet etmek için bağlantı iznim yok {BOT_NAME} asistani davet edin{message.chat.title}."
                )
            except Exception as ex:
                return await fallen.edit_text(
                    f"Davet ederken hata oluştu {BOT_NAME} asistani davet edin{message.chat.title}.\n\n**sebep :** `{ex}`"
                )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        anon = await fallen.edit_text(
            f"Lütfen bekleyin...\n\nDavet {ASS_NAME} ᴛᴏ {message.chat.title}."
        )
        try:
            await app2.join_chat(invitelink)
            await asyncio.sleep(2)
            await fallen.edit_text(
                f"{ASS_NAME} Bot başarıyla giriş yaptı,\n\nYayın başlıyor..."
            )
        except UserAlreadyParticipant:
            pass
        except Exception as ex:
            return await fallen.edit_text(
                f"Davet ederken hata oluştu {BOT_NAME} asistanı davrt edin {message.chat.title}.\n\n**Sebep :** `{ex}`"
            )
        try:
            await app2.resolve_peer(invitelink)
        except:
            pass

    ruser = message.from_user.first_name
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"» Üzgünüm bebeğim, parça çok uzun süre  {DURATION_LIMIT} Dakikalar oynamak için izin verilmiyor {BOT_NAME}."
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        file_path = (
            await message.reply_to_message.download(file_name)
            if not os.path.isfile(os.path.join("downloads", file_name))
            else f"downloads/{file_name}"
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            title = results[0]["title"]
            duration = results[0]["duration"]
            videoid = results[0]["id"]

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            return await fallen.edit_text(f"birşeyler yanlış gitti\n\n**Hata :** `{e}`")

        if (dur / 60) > DURATION_LIMIT:
            return await fallen.edit_text(
                f"» Üzgünüm bebeğim, parça çok uzun süre  {DURATION_LIMIT} Dakika max 60 dakika {BOT_NAME}."
            )
        file_path = audio_dl(url)
    else:
        if len(message.command) < 2:
            return await fallen.edit_text("» Hangi şarkıyı oynatmak istiyorsun ?")
        await fallen.edit_text("🔎")
        query = message.text.split(None, 1)[1]
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            videoid = results[0]["id"]
            duration = results[0]["duration"]

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            LOGGER.error(str(e))
            return await fallen.edit("» Sorgu işlenemedi, tekrar dene...")

        if (dur / 60) > DURATION_LIMIT:
            return await fallen.edit(
                f"» üzgünüm bebeğim parça çok uzun süre  {DURATION_LIMIT} max dakika 60 dakika {BOT_NAME}."
            )
        file_path = audio_dl(url)

    try:
        videoid = videoid
    except:
        videoid = "fuckitstgaudio"
    if await is_active_chat(message.chat.id):
        await put(
            message.chat.id,
            title,
            duration,
            videoid,
            file_path,
            ruser,
            message.from_user.id,
        )
        position = len(fallendb.get(message.chat.id))
        qimg = await gen_qthumb(videoid, message.from_user.id)
        await message.reply_photo(
            photo=qimg,
            caption=f"**➻ Sıraya Eklendi {position}**\n\n‣ **Başlık :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n‣ **Süre :** `{duration}` Dakika\n‣ **Tarafından :** {ruser}",
            reply_markup=buttons,
        )
    else:
        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.join_group_call(
                message.chat.id,
                stream,
                stream_type=StreamType().pulse_stream,
            )

        except NoActiveGroupCall:
            return await fallen.edit_text(
                "**» Aktif sesli yok.**\n\nLütfen sesli açıp tekrar deneyin."
            )
        except TelegramServerError:
            return await fallen.edit_text(
                "» Telegram içsel bazı sorunlar yaşıyor, lütfen sesli sohbeti yeniden başlatın ve tekrar deneyin."
            )
        except UnMuteNeeded:
            return await fallen.edit_text(
                f"» {BOT_NAME} Asistan Sesli Sohbette Muteli,\n\nLütfen mutesini açın {ASS_MENTION} Sesli sohbeti kapatık tekrardan müzik açmayı deneyin."
            )

        imgt = await gen_thumb(videoid, message.from_user.id)
        await stream_on(message.chat.id)
        await add_active_chat(message.chat.id)
        await message.reply_photo(
            photo=imgt,
            caption = f"**➻ Yayın Başladı**\n\n" \
          f"‣ **Başlık :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n" \
          f"‣ **Süre :** `{duration}` Dakika\n" \
          f"‣ **Yayıncı :** {ruser}",
            reply_markup=buttons,
        )

    return await fallen.delete()
