
import math
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Uploader.script import Translation



async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        time_to_completion = TimeFormatter(milliseconds=time_to_completion)
        
        progress = "Pʀᴏɢʀᴇss... {2} {0}{1}\n\n".format(
            ''.join(["🟩" for _ in range(math.floor(percentage / 5))]),
            ''.join(["⬜️" for _ in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )


        tmp = progress + "✊💦 Uᴘʟᴏᴀᴅᴇᴅ : {0} \n\n✊💨 Sᴘᴇᴇᴅ : {2}/s\n\n ✊💨 Fɪʟᴇ Sɪᴢᴇ : {1} ✊💦 Tɪᴍᴇ Lᴇғᴛ : {4}\n\n © @TG_YouTubeBot♥️".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s",
            time_to_completion if time_to_completion != '' else  "0 s"
        )
        try:
            await message.edit(text=f"{tmp}\n {ud_type}")
        except:
            pass





SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']




def huanbytes(size_in_bytes) -> str:
    if size_in_bytes is None:
        return '0B'
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        return f'{round(size_in_bytes, 2)}{SIZE_UNITS[index]}'
    except IndexError:
        return 'File too large'

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"{str(round(size, 2))} {Dic_powerN[n]}B"


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)}d, " if days else "")
        + (f"{str(hours)}h, " if hours else "")
        + (f"{str(minutes)}m, " if minutes else "")
        + (f"{str(seconds)}s, " if seconds else "")
        + (f"{str(milliseconds)}ms, " if milliseconds else "")
    )

    return tmp[:-2]
