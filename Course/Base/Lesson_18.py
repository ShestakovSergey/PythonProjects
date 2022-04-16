#Выполнение комманд

import subprocess

result = subprocess.run(['python3', 'Lesson_1.py'], stdout=subprocess.PIPE)
outresult = result.stdout.decode('utf-8')

print('------------------HOMEWORK----------------------')

result = subprocess.run(['date', '-v1m'], stdout=subprocess.PIPE)
outresult = result.stdout.decode()

print(outresult)
