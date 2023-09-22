# Leer el archivo de entrada
with open('UNICODE_8.txt', 'r', encoding='utf-8') as entrada_archivo:
    contenido = entrada_archivo.read()

# Insertar la cadena "AQUÍ" cada 20 caracteres
resultado = ""
for i, caracter in enumerate(contenido):
    resultado += caracter
    if (i + 1) % 20 == 0:
        resultado += "AQUÍ"

# Calcular la cantidad de caracteres necesarios para que sea múltiplo de 4
caracteres_faltantes = (4 - (len(resultado) % 4)) % 4
resultado += "X" * caracteres_faltantes

# Escribir el resultado en un nuevo archivo
with open('preprocesadaaqui.txt', 'w', encoding='utf-8') as salida_archivo:
    salida_archivo.write(resultado)

print("Preprocesamiento completado. El resultado se ha guardado en 'salida_preprocesada.txt'.")