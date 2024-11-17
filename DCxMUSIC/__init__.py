from DCxMUSIC.core.bot import DC
from DCxMUSIC.core.dir import dirr
from DCxMUSIC.core.git import git
from DCxMUSIC.core.userbot import Userbot
from DCxMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DC()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

