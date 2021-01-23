from gtts import gTTS
import os

print('1> 한국어 2> 영어')
ee = int(input('언어를 선택하세요 : '))

print(' 1> 일반 모드 2> 대본 모드')
mod = int(input('모드를 선택하세요 : '))
num = 0



if mod == 1:
    b = input('파일명을 입력하세요 : ')
    a = input('내용을 입력하세요 : ')
    if ee == 1:
        tts = gTTS('{}'.format(a), lang='ko')
        tts.save('{}.mp3'.format(b))
        
    elif ee == 2:
        tts = gTTS('{}'.format(a), lang='en')
        tts.save('{}.mp3'.format(b))

ppap = open('list.txt', 'r').read().split('\n')        


if mod == 2:
    if ee == 1:
        for x in ppap:
            tts = gTTS('{}'.format(ppap[num]), lang='ko')
            tts.save('{}.mp3'.format(num))
            num = num + 1

    if ee == 2:
        for x in ppap:
            tts = gTTS('{}'.format(ppap[num]), lang='en')
            tts.save('{}.mp3'.format(num))
            num = num + 1