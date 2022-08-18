import os
import subprocess

class SofTalk:
    def play(self, char_no, text):
        path = './softalk/SofTalk.exe'
        char = '/T:' + str(char_no)
        tts = '/W:' + text
        command = [path, char, tts]
        c = ' '.join(command)
        p = subprocess.Popen(c)

