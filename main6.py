import math

def encontrar_secuencias_repetidas(texto, longitud_secuencia):
    secuencias = {}
    
    for i in range(len(texto) - longitud_secuencia + 1):
        secuencia = texto[i:i + longitud_secuencia]
        if secuencia.isalpha():
            if secuencia not in secuencias:
                secuencias[secuencia] = [i]
            else:
                secuencias[secuencia].append(i)
    
    return {secuencia: posiciones for secuencia, posiciones in secuencias.items() if len(posiciones) > 1}

def encontrar_distancias(posiciones):
    distancias = []
    
    for i in range(len(posiciones)):
        for j in range(i + 1, len(posiciones)):
            distancia = posiciones[j] - posiciones[i]
            distancias.append(distancia)
    
    return distancias

def kasiski_analisis(texto, longitud_secuencia):
    secuencias_repetidas = encontrar_secuencias_repetidas(texto, longitud_secuencia)
    
    distancias = {}
    for secuencia, posiciones in secuencias_repetidas.items():
        distancias[secuencia] = encontrar_distancias(posiciones)
    
    return distancias

# Leer el archivo de entrada
with open('HERALDOSNEGROSpre.txt', 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Establecer la longitud de la secuencia a buscar (ajusta según sea necesario)
longitud_secuencia = 3

# Ejecutar el análisis de Kasiski
resultados_kasiski = kasiski_analisis(texto, longitud_secuencia)

# Imprimir las secuencias y distancias
for secuencia, distancias in resultados_kasiski.items():
    print(f"Sucesion: {secuencia}")
    print(f"Distancias: {distancias}")
    print()