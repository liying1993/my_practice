from collections import namedtuple

Message = namedtuple("Message", ["text"])
message = Message("lallalal")


class Core:
    def __init__(self):
        self.functionDict = {'FriendChat': {}, 'GroupChat': {}, 'MpChat': {}}
core = Core()
def msg_register(msgType,  isFriendChat=False, isGroupChat=False, isMpChat=False):
    if not (isinstance(msgType, list) or isinstance(msgType, tuple)):
        msgType = [msgType]
    def _msg_register(fn):
        for _msgType in msgType:
            if isFriendChat:
                core.functionDict['FriendChat'][_msgType] = fn
            if isGroupChat:
                core.functionDict['GroupChat'][_msgType] = fn
            if isMpChat:
                core.functionDict['MpChat'][_msgType] = fn
            if not any((isFriendChat, isGroupChat, isMpChat)):
                core.functionDict['FriendChat'][_msgType] = fn
        return fn
    return _msg_register

@msg_register("text")
def text_reply(msg):
    return msg.text

if __name__ == '__main__':
    text_reply(message)
    print(core.functionDict["FriendChat"]["text"].__dict__)