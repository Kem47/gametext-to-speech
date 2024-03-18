import pytesseract as pt
import platform
from PIL import Image



class OCR:
    
    def __init__(self) -> None:
        pass
    if platform.system() == 'Darwin':  # macOS
        pt.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.4/bin/tesseract'
    elif platform.system() == 'Windows':
        pt.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    else:
        print('Operating system not supported')

    image_file = '../text_images/pfkm-4.jpg'


    # get text from image - pytesseract
    image = Image.open(image_file)
    text = pt.image_to_string(image)
    # boxes = pt.image_to_boxes(image)
    data = pt.image_to_data(image, output_type=pt.Output.DICT)
    osd = pt.image_to_osd(image, output_type=pt.Output.DICT)
    print(text)