#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ุงููููู ูุชุนููุจ ุนููู ุชุฎููุท ุงุฐูุฑ ุงููุตูุฏุฑ
#ุชุนูุฏูู ุจูููุชู ๐

import os
import random
from asyncio import sleep

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from zthon import zedub
from zthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from . import *
from . import mention

plugin_category = "ุงูุนุฑูุถ"
LOGS = logging.getLogger(__name__)

sts_animal = "https://telegra.ph/file/720a8d292301289bb7ca4.mp4"#ูุทู
sts_animal2 = "https://telegra.ph/file/fa43723297d16ebccfa94.mp4" #ููุจ
sts_animal3 = "https://telegra.ph/file/bc4c35ca805ab9e4ef8d7.mp4"#ูุฑุฏ
sts_animal4 = "https://telegra.ph/file/7cc42816b3e161f7183b6.mp4"#ุตุฎู
sts_animal5 = "https://telegra.ph/file/8beaf555e0d4e3f00c294.mp4"#ุทูู
sts_animal6 = "https://telegra.ph/file/c34cb870037a4ed2be972.mp4"#ุจุฒูู
sts_animal7 = "https://telegra.ph/file/c499feb6a51dea16a1fe5.mp4"#ุงุจู ุจุฑูุต
sts_animal8 = "https://telegra.ph/file/19b193f06d680e3ec79c0.mp4"#ุฌุฑูุฐู
sts_animal9 = "https://telegra.ph/file/cd1fcb86af78d83ba9002.mp4"#ูุงูุดู

jjj = [
    "100% ูู ุญููุงู ุบูุจูู ๐ฑ๐.",
    "90% ูู ุญููุงู ุถูู ๐ฑ๐๐",
    "80%  ูด๐ฑ๐",
    "70%  ูด๐ฑ๐",
    "60% ุจุฑุงุณู 60 ุญุธ ๐๐",
    "50% ุญููุงู ูุฌูู๐๐",
    "( 40% ) ุฎูุด ุญููุงู ๐๐",
    "30% ูด๐๐",
    "20% ูด๐๐",
    "10% ูด๐๐",
    "0% ูด๐ข๐",
]


ZEED_IMG = sts_animal or sts_animal2 or sts_animal3 or sts_animal4 or sts_animal5 or sts_animal6 or sts_animal7 or sts_animal8 or sts_animal9


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "ุงูุญููุงู ูุงูุฎูู ุจุฑููุงูู"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    last_name = replied_user.last_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    yoy = random.choice(jjj)
    ZEED_IMG
    x = random.randrange(1, 9)
    if x == 1:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ูุทู ุฒุฑุจู ๐ฆ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal, caption
    if x == 2:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ุฌูุจ ุดูุงุฑุน ๐โ๐ฆบ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal2, caption
    if x == 3:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ูุฑุฏ ูุฒููู ๐ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal3, caption
    if x == 4:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ุตุฎู ูุญุชุฑู ๐ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal4, caption
    if x == 5:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ุทูู ุงุจู ุงูุจุนุฑูุฑ ุงููุตุฎ ๐ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal5, caption
    if x == 6:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ุจุฒูู ุงุจูุฎุงูุฏ ๐ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal6, caption
    if x == 7:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ุงูุฒุงุญู ุงุจู ุจุฑูุต ๐ฆ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal7, caption
    if x == 8:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ุฌุฑูุฐู ุงุจู ุงููุฌุงุฑู ๐ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal8, caption
    if x == 9:
       username = "@{}".format(username) if username else ("ูุงููุฌุฏ ูุนุฑู")
       caption = f"<b>  โฎโข๐ฆฆ ุงูุญููุงู โฆ </b> {first_name} {last_name} \n"
       caption += f"<b> ูดโผโโโโโโโโโโโโโโโโโโโพ </b>\n"
       caption += f"<b> โข ๐ | ูุนูุฑูู  โฆ </b> {username}\n"
       caption += f"<b> โข ๐ | ุงููุฏูู   โฆ </b> <code>{user_id}</code>\n"
       caption += f"<b> โข ๐ | ุตููุฑู  โฆ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> โข ๐ | ููููุนู   โฆ  ูุงูุดู ๐ </b>\n"
       caption += f"<b> โข ๐ | ูุณุจุชูู  โฆ  {yoy} </b>\n\n\n"
       caption += f"<b> ๐ฉ ๐๐๐๐๐พ๐ ๐๐๐ฟ ๐ช </b> - @ZedThon "
       return sts_animal9, caption


@zedub.zed_cmd(pattern="ุญููุงู(?: |$)(.*)")
async def who(event):
    zed = await edit_or_reply(event, "โ")
    zel_dev = ()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        ZEED_IMG, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(zed, "**- ููู ุงุณุชุทูุน ุงูุนุซูููุฑ ุน ุงูุดุฎููุต**")
    if replied_user.id in zel_dev:
       return await edit_or_reply(zed, "**- ุฏู . . ุงูููู ุงุญูุฏ ุงููุทููุฑูู . . ุงูุชูู ุงูุญูููุงู ููู**")
    if replied_user.id == 5970563361 or replied_user.id == 5093806483 or replied_user.id == 5811133066 or replied_user.id == 1096229060:
       return await edit_or_reply(zed, "**- ุฏู . . ุงูููู ุงููุทููุฑ . . ุงูุชูู ุงูุญูููุงู ููู**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            ZEED_IMG,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        await zed.delete()
    except TypeError:
        await zed.edit(caption, parse_mode="html")

