import json
import pandas as pd

datos = []
with open('datos_raw.json', 'r') as f:
    for linea in f:
        try:
            datos.append(json.loads(linea.strip()))
        except Exception:
            pass

df = pd.DataFrame(datos)
df.to_csv('datos.csv', index=False)
print(f"Archivo datos.csv creado exitosamente con {len(df)} filas.")
