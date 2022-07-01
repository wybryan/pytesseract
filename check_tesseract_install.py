import os
import subprocess
from PIL import Image

import pytesseract


def exec_shell(cmd):
    result = subprocess.getstatusoutput(cmd)
    return result

_, tesseract_path = exec_shell('which tesseract')

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = tesseract_path
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'))))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png')))

# List of available languages
print(pytesseract.get_languages(config=''))

# French text image to string
print(pytesseract.image_to_string(Image.open(os.path.join(os.path.dirname(__file__),'tests/data', 'test-european.jpg')), lang='fra'))

# Batch processing with a single file containing the list of multiple image file paths
print(pytesseract.image_to_string(os.path.join(os.path.dirname(__file__),'tests/data', 'images.txt')))

# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'), timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'), timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'))))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'))))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'))))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'), extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'), extension='hocr')

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml(os.path.join(os.path.dirname(__file__),'tests/data', 'test.png'))