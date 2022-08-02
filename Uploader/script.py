from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT_Old = """
Hi {} 🥰

💡 `I am Telegram most Powerful Url Uploader Bot`

<b>⚙️ Press /settings to change my settings</b>

Use help button to know how to use me

🦊 <b>Maintained By</b> : [MyTestBotZ](https://telegram.me/OO7ROBOT)
"""
    START_TEXT = """
Hello👋 {} , 
<b>a Simple YouTube Downloader Bot</b> that can:
  ➠ Download YouTube videos
  ➠ Download audio from YouTube videos
  ➠ Support YouTube Shorts Link
  ➠ YouTube Playlist (Coming Soon).....
  
<b>⚙️ Press /settings to change my settings</b>

<b>NB</b>: <code> Bot may slow ,so wait 5 - 10 second to bot respond....
please dont spam with links...</code>
┈┈┈••💙✿💛✿💚••┈┈┈
<b>Made with ♥️ by @MyTestBotZ </b>
"""
    HELP_TEXT_Old = """
You need Help ?? 😅
   
✵ First go to the /settings and change the bot behavior as your choice.

✵ Send me the custom thumbnail to save it permanently. (𝚘𝚙𝚝𝚒𝚘𝚗𝚊𝚕)

✵ Now send me the ytdl or direct link.

✵ Select the desired option.

✵ Then be relaxed your file will be uploaded soon..

✵ Use `/caption` to Set caption as Reply to Media


 
"""
    HELP_TEXT = """<b><u>How to Use me 🤔</u></b>
    
  <b>First go to the /settings and change the bot behavior as your choice.</b>

1. <b>Send Any Youtube url</b>
        
2. <b>Select the Desired File Size Button.</b>
  
   <b>Thats it, I will Do Rest of it 😌 </b>
   
<b><u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.

<b><u>To Delete Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail

➠ Use /caption to Set caption as Reply to Media
"""
    ABOUT_TEXT = """
**✊💦 My Name** : [YouTube📥Bot](https://telegram.me/TG_YouTubeBot)

**✊💦 Channel** : [MyTestBotZ](https://t.me/MyTestBotZ)

**✊💦 Version** : [2.5 Stable](https://t.me/Tg_Youtubebot)

**✊💦 Source** : [Click Here](https://github.com/OO7ROBot)

**✊💦 Server** : [Heroku](https://heroku.com/)

**✊💦 Language :** [Python 3.10.5](https://www.python.org/)

**✊💦 Framework :** [Pyrogram 2.0.35](https://docs.pyrogram.org/)

**✊💦 OtherBotZ :** [My Bots List](https://telegram.me/mybotzlist)

**✊💦 Credits :** `Everyone in this journey`

**✊💦 Maintained By :  @OO7ROBot** 

"""


    PROGRESS = """
✊💦 Uᴘʟᴏᴀᴅᴇᴅ : {1}\n\n 
✊💨 Sᴘᴇᴇᴅ : {3} \n\n
✊💦 Fɪʟᴇ Sɪᴢᴇ : {2} \n\n
✊💨 Tɪᴍᴇ Lᴇғᴛ : {4} \n\n

"""
    ID_TEXT = """
🆔 Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

    PLANS = """ You Can Use This Bot 100% Freely Until I Change My Mind 😜😌😌
    
   If You Like To Support My Works, Please Feel Free To Donate Any Amount You Like. 
   
   • Cᴏɴᴛᴀᴄᴛ ᴍᴇ ᴠɪᴀ @OO7ROBot"""
    PLANS_old = """🔰 My Plans 🔰

🛡️PLANS 1(PER 50 LINKS)🛡️

🌸 1 Day      - ₹20
🌺 1 Week   - ₹80
🌷 1 Month - ₹140

🛡️ PLANS 2(PER 100 LINKS)🛡️

🌸 1 Day      - ₹40
🌺 1 Week   - ₹100
🌷 1 Month - ₹160

🛡️ PLANS 3(PER 200 LINKS)🛡️

🌸 1Day      - ₹60
🌺 1Week   - ₹120
🌷 1Month - ₹180

"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️ Settings', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('❓ Help', callback_data='help'),
        InlineKeyboardButton('♻️ About', callback_data='about')
        ],[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('♻️ About', callback_data='about')
        ],[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('❓ Help', callback_data='help')
        ],[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    TEXT = "sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴇᴛ ɪᴛ"
    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    
    FORMAT_SELECTION = "<b>Now Select the desired formats, File size might be approximate..\n\n• To Toggle File🔁Video Goto /settings</b>"
    
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_FILE = "📥 Downloading  File "
    UPLOAD_FILE = " UploadinG 📤 \n\n To  transfer.sh "
    ANNO_UPLOAD = " UploadinG📤 \n\n To  anonfiles.com "
    BAY_UPLOAD = " UploadinG📤 \n\n To  bayfiles.com "
    GO_FILE_UPLOAD = " 📤UploadinG📤 \n\n To  gofile.io "
    
    DOWNLOAD_START_old = "Trying to Download ⌛\n\n💮🌸 <i>{} 💮🌸</i>"
    UPLOAD_START_old = "💮🌸 <i>{} 💮🌸</i>\n\n📤 Uploading Please Wait "
    DOWNLOAD_START = "📥 <b>Dᴏᴡɴʟᴏᴀᴅɪɴɢ Tᴏ Mʏ sᴇʀᴠᴇʀ Pʟᴇᴀsᴇ Wᴀɪᴛ</b>... \n\n➤Fɪʟᴇ Nᴀᴍᴇ :<i> {}</i>\n\nⁱᵗˢ ᵗᵃᵏᵉ ᵗⁱᵐᵉ ᵈᵉᵖᵉⁿᵈ ᵒⁿ ʸᵒᵘʳ ᶠⁱˡᵉ ˢⁱᶻᵉ"
    UPLOAD_START = "📤 <b>Uᴘʟᴏᴀᴅɪɴɢ ᴛᴏ TG...</b>\n\nFɪʟᴇ Nᴀᴍᴇ : <i>{}</i>"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG = " ThankYou For Using @TG_YouTubeBot. JOIN : https://t.me/MyTestBotZ\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/OO7ROBot'>@OO7ROBot</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Cᴜsᴛᴏᴍ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ. Tʜɪs ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜsᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ғɪʟᴇ."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Cᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Nᴏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ"
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    AFTER_GET_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\nJoin : .@MyTestBotZ"
    AFTER_GET_DL_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\nValid for <b>14</b> days."
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : @Tellybots_4u \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\n"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : @MyTestBotZ \n For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    
    FREE_USER_LIMIT_Q_SZE = "⏳ Please Wait 30 Second Before Next Request \n • Check Your Current /plans" """Cannot Process Free users only 1 request per 4 hrs\n
Upgrade your /plans to Remove Time Gaps and For link Processing"""
    
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<b>Sorry Dear You Must Join My Updates Channel😌😉....</b> \n <i>Due To OverLoad Only Channel Subscribers Can Use Meh</i>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    CHECK_LINK = "<b>⏳</b>"

    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! 🤩
    
Ex <a href='https://telegra.ph/file/ddb0caa56e6e5a4a7d3bc.jpg'>:</a> See This! 👇"""
