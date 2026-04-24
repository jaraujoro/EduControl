import os

# Carpeta donde están tus apps
BASE_DIR = r"back\apps"

for root, dirs, files in os.walk(BASE_DIR):

    if os.path.basename(root) == "migrations":
        print(f"\nProcesando: {root}")

        for file in files:
            if file != "__init__.py":
                file_path = os.path.join(root, file)

                try:
                    os.remove(file_path)
                    print(f"  Eliminado: {file}")
                except Exception as e:
                    print(f"  Error eliminando {file}: {e}")

print("\nMigraciones limpiadas correctamente.")