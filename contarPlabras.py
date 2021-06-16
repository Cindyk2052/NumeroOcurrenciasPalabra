from collections import Counter

def frecuencia(archivo):
	try:
		with open(archivo,'r', encoding = 'utf-8') as f:
			contenido = f.readline()
			palabras = contenido.split()
			return Counter(palabras)
	except FileNotFoundError:
		print("Archivo no encontrado.")

nombre_archivo = 'fragmento.txt'
conteo = frecuencia(nombre_archivo)
print(conteo)


