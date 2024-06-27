from PIL import Image #importo la clase image de modulo pil para cargar imagenes
from pytesseract import *
# direccion del tesseract
pytesseract.tesseract_cmd = r'C:\Users\Usuario\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("image.jpg")

resultado = pytesseract.image_to_string(img)

print(resultado)