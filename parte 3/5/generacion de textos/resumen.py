import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import heapq

# Descargar los recursos necesarios para NLTK (solo la primera vez)
nltk.download('punkt')
nltk.download('stopwords')

def resumir_texto(texto, numero_oraciones=2):
    oraciones = sent_tokenize(texto)
    palabras = word_tokenize(texto.lower())  # Convertir todo a minúsculas

    # Obtener las stopwords en español
    stopwords_lista = set(stopwords.words('spanish'))

    # Eliminar las stopwords y la puntuación de las palabras
    palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in stopwords_lista]

    # Calcular la frecuencia de cada palabra
    frecuencia_palabras = FreqDist(palabras_filtradas)

    # Asignar una puntuación a cada oración según la suma de las frecuencias de las palabras que contiene
    puntuacion_oraciones = {}
    for i, oracion in enumerate(oraciones):
        for palabra in word_tokenize(oracion.lower()):
            if palabra in frecuencia_palabras:
                if i in puntuacion_oraciones:
                    puntuacion_oraciones[i] += frecuencia_palabras[palabra]
                else:
                    puntuacion_oraciones[i] = frecuencia_palabras[palabra]

    # Obtener las oraciones con mayor puntuación
    oraciones_resumen = heapq.nlargest(numero_oraciones, puntuacion_oraciones, key=puntuacion_oraciones.get)
    resumen = ' '.join([oraciones[i] for i in sorted(oraciones_resumen)])

    return resumen

# Ejemplo
texto_ejemplo = """
Los lenguajes son una parte crucial de la inteligencia humana e importantes para la comunicación humana. Al investigar la comprensión automática y la generación de lenguajes humanos, el procesamiento del lenguaje natural (NLP) ha sido un subcampo central de la investigación en inteligencia artificial. Desde la década de 1950, la tecnología de NLP ha recibido una atención continua por parte de la investigación y se han logrado grandes avances. Hoy en día, la tecnología NLP se está convirtiendo en una parte indispensable de nuestro negocio y de nuestra vida diaria. Por ejemplo, los motores de búsqueda procesan automáticamente billones de documentos a través de Internet, obtienen conocimientos de ellos y responden a las consultas de los usuarios basándose en su comprensión. Los minoristas en línea procesan millones de descripciones de productos y comentarios de usuarios para recomendar el producto más adecuado según la búsqueda de un usuario. Los sistemas de diálogo automático y los sistemas de traducción son cada vez más utilizados para facilitar la comunicación. En los negocios, los motores de análisis de texto han estado reemplazando el trabajo manual en el análisis de grandes cantidades de documentos para una mejor toma de decisiones.
"""
resumen = resumir_texto(texto_ejemplo)
print("Texto original:")
print(texto_ejemplo)
print("\nResumen:")
print(resumen)