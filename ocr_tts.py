from ocr import OCR
from tts import TTS

class Reader:

    def __init__(self) -> None:
        self.ocr = OCR()
        self.tts = TTS()

    def play(self, screenshot):
        pass

    def pause(self):
        pass


        
