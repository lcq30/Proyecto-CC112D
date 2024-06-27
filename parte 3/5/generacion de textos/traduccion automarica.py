from googletrans import Translator

# Crear un objeto Translator
translator = Translator()

# Ejemplo de traducción de texto
texto = "hello world"
traduccion = translator.translate(texto, dest='es')

# Imprimir el texto original y la traducción
print(f'Texto original: {texto}')
print(f'Traducción: {traduccion.text}')

