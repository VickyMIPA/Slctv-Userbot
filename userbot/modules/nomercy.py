from time import sleep
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern='^.nomercy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Fajar Peler☑️**")
    await typew.edit("**Fajar Peler✅**")
    sleep(1)
    await typew.edit("**Tebe Gilaa☑️**")
    await typew.edit("**Tebe Gilaa✅**")
    sleep(2)
    await typew.edit("**Popoy Depresi☑️**")
    await typew.edit("**Popoy Depresi✅**")
    sleep(2)
    await typew.edit("**Timeh Gajelas☑️**")
    await typew.edit("**Timeh Gajelas✅**")
    sleep(2)
    await typew.edit("**Aca GJM!☑️**")
    await typew.edit("**Aca GJM!✅**")
    sleep(2)
    await typew.edit("**Dare GJB!☑️**")
    await typew.edit("**Dare GJB!✅**")
    sleep(2)
    await typew.edit("**Vio,MengRibet☑️**")
    await typew.edit("**Vio,MengRibet✅**")
    sleep(2)
    await typew.edit("**Jeje,Mengintil☑️**")
    await typew.edit("**Jeje,Mengintil✅**")
    sleep(2)
    await typew.edit("**Sins,Sijelek☑️**")
    await typew.edit("**Sins,Sijelek✅**")
    sleep(2)
    await typew.edit("**Lexi,Sidongo☑️**")
    await typew.edit("**Lexi,Sidongo✅**")
    sleep(2)
    await typew.edit("**Ulum,Sikontol☑️**")
    await typew.edit("**Ulum,Sikontol✅**")
    sleep(2)
    await typew.edit("**Vicky,Kyutt☑️**")
    await typew.edit("**Vicky,Kyutt✅**")
    sleep(3)
    await typew.edit("**CUMA VICKY YANG BENER!😁**")

CMD_HELP.update({
    "nomercy":
    "`.nomercy`\
    \n\n`.nomercy` 
})

