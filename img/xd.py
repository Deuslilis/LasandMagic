import os

def listar_imagenes(carpeta="."):
    # Extensiones típicas de imágenes
    extensiones = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")
    rutas = []

    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith(extensiones):
            # Genera la ruta relativa para usar en tu HTML
            rutas.append(f"./{archivo}")
    return rutas

if __name__ == "__main__":
    carpeta = "img"  # cambia a "." si quieres la carpeta actual
    rutas = listar_imagenes(carpeta)
    print("Rutas de imágenes encontradas:")
    for r in rutas:
        print(r)
