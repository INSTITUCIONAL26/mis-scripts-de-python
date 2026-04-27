import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def seleccionar_y_procesar_imagen():
    # 1. Crear una ventana oculta de Tkinter para que no moleste
    root = tk.Tk()
    root.withdraw()
    
    # Abrir el seleccionador de archivos de Windows
    print("Selecciona una imagen en la ventana emergente...")
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona una imagen JPG",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
    )
    
    # Verificar si el usuario seleccionó algo o canceló
    if not ruta_archivo:
        print("No seleccionaste ninguna imagen.")
        return

    # 2. Convertir la imagen en un array y renderizar
    try:
        # Cargar
        img = Image.open(ruta_archivo)
        
        # Convertir a Array
        img_array = np.array(img)
        
        # Mostrar información en consola
        print(f"Imagen cargada desde: {ruta_archivo}")
        print(f"Dimensiones del array: {img_array.shape}")
        
        # Renderizar
        plt.imshow(img_array)
        plt.title(f"Renderizado MODO #2\n{ruta_archivo.split('/')[-1]}")
        plt.axis('off')
        plt.show()
        
    except Exception as e:
        print(f"Ocurrió un error al procesar la imagen: {e}")

# Ejecutar el método
seleccionar_y_procesar_imagen()