from asyncio import sleep
from pyrogram import Client, filters
import random 
api_id = 11469052
api_hash = "85f96e9fa567f3ae49379b1e67c547a2"
app = Client("account",api_id,api_hash)
@app.on_message()
def avtootvet(client,message):
    if message.chat.id == -1001353006927 and message.text.lower() == "шипперим":
        a = app.get_chat_members(message.chat.id)
        d = {}
        for i in a:
            if not i.user.is_bot:
                d[str(i.user.id)] = f"{i.user.first_name}" 
        rand = random.choice(list(d.keys()))
        rand2 = random.choice(list(d.keys()))
        app.send_message(-1001353006927, f"💞 РАНДОМ ШИППЕРИМ: <a href='tg://openmessage?user_id={int(rand)}'>{d.get(rand)}</a> + <a href='tg://openmessage?user_id={int(rand2)}'>{d.get(rand2)}</a>. Любите друг друга и берегите. Мур.", parse_mode="html")
app.run()