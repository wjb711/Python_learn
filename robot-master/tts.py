# -*- coding: utf-8 -*-
import PyBaiduYuyin as pby
def speak(test):
    tts = pby.TTS(app_key='wxNGGTpSQTKYjROe5gpgBKDO', secret_key='f4a44a0f4c5d12173c34e5b258ef1f98')
    test=test.encode('utf-8')
    tts.say(test)
