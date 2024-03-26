from ocr import OCR
from tts import TTS
import pygame

class Reader:

    def __init__(self) -> None:
        self.ocr = OCR()
        self.tts = TTS()
        pygame.mixer.init()
        self.channel = pygame.mixer.Channel(0)
        self.state = 'stopped'

    def play(self, image):
        # print("Started \"OCRTTS Play\"")
        # text = self.ocr.image_to_string(image)
        # self.tts.synthesize(text)
        # self.sound = pygame.mixer.Sound("audio_output/temp.wav")
        # # self.sound.play()
        # self.channel.play(self.sound)

        if not self.channel.get_busy():
            self.state = 'stopped'
        if self.state == 'stopped':
            print("Started \"OCRTTS Play\"")
            text = self.ocr.image_to_string(image)
            self.tts.synthesize(text)
            self.sound = pygame.mixer.Sound("audio_output/temp.wav")
            self.channel.play(self.sound)
            self.state = 'playing'
        elif self.state == 'paused':
            self.channel.unpause()
            self.state = 'playing'

    def pause(self):
        # if self.channel.get_busy():
        #     self.channel.pause()

        if self.state == 'playing':
            self.channel.pause()
            self.state = 'paused'
        
