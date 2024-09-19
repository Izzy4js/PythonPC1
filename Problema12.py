"""
Problema 12:
La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios,
anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
la web.
Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip
Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.
"""

archivo = input("Introduce el nombre del archivo: ").strip().lower()

tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

extension = ""
if "." in archivo:
    extension = archivo[archivo.rfind("."):]

tipo_mime = tipos_mime.get(extension, "application/octet-stream")
print("Tipo MIME:", tipo_mime)