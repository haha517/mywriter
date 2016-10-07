# -*- coding: utf-8 -*-
from gtts import gTTS
import os
tts = gTTS(text='游客朋友您好，今天我们来到的是白云山风景名胜区。\
白云山风景名胜区位于陕北佳县城南5公里处的黄河之滨，国家4A级旅游景区。\
这里古称双龙岭，亦叫嵯峨岭，后因终年白云缭绕，而称白云山。', lang='ZH-cn')
tts.save("goodgtts.mp3")
