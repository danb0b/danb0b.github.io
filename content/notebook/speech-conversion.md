---
title: Speech Conversion Tech
tags: 
- speech-to-text
- text-to-speech
summary: ""
---


https://github.com/KoljaB/RealtimeSTT
sudo apt install -y portaudio19-dev
pip install pyaudio
pip install RealtimeSTT


import RealtimeSTT


recorder.start()
recorder.stop()
print(recorder.text())

with AudioToTextRecorder() as recorder:
    print(recorder.text())