import pytesseract as pt
import platform
from PIL import Image



class OCR:
    
    def __init__(self) -> None:
        if platform.system() == 'Darwin':  # macOS
            pt.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.4/bin/tesseract'
        elif platform.system() == 'Windows':
            pt.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        else:
            print('Operating system not supported')

    image_file = '../text_images/pfkm-4.jpg'

    def image_to_string(self, image):
        text = pt.image_to_string(image)
        text = text.replace('\n', ' ')
        return text
