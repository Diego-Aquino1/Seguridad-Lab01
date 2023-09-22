# Leer el archivo de entrada
with open('HERALDOSNEGROSpre.txt', 'r', encoding='utf-8') as entrada_archivo:
    contenido = entrada_archivo.read()

# Mostrar cada carácter en su representación UTF-8 (en hexadecimal)
for caracter in contenido:
    print(f"Carácter: {caracter}, Valor UTF-8: {ord(caracter):04x}")

# Abrir el archivo de salida para escritura
with open('UNICODE_8.txt', 'w', encoding='utf-8') as salida_archivo:
    # Iterar sobre el contenido y escribirlo en el archivo de salida
    for caracter in contenido:
        salida_archivo.write(f"{ord(caracter):04x}")