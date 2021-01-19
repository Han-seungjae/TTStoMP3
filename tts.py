from gtts import gTTS

b = input('파일명을 입력하세요 : ')
a = input('내용을 입력하세요 : ')


tts = gTTS('{}'.format(a), lang='ko'c)
tts.save('{}.mp3'.format(b))
