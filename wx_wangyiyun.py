import os
import itchat
from NetEaseMusicApi import interact_select_song
import subprocess
from itchat.content import *

HELP_MSG = u'''
欢迎使用微信网易云音乐
帮助： 显示帮助
关闭： 关闭歌曲
歌名： 按照引导播放音乐
'''

path = "/Users/liying/Documents/stop.mp3"
with open(path, 'w') as f: pass
def stop_music():
    subprocess.call(['open', path])

@itchat.msg_register(TEXT)
def music_player(msg):
    # print(msg)
    if msg["ToUserName"] != 'filehelper': return
    if msg['Text'] == u'关闭':
        stop_music()
        itchat.send(u'音乐已关闭', 'filehelper')
    elif msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']), 'filehelper')
itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()



