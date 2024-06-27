# Librería PDF -> HTML
import fitz



def PdfToHTML():
    # Insertamos el PDF
    pdf = "pdfprueba.pdf"
    documento = fitz.open(pdf)
    pagina = documento.loadPage(0)
    doc = fitz.open(pdf)
    salida = open(pdf + ".html", "wb")
    for pagina in doc:
        texto = pagina.getText("html").encode("utf8")
        salida.write(texto)
        salida.write(b"\n--------------------\n")
    salida.close()
    Resumen()



PdfToHTML()