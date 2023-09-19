import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1356469075))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vbtsvillian/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/villen_012")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ll_Hidden_leaf_ll")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/10dafdc710eb6e3ee469e.jpg"
                     "https://graph.org/file/224bd60fa314722f98bf6.jpg"
                     "https://graph.org/file/82cfaa6c4d09df2153e57.jpg"
                     "https://graph.org/file/fab3d1d09513076dff810.jpg"
                     "https://graph.org/file/dd20a34de2e051a38c878.jpg"
                     "https://graph.org/file/7dfa63df67e93d69312f6.jpg"
                     "https://graph.org/file/0cbf8de9e33aff4418818.jpg"
                     "https://graph.org/file/00b9ebe60c82887956b69.jpg"
                     "https://graph.org/file/ea97422373541e862bc33.jpg"
                     "https://graph.org/file/d0b42f292ee5232dc2209.jpg"
                     "https://graph.org/file/c6c74d6235537b2417407.jpg"
                     "https://graph.org/file/193bf923d120a50bfa84f.jpg"
                     "https://graph.org/file/c814d273038e082c0f791.jpg"
                     "https://graph.org/file/6ed92054f6253368047ba.jpg"
                     "https://graph.org/file/10159c98a3cdb10079ccb.jpg"
                     "https://graph.org/file/717d51d89807cc7af988c.jpg"
                     "https://graph.org/file/6fa7567ec0f11a1f5dead.jpg"
                     "https://graph.org/file/e1bab38e048f715c5b558.jpg"
                     "https://graph.org/file/3ab2901650851a2c747aa.jpg"
                     "https://graph.org/file/7f63943d9ff5a29881208.jpg"
                     "https://graph.org/file/9a3e917ca41448f0b24ab.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/23fe3ea3615817f63b66e.jpg"
                    "https://graph.org/file/717d51d89807cc7af988c.jpg"
                    "https://graph.org/file/4f25b6bb9d306a18072fa.jpg"
                    "https://graph.org/file/10159c98a3cdb10079ccb.jpg"
                    "https://graph.org/file/4aa8b8df048863b93e157.jpg"
                    "https://graph.org/file/6ed92054f6253368047ba.jpg"
                    "https://graph.org/file/d0b42f292ee5232dc2209.jpg"
                    "https://graph.org/file/ea97422373541e862bc33.jpg"
                    "https://graph.org/file/de47280ed99e10d262b4a.jpg"
                    "https://graph.org/file/7dfa63df67e93d69312f6.jpg"
                    "https://graph.org/file/c0e934aab37544af99e53.jpg"
                    "https://graph.org/file/dd20a34de2e051a38c878.jpg"
                    "https://graph.org/file/df06c8a46fb0fd3589cf3.jpg"
                    "https://graph.org/file/261eccc6a8d08ee57b91e.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
