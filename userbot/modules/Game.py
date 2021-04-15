#port by ilham mansiez
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP

chat = "@gamee"


@register(outgoing=True, pattern="^.ninjagame ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("play grafit ninja 2")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("play grafit ninja 2")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(conv.chat_id, [msg.id, response.id])

@register(outgoing=True, pattern="^.racergame ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("Play - F1 Racer")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("Play - F1 Racer")
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(conv.chat_id, [msg.id, response.id])


CMD_HELP.update(
    {
        "Kalkulator": ".ninjagame\
    \nUntuk Membuat Bot Dari Game, .ninjagame "
    })
