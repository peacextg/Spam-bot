# © @ll_ALPHA_BABY_lll
import asyncio
from random import choice
from telethon import events, functions, types
from RAUSHAN.data import GROUP, PORMS
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl

# Import ALTRON from the data file
try:
    from RAUSHAN.data import ALTRON
except ImportError:
    ALTRON = []

# Protection check function (matching the raid module)
async def is_protected(user_id):
    if user_id in ALTRON:
        return True, "ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ."
    elif user_id == OWNER_ID:
        return True, "ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ."
    elif user_id in SUDO_USERS:
        return True, "ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ."
    return False, None

# Enhanced GIF spam function
async def gifspam(client, event, media_msg):
    try:
        if hasattr(media_msg, 'media') and hasattr(media_msg.media, 'document'):
            await client(
                functions.messages.SaveGifRequest(
                    id=types.InputDocument(
                        id=media_msg.media.document.id,
                        access_hash=media_msg.media.document.access_hash,
                        file_reference=media_msg.media.document.file_reference,
                    ),
                    unsave=True,
                )
            )
    except Exception as e:
        print(f"GIF spam error: {e}")

# Ultra rapid spam function with 10x speed
async def perform_spam(client, chat_id, message, count, reply_to=None, is_media=False, media_msg=None):
    """Perform spam with 10x speed (0.01s delay)"""
    for _ in range(count):
        try:
            if is_media and media_msg:
                sent = await client.send_file(chat_id, media_msg, caption=message if message else None)
                await gifspam(client, event, sent)
            else:
                if reply_to:
                    await client.send_message(chat_id, message, reply_to=reply_to)
                else:
                    await client.send_message(chat_id, message)
            await asyncio.sleep(0.01)  # 10x faster than original (0.1s)
        except Exception as e:
            print(f"Spam error: {e}")
            break


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(event):
    if event.sender_id not in SUDO_USERS:
        return
    
    altron = event.text.split(" ", 2)
    mk = await event.get_reply_message()

    try:
        # Check if replying to a protected user
        if mk and mk.sender_id:
            protected, msg = await is_protected(mk.sender_id)
            if protected:
                await event.reply(msg)
                return

        if len(altron) >= 3:
            count = int(altron[1])
            if count <= 0:
                await event.reply("❌ Count must be greater than 0!")
                return
                
            message = altron[2]
            if event.reply_to_msg_id:
                # 10x faster spam with reply
                for _ in range(count):
                    await event.client.send_message(event.chat_id, message, reply_to=event.reply_to_msg_id)
                    await asyncio.sleep(0.01)  # 10x faster
            else:
                # 10x faster spam without reply
                for _ in range(count):
                    await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(0.01)  # 10x faster
                
        elif event.reply_to_msg_id and mk.media:
            count = int(altron[1]) if len(altron) > 1 else 5
            if count <= 0:
                await event.reply("❌ Count must be greater than 0!")
                return
                
            # 10x faster media spam
            for _ in range(count):
                sent = await event.client.send_file(event.chat_id, mk, caption=mk.text)
                await gifspam(event, event, sent) 
                await asyncio.sleep(0.01)  # 10x faster
                
        elif event.reply_to_msg_id and mk.text:
            count = int(altron[1]) if len(altron) > 1 else 5
            if count <= 0:
                await event.reply("❌ Count must be greater than 0!")
                return
                
            message = mk.text
            # 10x faster text spam with reply
            for _ in range(count):
                await event.client.send_message(event.chat_id, message, reply_to=event.reply_to_msg_id)
                await asyncio.sleep(0.01)  # 10x faster
        else:
            await event.reply(f"😈 **Usage:**\n  » {hl}spam 13 Altron\n  » {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » {hl}spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")

    except (IndexError, ValueError):
        await event.reply(f"😈 **Usage:**\n  » {hl}spam 13 Altron\n  » {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » {hl}spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
    except Exception as e:
        print(f"Spam error: {e}")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
async def pspam(event):
    if event.sender_id not in SUDO_USERS:
        return
        
    if event.chat_id in GROUP:
        await event.reply("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        return
        
    try:
        # Check if replying to a protected user
        if event.reply_to_msg_id:
            mk = await event.get_reply_message()
            if mk and mk.sender_id:
                protected, msg = await is_protected(mk.sender_id)
                if protected:
                    await event.reply(msg)
                    return
        
        counter = int(event.text.split(" ", 2)[1])
        if counter <= 0:
            await event.reply("❌ Count must be greater than 0!")
            return
            
        porrn = choice(PORMS)
        # 10x faster pspam
        for _ in range(counter):
            alt = await event.client.send_file(event.chat_id, porrn)
            await gifspam(event, event, alt) 
            await asyncio.sleep(0.01)  # 10x faster
    except (IndexError, ValueError):
        await event.reply(f"🔞 **Usage:**  {hl}pspam 13")
    except Exception as e:
        print(f"PSpam error: {e}")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
async def hang(event):
    if event.sender_id not in SUDO_USERS:
        return
        
    if event.chat_id in GROUP:
        await event.reply("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        return
        
    try:
        # Check if replying to a protected user
        if event.reply_to_msg_id:
            mk = await event.get_reply_message()
            if mk and mk.sender_id:
                protected, msg = await is_protected(mk.sender_id)
                if protected:
                    await event.reply(msg)
                    return
        
        counter = int(event.text.split(" ", 2)[1])
        if counter <= 0:
            await event.reply("❌ Count must be greater than 0!")
            return
            
        hang = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰"
        
        # 10x faster hang spam
        for _ in range(counter):
            await event.respond(hang)
            await asyncio.sleep(0.01)  # 10x faster (was 0.3)
    except (IndexError, ValueError):
        await event.reply(f"😈 **Usage:** {hl}hang 10")
    except Exception as e:
        print(f"Hang error: {e}")
                
