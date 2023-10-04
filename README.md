Este repositorio está creado con el fin de realizar un desafío de Latam para llevar a cabo un análisis de los tweets publicados en cierto período de tiempo. El repositorio contiene 3 documentos:

1. tweets.json.zip: Es el documento que contiene la información a analizar.

2. challenge_latam.ipynb: Es un archivo Jupyter Notebook que contiene los resultados y análisis de cada problema propuesto en el desafío.

3. modulo_funciones_latam.py: Es un archivo .py que utilicé como módulo en Jupyter para poder realizar el análisis de memoria (nota: las funciones que están en el documento son las mismas que estan en "challenge_latam.ipynb", lo hice de esa manera ya que tuve problemas de compatibilidad con Jupyter al utilizar directamente la librería memory_profile en el mismo script).


Conclusiones del desafio.-

Ejercicio 1

Respecto al tiempo se puede observar en el resultado que la mayor cantidad de tiempo que demora es en la lectura del archivo como tal, podria mejorar los tiempos cambiando la información a alguna bbdd no relacional como mongodb que permita aumentar la velocidad de procesamiento.

Con respecto a la memoria se observa que la mayor cantidad de memoria que se utiliza es al momento de cargar el archivo.json a un dataframe, se podria reducir la cantidad de memoria utilizada leyendo de manera particionada la data del archivo.

Ejercicio 2 y 3

Creo que la forma de diseño que tienen estas funciones son bastantes optimas respecto a tiempo y memoria
