# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

import pandas as pd
import os

def creacion(carpeta_entrada, archivo_salida):
    datos = []
    for sentimiento in ['positive', 'negative', 'neutral']:
        ruta_sentimiento = os.path.join(carpeta_entrada, sentimiento)
        if os.path.exists(ruta_sentimiento):  
            for nombre_archivo in os.listdir(ruta_sentimiento):
                if nombre_archivo.endswith('.txt'):
                    with open(os.path.join(ruta_sentimiento, nombre_archivo), 'r') as archivo:
                        frase = archivo.read().strip()
                        datos.append({'phrase': frase, 'target': sentimiento})
    
    df = pd.DataFrame(datos)
    df.to_csv(archivo_salida, index=False)

# Crear el directorio de salida si no existe
os.makedirs('files/output', exist_ok=True)

# Crear train_dataset.csv
creacion('files/input/train', 'files/output/train_dataset.csv')

# Crear test_dataset.csv
creacion('files/input/test', 'files/output/test_dataset.csv')