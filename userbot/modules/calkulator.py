#port by ilham mansiez
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP

chat = "@CalcuBot"


@register(outgoing=True, pattern="^.calkulator ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message("text")
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(conv.chat_id, [msg.id, response.id])
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message("text")
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(conv.chat_id, [msg.id, response.id])
CMD_HELP.update(
    {
        "kalkulator": ".calkulator\
    \nUntuk Membuat Bot Dari kalkulator, .calkulator  < contoh 2+2 >."
    })
