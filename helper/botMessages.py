#!/usr/bin/env python3


# Bot defined Messages
class BotMessage(object):
    common_text = "\n\n<u>If you are facing any problem, so report at @AJPyroVerseGroup</u>"
    help_msg = f"<i>To use me, Just Send me any direct downloading link, and I will send you the file as telegram file.</i>{common_text}"
    start_msg = f"<b>السلام عليكم أنا بوت لرفع الملفات , فقط أرسل رابط تحميل مباشر لملف و سأرفعه لك على التلجرام \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 \n\n لدعم استمرار المشروع هنا \n\n http://paypal.me/kelectronic89 \n\n تم تطويره بواسطة  @AJTimePyro"
    not_joined_community = f"<b>To use this bot, you need to Join our Channel and Group.</b>{common_text}"
    broadcast_failed = "<b>Broadcasting Message can`t be empty</b>"
    processing_url = "<i>Please wait while I am Processing File</i>"
    starting_to_download = "<i>Starting to Upload the file.... Have Some Patience!!!</i>"
    unsuccessful_upload = f'Uploading went <b>Unsuccessful</b>, Something Went Wrong{common_text}'
    uploading_msg = "<b>File successfully downloaded to server, Now uploading to Telegram.</b>"
    youtube_url = "<b>Currently I do not support youtube videos.</b>"
    telegramLimit = f"<b>It is more than limit of telegram.</b>"
    
