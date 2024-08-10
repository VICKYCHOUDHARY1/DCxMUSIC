#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

import re

from os import getenv

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

from dotenv import load_dotenv

from pyrogram import filters

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

load_dotenv()

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this value from my.telegram.org/apps

API_ID = int(getenv("API_ID"))

API_HASH = getenv("API_HASH")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get your token from @BotFather on Telegram.

BOT_TOKEN = getenv("BOT_TOKEN")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get your mongo url from cloud.mongodb.com

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 999999))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Chat id of a group for logging bot's activities

LOGGER_ID = int(getenv("LOGGER_ID", None))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this value @MissRose_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7001982096))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Your heroku app name

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Get it from http://dashboard.heroku.com/account

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/vicky0604hello/DCxMUSIC")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Fill this variable if your upstream repository is private

GIT_TOKEN = getenv("GIT_TOKEN", None)  

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_DC_BOTS")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TEAM_DC_BOTS")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Set this to True if you want the assistant to automatically leave chats after an interval

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this credentials from https://developer.spotify.com/dashboard

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "821d1bf8430346b98aa98e62ceb31416")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5fad47a0e1a340ca9cf88d9aa60b494b")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get your pyrogram v2 session on Telegram
STRING1 = getenv("STRING_SESSION", None)

STRING2 = getenv("STRING_SESSION2", None)

STRING3 = getenv("STRING_SESSION3", None)

STRING4 = getenv("STRING_SESSION4", None)

STRING5 = getenv("STRING_SESSION5", None)

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

BANNED_USERS = filters.user()

adminlist = {}

lyrical = {}

votemode = {}

autoclean = []

confirmer = {}

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/83da25751161cc4b9d408.jpg")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/59d3d5fbaca41ec09f33d.jpg")

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

PLAYLIST_IMG_URL = "https://graph.org/file/954b70e8c68314875cb78.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

STATS_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

TELEGRAM_AUDIO_URL = "https://graph.org/file/92349afcdfb9da6f7c693.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

TELEGRAM_VIDEO_URL = "https://graph.org/file/92349afcdfb9da6f7c693.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

STREAM_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

SOUNCLOUD_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

YOUTUBE_IMG_URL = "https://graph.org/file/4cf64c2a1902b56a52d13.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

# Get this type of link from @vTelegraphBot on Telegram by sending image

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
#---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X