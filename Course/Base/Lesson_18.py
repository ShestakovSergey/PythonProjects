import subprocess
import io

sp = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True)
out = io.TextIOWrapper(sp.stdout, encoding='Windows-1251')

s = ' '
while s:
    s = out.readline()
    print(s)
