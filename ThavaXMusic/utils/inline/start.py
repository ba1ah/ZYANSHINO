from pyrogram.types import InlineKeyboardButton

import config
from ThavaXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋 ᴀᴅᴅ ᴍᴇ 🤍",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="🦋 ʜᴇʟᴘ 🤍", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🦋 ɴᴇᴛᴡᴏʀᴋ 🤍", url=f"https://t.me/Team_Hypers_Networks),
            InlineKeyboardButton(text="🦋 ᴜᴘᴅᴀᴛᴇ 🤍", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="🦋 ᴏᴡɴᴇʀ 🤍", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="🦋 sᴏᴜʟ 🤍", url=f"https://t.me/king_0f_izzy"),
        ],
    ]
    return buttons
