class script(object):
    START_TXT = """Hᴇʏ {},
        Mʏ ɴᴀᴍᴇ ɪs Jᴇɴɴɪᴇ `BLΛƆKPIИK,Pʟᴇᴀsᴇ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ.."""
    HELP_TXT = """𝙷𝙴𝚈 {}
Tʜᴇsᴇ Aʀᴇ Tʜᴇ Aᴠᴀɪʟᴀʙʟᴇ Lɪsᴛ Oғ Mʏ Cᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """ 𝑯𝒆𝒚, 𝑰 𝑨𝒎 𝑱𝒆𝒏𝒏𝒊𝒆
  ❥ Cʀᴇᴀᴛᴏʀ:  <a href=@Arjun_La_Lis_A>𝗔𝗿𝗷𝘂𝗻</a>
  ❥ Lɪʙʀᴀʀʏ:     𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺
  ❥ Lᴀɴɢᴜᴀɢᴇ:    𝗣𝘆𝘁𝗵𝗼𝗻 𝟯
  ❥ Dᴀᴛᴀ Bᴀsᴇ:   𝗠𝗼𝗻𝗴𝗼 𝗗𝗕
  ❥ Bᴏᴛ Sᴇʀᴠᴇʀ:  𝗛𝗲𝗿𝗼𝗸𝘂"""
    MANUELFILTER_TXT = """Help: <b>Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀ</b>

- Fɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Jᴇɴɴɪᴇ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ
<b>NOTE:</b>
          
1. Jᴇɴɴɪᴇ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>Commands and Usage:</b>
• /filter - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Jᴇɴɴɪᴇ Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>NOTE:</b>
1. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Jᴇɴɴɪᴇ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+WqhO2sfnZxcxYjk1)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Aᴜᴛᴏᴍᴀᴛɪᴄ Fɪʟᴛᴇʀ</b>

<b>NOTE:</b>
1. Mᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
3. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """Help: <b>Aᴛᴛᴀᴄʜᴍᴇɴᴛs</b>

- Usᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs 
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<ʙ>NOTE:</ʙ>
1. Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <ᴄᴏᴅᴇ>/ᴄᴏɴɴᴇᴄᴛ</ᴄᴏᴅᴇ> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ PM

<ʙ>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</ʙ>
• /ᴄᴏɴɴᴇᴄᴛ  - <ᴄᴏᴅᴇ>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ PM</ᴄᴏᴅᴇ>
• /ᴅɪsᴄᴏɴɴᴇᴄᴛ  - <ᴄᴏᴅᴇ>ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ</ᴄᴏᴅᴇ>
• /ᴄᴏɴɴᴇᴄᴛɪᴏɴs - <ᴄᴏᴅᴇ>ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs</ᴄᴏᴅᴇ>"""
    EXTRAMOD_TXT = """Help: <b>Cᴜsᴛᴏᴍ Mᴏᴅᴜʟᴇs</b>

<b>NOTE:</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ Jᴇɴɴɪᴇ

<ʙ>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</ʙ>
• /ɪᴅ - <ᴄᴏᴅᴇ>ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.</ᴄᴏᴅᴇ>
• /ɪɴғᴏ  - <ᴄᴏᴅᴇ>ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.</ᴄᴏᴅᴇ>
• /ɪᴍᴅʙ  - <ᴄᴏᴅᴇ>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDʙ sᴏᴜʀᴄᴇ.</ᴄᴏᴅᴇ>
• /sᴇᴀʀᴄʜ  - <ᴄᴏᴅᴇ>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs.</ᴄᴏᴅᴇ>"""
    ADMIN_TXT = """Help: <b>Aᴅᴍɪɴ Mᴏᴅᴜʟᴇs</b>

<b>NOTE:</b>
Tʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs

<ʙ>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</ʙ>
• /ʟᴏɢs - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴄᴇɴᴛ ᴇʀʀᴏʀs</ᴄᴏᴅᴇ>
• /sᴛᴀᴛs - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ғɪʟᴇs ɪɴ ᴅʙ.</ᴄᴏᴅᴇ>
• /ᴅᴇʟᴇᴛᴇ - <ᴄᴏᴅᴇ>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ.</ᴄᴏᴅᴇ>
• /ᴜsᴇʀs - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.</ᴄᴏᴅᴇ>
• /ᴄʜᴀᴛs - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs </ᴄᴏᴅᴇ>
• /ʟᴇᴀᴠᴇ  - <ᴄᴏᴅᴇ>ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.</ᴄᴏᴅᴇ>
• /ᴅɪsᴀʙʟᴇ  -  <ᴄᴏᴅᴇ>ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</ᴄᴏᴅᴇ>
• /ʙᴀɴ  - <ᴄᴏᴅᴇ>ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ.</ᴄᴏᴅᴇ>
• /ᴜɴʙᴀɴ  - <ᴄᴏᴅᴇ>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.</ᴄᴏᴅᴇ>
• /ᴄʜᴀɴɴᴇʟ - <ᴄᴏᴅᴇ>ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs</ᴄᴏᴅᴇ>
• /ʙʀᴏᴀᴅᴄᴀsᴛ - <ᴄᴏᴅᴇ>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs</ᴄᴏᴅᴇ>"""
    STATUS_TXT = """❊ 𝗧𝗼𝘁𝗮𝗹 𝗜𝗻𝗱𝗲𝘅𝗲𝗱 𝗙𝗶𝗹𝗲𝘀: <code>{1986533}</code>
❊ 𝗧𝗼𝘁𝗮𝗹 𝗨𝘀𝗲𝗿𝘀: <code>{}</code>
❊ 𝗧𝗼𝘁𝗮𝗹 𝗖𝗵𝗮𝘁: <code>{}</code>
❊ 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 𝗨𝘀𝗲𝗱: <code>{}</code> 𝙼𝚒𝙱
❊ 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗽𝗰: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
