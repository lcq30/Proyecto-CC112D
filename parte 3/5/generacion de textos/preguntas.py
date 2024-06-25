#Cómo se importa la biblioteca NLTK en un script de Python?
pip install nltk
import nltk
nltk.download('all')
#¿Qué comando se utiliza para descargar conjuntos de datos y recursos adicionales para NLTK?
import nltk
nltk.download('all')
nltk.download('punkt')
nltk.download('stopwords')
#¿Cómo se puede acceder al primer texto de ejemplo proporcionado por NLTK después de importar los textos de ejemplo?
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
primer_texto = textos_disponibles[0]
contenido = nltk.corpus.gutenberg.raw(primer_texto)
# Imprimir el contenido del primer texto
print(f"Primer texto de ejemplo ({primer_texto}):")
print(contenido[:500])

#¿Cómo se busca en qué contexto aparece la palabra "monstrous" en el primer texto de ejemplo?
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
primer_texto = textos_disponibles[0]
palabras = nltk.corpus.gutenberg.words(primer_texto)
nltk_text = nltk.Text(palabras)
nltk_text.concordance("monstrous")

#¿Cómo puedes encontrar palabras que se utilizan en contextos similares a "monstrous" en el segundo texto de ejemplo?
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
segundo_texto = textos_disponibles[1]
palabras = nltk.corpus.gutenberg.words(segundo_texto)
nltk_text = nltk.Text(palabras)
print("Palabras en contextos similares a 'monstrous' en el segundo texto:")
nltk_text.similar("monstrous")

#Si quisieras encontrar contextos comunes para las palabras "monstrous" y "very" en el segundo texto de ejemplo, ¿qué comando usarías?
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
segundo_texto = textos_disponibles[1]
palabras = nltk.corpus.gutenberg.words(segundo_texto)
nltk_text = nltk.Text(palabras)
print("Contextos comunes para 'monstrous' y 'very' en el segundo texto:")
nltk_text.common_contexts(["monstrous", "very"])

#¿Cómo generas un diagrama de dispersión de las palabras "citizens", "democracy", "freedom", "duties", "America" en el cuarto texto de ejemplo?
import nltk
import matplotlib.pyplot as plt
textos_disponibles = nltk.corpus.gutenberg.fileids()
cuarto_texto = textos_disponibles[3]
palabras = nltk.corpus.gutenberg.words(cuarto_texto)
nltk_text = nltk.Text(palabras)
plt.figure(figsize=(12, 6))
nltk_text.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
plt.title('Diagrama de Dispersión de Palabras en el Cuarto Texto de Ejemplo')
plt.show()
#¿Cómo se cuenta el número total de tokens (palabras y símbolos de puntuación) en el primer texto de ejemplo?
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
primer_texto = textos_disponibles[0]
tokens = nltk.corpus.gutenberg.words(primer_texto)
num_tokens = len(tokens)

print(f"Número total de tokens en el primer texto ({primer_texto}): {num_tokens}")
#Calcula una medida interesante como diversidad léxica de un texto, que es la proporción del número de palabras únicas sobre el total de palabras.
# Esto puede dar una idea de cuán rico en vocabulario es un texto.
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
texto = textos_disponibles[0]
palabras = nltk.corpus.gutenberg.words(texto)
total_palabras = len(palabras)
palabras_unicas = set(palabras)
num_palabras_unicas = len(palabras_unicas)
diversidad_lexica = num_palabras_unicas / total_palabras
print(f"Texto: {texto}")
print(f"Número total de palabras: {total_palabras}")
print(f"Número de palabras únicas: {num_palabras_unicas}")
print(f"Diversidad léxica: {diversidad_lexica:.4f}")
#NLTK permite examinar la distribución de frecuencia de las palabras dentro de un texto,
# lo cual es útil para identificar las palabras más comunes o cómo se distribuye el uso de palabras específicas. Calcula ese concepto
import nltk
from nltk import FreqDist
textos_disponibles = nltk.corpus.gutenberg.fileids()
texto = textos_disponibles[0]
palabras = nltk.corpus.gutenberg.words(texto)
freq_dist = FreqDist(palabras)
print("Palabras más comunes y su frecuencia:")
print(freq_dist.most_common(20))
freq_dist.plot(20, cumulative=False)
#Filtrar palabras cortas (por ejemplo, palabras con menos de 3 letras) para centrarse en el contenido más significativo del texto.
import nltk
from nltk import FreqDist
textos_disponibles = nltk.corpus.gutenberg.fileids()
texto = textos_disponibles[0]
palabras = [palabra.lower() for palabra in nltk.corpus.gutenberg.words(texto) if len(palabra) >= 3]
freq_dist = FreqDist(palabras)
print("Palabras más comunes y su frecuencia:")
print(freq_dist.most_common(20))
freq_dist.plot(20, cumulative=False)
#Podemos estar interesados en encontrar palabras únicas de un largo específico. Calcula por ejemplo, palabras únicas de 5 letras.
import nltk
textos_disponibles = nltk.corpus.gutenberg.fileids()
texto = textos_disponibles[0]
palabras_unicas = set([palabra.lower() for palabra in nltk.corpus.gutenberg.words(texto) if len(palabra) == 5])
print("Palabras únicas de 5 letras:")
print(palabras_unicas)
print(f"Número total de palabras únicas de 5 letras: {len(palabras_unicas)}")
#Las colocaciones son secuencias de palabras que ocurren juntas inusualmente a menudo,
# como "red wine" o "hard work". Escribe NLTK para identificarlas fácilmente.
import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
##Crea un objeto BigramCollocationFinder
text = "GAAAAAAAAAAAAAAAAAAAAAA AEAAEA"
tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
text = "GAAAAAAAAAAAAAAAA  AEAEAEAE"
tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)

Crea un objeto BigramCollocationFinder






