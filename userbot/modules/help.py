# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(petercord):
    """ For .help command,"""
    args = petercord.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await petercord.edit(str(CMD_HELP[args]))
        else:
            await petercord.edit("**Maaf Petercord, Saya Tidak Punya Perintah Itu :)**")
            await asyncio.sleep(200)
            await petercord.delete()
    else:
        await petercord.edit("DAFTAR PERINTAH PETERCORD SIMBOL 15 NEGARA")
        await petercord.edit("**💥 BAGIAN 1:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇮🇩`gamepetercord`🇮🇩`petercordkata-kata`🇮🇩`petercorddmisc`🇮🇩`petercordoff`🇮🇩`vip`🇮🇩`animasi`🇮🇩`android`🇮🇩`anime`🇮🇩`anti_spambot`🇮🇩`aria`🇮🇩`ascii`🇮🇩\n\n***╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 2:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇯🇵`blacklist`🇯🇵`carbon`🇯🇵`chat`🇯🇵`mutechat`🇯🇵`covid`🇯🇵`membuat`🇯🇵`deepfry`🇯🇵`emojigames`🇯🇵\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 3:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇮🇷`eval`🇮🇷`exec`🇮🇷`term`🇮🇷`frog`🇮🇷`federations`🇮🇷`figlet`🇮🇷`filter`🇮🇷`gban`🇮🇷`gcast`🇮🇷`gdrive`🇮🇷`gcommit`🇮🇷`github`🇮🇷\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 4:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇰🇷`glitch`🇰🇷`gps`🇰🇷`hash`🇰🇷`base64`🇰🇷`hentai`🇰🇷`heroku`🇰🇷`id`🇰🇷`imgmeme`🇰🇷`kekuatan`🇰🇷\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 5:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n`🇮🇱lastfm`🇮🇱`locks`🇮🇱`petercordmintabantuan`🇮🇱`aeshtetic`🇮🇱`petercorddeteksi`🇮🇱`chatperintah`🇮🇱`petercordphreaker`🇮🇱`hazmat`🇮🇱\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 6:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇱🇷`botfather`🇱🇷`amongus`🇱🇷`mengubahfontteks`🇱🇷`misc`🇱🇷`app`🇱🇷`link instagram`🇱🇷`grab`🇱🇷`clone`🇱🇷\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 7:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇳🇿`randomprofil`🇳🇿`petercordmusic`🇳🇿`tiny`🇳🇿`tempmail`🇳🇿`tiktok`🇳🇿`wordcloud`🇳🇿\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 8:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇶🇦`lyrics`🇶🇦`mega`🇶🇦`memes`🇶🇦`memify`🇶🇦`mentions`🇶🇦`purge`🇶🇦`purgeme`🇶🇦`del`🇶🇦`edit`🇶🇦\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 9:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇸🇦`sd`🇸🇦`random`🇸🇦`sleep`🇸🇦`shutdown`🇸🇦`repo`🇸🇦`readme`🇸🇦`repeat`🇸🇦`restart`🇸🇦\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 10:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇷🇺`raw`🇷🇺`nekobot`🇷🇺`notes`🇷🇺`petercord`🇷🇺`petercordfun`🇷🇺`pm`🇷🇺`profil`🇷🇺`quotly`🇷🇺`rastick`🇷🇺`resi`🇷🇺`reverse`🇷🇺`salam`🇷🇺`sangmata`🇷🇺\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 11:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇹🇷`santetonline`🇹🇷`image_search`🇹🇷`currency`🇹🇷`google`🇹🇷`wiki`🇹🇷`ud`🇹🇷`tts`🇹🇷`translate`🇹🇷`youtube`🇹🇷`rip`🇹🇷\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 12:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇬🇧`removebg`🇬🇧`ocr`🇬🇧`qrcode`🇬🇧`barcode`🇬🇧`paste`🇬🇧`getpaste`🇬🇧`nekobin`🇬🇧`direct`🇬🇧`screenshot`🇬🇧`sed`🇬🇧`snips`🇬🇧`spam`🇬🇧`spotifynow`🇬🇧`ssvideo`🇬🇧\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 13:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇩🇪`stickers`🇩🇪`stickers2`🇩🇪`sysd`🇩🇪`botver`🇩🇪`pip`🇩🇪`alive`🇩🇪`tag_all`🇩🇪`telegraph`🇩🇪`timedate`🇩🇪`torrent`🇩🇪\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 14:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇹🇯`transform`🇹🇯`update`🇹🇯`download`🇹🇯`getid`🇹🇯`waifu`🇹🇯`wallpaper`🇹🇯`weather`🇹🇯\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n"
                             "**💥 BAGIAN 15:**\n"
                             "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n🇸🇬`webupload`🇸🇬`welcome`🇸🇬`whois`🇸🇬`ping`🇸🇬`sinyal`🇸🇬`xiaomi`🇸🇬`zipfile`🇸🇬`penghapusankk`🇸🇬**╰┄┅┷┅┄┄┅┷┅┄╯**\n")
        await petercord.reply("\n**CARA MEMAKAINYA,** **CONTOH:**\n**KETIK** `.help petercordoff` **UNTUK INFORMASI MODULES**\n**GROUP SUPPORT:** [PETERCORD-USERBOT](@petercord)")
        await asyncio.sleep(1000)
        await petercord.delete()
