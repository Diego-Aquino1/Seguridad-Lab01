def calcular_frecuencia(texto):
    frecuencias = {}
    for caracter in texto:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

def imprimir_frecuencias_top5(frecuencias, archivo_salida):
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    top5_frecuencias = []
    for i, (caracter, conteo) in enumerate(frecuencias_ordenadas[:5], 1):
        top5_frecuencias.append((caracter, conteo))
        
    archivo_salida.write("\n")
    archivo_salida.write("Caracteres con mayor frecuencia:\n")
    for caracter, conteo in top5_frecuencias:
        archivo_salida.write(f"'{caracter}': {conteo}\n")

with open('HERALDOSNEGROSpre.txt', 'r', encoding='utf-8') as archivo_entrada:
    contenido = archivo_entrada.read()

frecuencias = calcular_frecuencia(contenido)

frecuencias_formateadas = ""
for caracter, conteo in frecuencias.items():
    frecuencias_formateadas += f"'{caracter}': {conteo}, "

with open('frecuencia.txt', 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write(frecuencias_formateadas)
    imprimir_frecuencias_top5(frecuencias, archivo_salida)

print("Operación completada. Resultados guardados en 'frecuencia.txt'.")