#PORT ILHAM
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP

chat = "@openmap_bot"


@register(outgoing=True, pattern="^.map ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("`Masukan Yang Benar Cok Biar Bisa Bikin Bot!!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("Medan")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(conv.chat_id, [msg.id, response.id])
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("Medan")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(conv.chat_id, [msg.id, response.id])


CMD_HELP.update(
    {
        "GoogleMap": ".map\
    \nUntuk Membuat Bot Dari GOOGLE MAP, .map  < nama kota/lokasi> "
    })
