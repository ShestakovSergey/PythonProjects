import subprocess

result = subprocess.run(['date', '-v1m'], stdout=subprocess.PIPE)
outresult = result.stdout.decode()

print(outresult)
