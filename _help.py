# Oreo - UserBot


from telethon import Button

from . import vc_asst, asst, in_pattern


@vc_asst("vchelp")
async def helper(event):
    res = await event.client.inline_query(asst.me.username, "vchelp")
    try:
        await res[0].click(event.chat_id)
    except Exception as e:
        await event.eor(e)


@in_pattern("vchelp")
async def wiqhshd(e):
    builder = e.builder
    res = [
        await builder.article(
            title="Vc Help",
            text="**VCBot Help Menu**\n\n",
            buttons=Button.inline("Voice Chat Help", data="uh_VCBot_"),
        )
    ]
    await e.answer(res)
