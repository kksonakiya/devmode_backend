from telethon import TelegramClient, events
from telethon.sessions import StringSession
import nest_asyncio
import asyncio, os
from dotenv import load_dotenv
from dateutil import tz
load_dotenv()

api_id = os.getenv("TELEGRAM_API")
api_hash = os.getenv("TELEGRAM_HASH")
session_string = os.getenv("TELEGRAM_SESSION_STRING")
contact_id = os.getenv("TELEGRAM_CONTACT_ID")

from_zone = tz.gettz("UTC")
to_zone = tz.gettz("Asia/Kolkata")
nest_asyncio.apply()
try:
    # client.disconnect()

    async def main(recipient, group_id, msg):
        client = TelegramClient(StringSession(session_string), api_id, api_hash)
        # client= TelegramClient(
        #     'myapp',
        #     api_id=,
        #     api_hash=,
        # )
        await client.connect()
        if msg:
            if recipient:
                contact = await client.get_entity(f"+91{recipient}")

                await client.send_message(int(contact.id), msg)
            if group_id:
                get_group = await client.get_entity(group_id)
                print(get_group.id, get_group.title)
                await client.send_message(int(group_id), msg)
        await client.disconnect()

    def sendmsg(recipient=None, group_id=None, msg=None):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("Sending msg!")
        asyncio.run(main(recipient, group_id, msg))

        print("Msg Sent!")

    async def getMessages_chatid(msg_count):
        client = TelegramClient(StringSession(session_string), api_id, api_hash)
        await client.connect()
        msgs = await client.get_messages(contact_id, msg_count)
        print(msgs[0])
        msg_data = []
        for msg in msgs:
            utc_zone = msg.date.replace(tzinfo=from_zone)
            utc_to_ist = utc_zone.astimezone(to_zone)
            msg_date = utc_to_ist.strftime(("%d/%m/%Y, %I:%M:%S %p"))
            from_id=msg.from_id
            if from_id:
                from_id = from_id.user_id
            else:
                from_id='None'
#             print(
#                 f"""Peer ID: {msg.peer_id}


# From ID: {msg.from_id}
# Message: {msg.message}
# Date: {msg_date}

#             """
#             )
            msg_data.append(
                dict(
                    message_id=msg.id,
                    peer_id=msg.peer_id.user_id,
                    from_id=from_id,
                    message=msg.message,
                    date=msg.date,
                )
            )
        return msg_data

    def getMessages():
        loop = asyncio.new_event_loop()

        asyncio.set_event_loop(loop)
        asyncio.run(getMessages_chatid())

except Exception as e:
    print(e)
