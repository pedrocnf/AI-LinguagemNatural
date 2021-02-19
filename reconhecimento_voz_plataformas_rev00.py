# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:09:59 2017

@author: pedro
"""

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

