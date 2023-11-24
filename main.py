from telethon.sync import TelegramClient

from ably import AblyRealtime
import os


api_id = "22165656"
api_hash = "e7ffdb2615ba7651095641331679943f"
api_phone = os.getenv("api_phone") 
ably_token = os.getenv("ably_token") 
ably_chanel = os.getenv("ably_chanel") 
ably_publish = os.getenv("ably_publish") 
chat_1 = os.getenv("chat_1") 
chat_2 = os.getenv("chat_2") 
chat_3 = os.getenv("chat_3") 


from telethon import TelegramClient, events

print({"API_ID": api_id, "API_HASH": api_hash, "Chat 1": chat_1, "Chat 2": chat_2, "Chat 3": chat_3, "Ably Token": ably_token, "Ably Chanel": ably_chanel, "Ably Publish": ably_publish})
client = TelegramClient('anon', api_id, api_hash,phone=api_phone)
@client.on(events.NewMessage(chats = [chat_1, chat_2, chat_3]))
async def handler(event):
    print("Event Occured")
    print(event.raw_text)
    ably = AblyRealtime(ably_token)

    await ably.connection.once_async('connected')
    print('Connected to Ably')
    channel = ably.channels.get(ably_chanel)
    await channel.publish(ably_publish, event.raw_text)
    # asyncio.run(main())
client.start()
client.run_until_disconnected()