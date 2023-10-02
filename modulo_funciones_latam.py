import zipfile
import json
from typing import List, Tuple
from collections import Counter
from datetime import datetime
import pandas as pd
import emoji
from memory_profiler import profile
import time
#%load_ext memory_profiler
import cProfile
from collections import defaultdict

# =============================================================================
# Ejercicio 1: Función enfocada a la memoria
# =============================================================================

@profile
def q1_memory(file_path: str) -> List[Tuple[str, int]]:
    # Lista para almacenar los datos JSON
    data = []

    # Abre el archivo ZIP
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        with zip_file.open('farmers-protest-tweets-2021-2-4.json') as json_file:
            data = [json.loads(line.decode('utf-8')) for line in json_file]    

    
    # Convierte la lista de datos en un DataFrame de Pandas
    df = pd.DataFrame(data)  
    
    # Agrupar por fecha y contar el número de tweets por fecha y usuario
    df['date'] = pd.to_datetime(df['date'])
    df['username'] = df['user'].apply(lambda x: x['username'])
    grouped = df.groupby([df['date'].dt.date, 'username']).size().reset_index(name='count')
    
    # Obtener las 10 fechas con más tweets
    top_dates = grouped.groupby('date')['count'].sum().nlargest(10).index
    
    # Obtener el usuario con más publicaciones para cada fecha
    result = []
    for date in top_dates:
        top_user = grouped[grouped['date'] == date].nlargest(1, 'count')
        result.append((date, top_user['username'].values[0]))
    return result

# =============================================================================
# Ejercicio 2: Función enfocada a extraer los emojis
# =============================================================================

def extract_emojis(text):
    emojis = set()
    for c in text:
        if c in emoji.EMOJI_DATA:
            emojis.add(c)
    return ''.join(emojis)

# =============================================================================
# Ejercicio 2: Función enfocada a la memoria
# =============================================================================

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Diccionario para almacenar los emojis y sus conteos
    start_time = time.time()  # Iniciar la medición de tiempo
    emoji_counts = Counter()

    # Abre el archivo ZIP
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        with zip_file.open('farmers-protest-tweets-2021-2-4.json') as json_file:
            for line in json_file:
                tweet = json.loads(line.decode('utf-8'))
                tweet_text = tweet.get('content', '')
                emojis = extract_emojis(tweet_text)
                emoji_counts.update(emojis)
    
    # Obtener los 10 emojis más usados
    top_emojis = emoji_counts.most_common(10)
    end_time = time.time()  # Finalizar la medición de tiempo
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    
    return top_emojis


# =============================================================================
# Ejercicio 3: Función enfocada a la memoria
# =============================================================================
@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    start_time = time.time()  # Iniciar la medición de tiempo

    user_mentions_count = defaultdict(int)

    # Abre el archivo ZIP y analiza el contenido JSON línea por línea
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        with zip_file.open('farmers-protest-tweets-2021-2-4.json') as json_file:
            for line in json_file:
                tweet = json.loads(line.decode('utf-8'))
                username = tweet.get("user", {}).get("username", "")
                mentioned_users = tweet.get("mentionedUsers", [])
                if mentioned_users is not None:
                    user_mentions_count[username] += len(mentioned_users)

    # Obtener el top 10 de usuarios con más menciones
    top_users = sorted(user_mentions_count.items(), key=lambda x: x[1], reverse=True)[:10]
    end_time = time.time()  # Finalizar la medición de tiempo
    print(f"Tiempo de ejecución q3_time: {end_time - start_time} segundos")

    return top_users