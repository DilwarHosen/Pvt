from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="❍ 𝐇𝙴𝙻𝙿 ❍", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="❍ 𝐒ҽƚƚιɳɠ𝐒❍", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐘ᴏᴜʀ 𝐇ᴇʟᴘᴇʀ ❍", callback_data="settings_back_helper"),
        ],
        [
             InlineKeyboardButton(
                text="❍ 𝐎ᴡɴᴇʀ ❍",
                url=f"https://t.me/AloneHuVai",
            ),
            InlineKeyboardButton(
                text="❍ 𝐀ʟʟ 𝐁ᴏᴛs ❍",
                url=f"https://t.me/AloneXBots",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝗙𝐑𝗜𝐄𝗡𝐃𝗦 𝗭𝐎𝗡𝐄🐝 ❍",
                url=f"https://t.me/+1iN6Tuz0-atmODI1",
            ),
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍✿︎ ᴀᴅᴅ ᴍᴇ ✿︎❍", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
                 
