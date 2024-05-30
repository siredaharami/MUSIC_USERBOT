from SafoneAPI import SafoneAPI

from PBXMUSIC.core.bot import PBX
from PBXMUSIC.core.dir import dirr
from PBXMUSIC.core.git import git
from PBXMUSIC.core.userbot import Userbot
from PBXMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PBX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
APP = "MissBroken_Bot"  # connect music api key "Dont change it"
