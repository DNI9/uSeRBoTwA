# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# Module for SHRP devices list by DNI9
#
#
""" Userbot module containing commands related to android"""

import re
from requests import get
from bs4 import BeautifulSoup

from userbot import CMD_HELP
from userbot.events import register

SHRP_DEVICES = 'https://raw.githubusercontent.com/DNI9/' \
    'uSeRBoTwA/botwa/userbot/modules/shrp_data.json'


@register(outgoing=True, pattern=r"^.shrp(?: |$)(\S*)")
async def device_info(request):
    if not request.text[0].isalpha()\
            and request.text[0] not in ("/", "#", "@", "!"):
        textx = await request.get_reply_message()
        device = request.pattern_match.group(1)
        if device:
            pass
        elif textx:
            device = textx.text
        else:
            await request.edit("`Usage: .shrp <codename>`")
            return
    found = [
        i for i in get(SHRP_DEVICES).json()
        if i["CodeName"] == device
    ]
    if found:
        reply = ''
        for item in found:
            name = item['Device']
            # brand = item['brand']
            codename = item['CodeName']
            shrp_version = item['shrp_ver']
            twrp_version = item['twrp_ver']
            maintainer = item['maintainer']
            build_date = item['Date']

            reply += f'**🦅 SkyHawk Recovery for {name} ({codename})** \n\n' \
                f'** SHRP Version:** `{shrp_version}`\n' \
                f'** TWRP Version:** `{twrp_version}`\n' \
                f'** Maintainer:** `{maintainer}`\n' \
                f'** Build Date:** `{build_date}`\n' \
                f'[Website | ](https://shrp.cf/)' \
                f'[Changelogs | ](https://telegra.ph/SHRP-Changelogs-08-21)' \
                f'[Download](https://sourceforge.net/projects/shrp/files/)'
    else:
        reply = f"`No Device Found !`\n"
    await request.edit(reply)


CMD_HELP.update({
    ".shrp <devices>": "For example .shrp c106"
})
