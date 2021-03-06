import xbmcaddon
import sys
import os

import helper


addon = xbmcaddon.Addon(id='plugin.video.Outermatrix-KiddoTV')
addonpath = xbmc.translatePath( addon.getAddonInfo('path') )


channels = [
["Baby First TV","BabyFirstTV"],
["Barbie","Barbie"],
["Disney Films","DisneyFilms"],
["Disney Junior","DisneyJunior"],
["Incredible Hulk","IncredibleHulk"],
["Monster High","MonsterHigh"],
["Nick Jr","NickJr"],
["Spiderman","Spiderman"],
["zui.com","zui"],
]

def mainPage():
	for channel in channels:
		channelPic = os.path.join(addonpath,'resources','images',channel[1]+'.png')
		helper.addDirectoryItem(channel[0],{"channel":channel[1]}, channelPic)
	helper.endOfDirectory()

    
if not sys.argv[2]:
    mainPage()
else:
	global params
	params = helper.get_params()
	importChannel = "channels."+params['channel']
	channel = __import__(importChannel)
