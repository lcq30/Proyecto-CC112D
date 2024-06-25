import pdfplumber # PARA EXTRAER TEXTO
import pytesseract # PARA RECONOCER TEXTOS E IMAGENES
from PIL import Image #ABRIR Y MANIPULAR IMAGENES
from google.cloud import translate_v2 as translate  # CAMBIO DE IDIOMA
from bs4 import BeautifulSoup # PARA ANALIZAR DOCUMENTOS HTML Y XML
import requests #DESCARGAR DE WEB
import nltk #PROCESAMIENTO DEL LENGUAJE
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

translate_client = translate.Client()


pdf_text = """
I hope you are well. I wanted to thank 
him for his dedication in teaching this course.
 I have been working hard and I have learned.
  (I'm Rios) I write this here so that I can consider this part that I had to, 
  please approve me to transfer to chemistry: c. I very much appreciate your time and consideration.
"""
imagen = Image.open('imagen.jpeg')

url = 'https://www.example.com'

def extract_text_from_pdf(pdf_text):
    sentences = sent_tokenize(pdf_text)
    words = word_tokenize(pdf_text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    freq = FreqDist(filtered_words)
    top_sentences = sorted(sentences, key=lambda x: sum(freq[word.lower()] for word in word_tokenize(x) if word.lower() not in stop_words), reverse=True)[:2]

    return top_sentences


def translate_text(texto, target_language='es'):

    translation = translate_client.translate(texto, target_language=target_language)
    return translation["translatedText"]

def ocr_text_from_image(imagen):

    texto_reconocido = pytesseract.image_to_string(imagen)
    return texto_reconocido

def extract_text_from_web(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    texto_web = soup.get_text()
    return texto_web

print("Resumen del texto del PDF:")
pdf_summary = extract_text_from_pdf(pdf_text)
for sentence in pdf_summary:
    print(sentence)

print("\nTexto traducido:")
texto_traducido = translate_text(pdf_text, target_language='es')
print(texto_traducido)

print("\nTexto reconocido desde la imagen:")
texto_reconocido = ocr_text_from_image(imagen)
print(texto_reconocido)

print("\nTexto extraído de la página web:")
texto_web = extract_text_from_web(url)
print(texto_web)
