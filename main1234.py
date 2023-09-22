# Lee el contenido del archivo
with open("text.txt", "r", encoding="utf-8") as archivo_entrada:
    texto = archivo_entrada.read()

# 1. Realizar sustituciones
texto = texto.replace("j", "i")
texto = texto.replace("h", "i")
texto = texto.replace("̃n", "n")
texto = texto.replace("k", "l")
texto = texto.replace("u", "v")
texto = texto.replace("w", "v")
texto = texto.replace("y", "z")

# Muestra la salida parcial
print("Salida parcial después de sustituciones:")
print(texto[:300])  # Muestra los primeros 300 caracteres

# 2. Eliminar tildes
import unicodedata

texto = ''.join([c for c in unicodedata.normalize('NFD', texto) if not unicodedata.combining(c)])

# Muestra la salida parcial
print("\nSalida parcial después de eliminar tildes:")
print(texto[:300])  # Muestra los primeros 300 caracteres

# 3. Convertir a mayúsculas
texto = texto.upper()

# Muestra la salida parcial
print("\nSalida parcial después de convertir a mayúsculas:")
print(texto[:300])  # Muestra los primeros 300 caracteres

# 4. Eliminar espacios en blanco y signos de puntuación
import string

caracteres_a_eliminar = string.whitespace + string.punctuation + "¡!"
texto = ''.join([c for c in texto if c not in caracteres_a_eliminar])

# Muestra la salida parcial
print("\nSalida parcial después de eliminar espacios y puntuación:")
print(texto[:300])  # Muestra los primeros 300 caracteres

# Guardar el resultado en "HERALDOSNEGROS pre.txt"
with open("HERALDOSNEGROSpre.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(texto)

print("\nOperaciones de preprocesamiento completadas. Resultado guardado en 'HERALDOSNEGROS pre.txt'.")
