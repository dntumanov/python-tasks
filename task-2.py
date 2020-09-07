import re
import os

files: list = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']
data: list = []

path: str = 'supp_files/task-2'

for file in files:
    if re.search('.txt', file):
        data.append(file)
print(data)

# Если бы работал с каталогом
data: list = [file for file in os.listdir(path) if file.endswith('.txt')]
print(data)


