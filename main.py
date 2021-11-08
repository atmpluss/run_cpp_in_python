from subprocess import Popen, PIPE
from random import randint

p = Popen(['a.exe'], shell=True, stdout=PIPE, stdin=PIPE)
for ii in range(10):
    value = str(randint(0, 10)) + '\n'
    value = bytes(value, 'UTF-8')  # Needed in Python 3.
    value2 = str(randint(0, 10)) + '\n'
    value2 = bytes(value2, 'UTF-8')  # Needed in Python 3.


    p.stdin.write(value)
    p.stdin.write(value2)
    p.stdin.flush()
    result = p.stdout.readline().strip()
    print("c++ result: " + str(float(result)))
    print("python result: " +str(float(value) + float(value2)))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")