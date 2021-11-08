from subprocess import Popen, PIPE
from random import randint
#
p = Popen(['a.exe'], shell=True, stdout=PIPE, stdin=PIPE)
for ii in range(40):
    print(ii)
    p = Popen(['a.exe'], shell=True, stdout=PIPE, stdin=PIPE)

    value0 = str(ii) + '\n'
    value0 = bytes(value0, 'UTF-8')  # Needed in Python 3.

    value1 = str(randint(0, 100)) + '\n'
    value1 = bytes(value1, 'UTF-8')  # Needed in Python 3.
    value2 = str(randint(-100, 0)) + '\n'
    value2 = bytes(value2, 'UTF-8')  # Needed in Python 3.

    p.stdin.write(value0)
    p.stdin.write(value1)
    p.stdin.write(value2)
    p.stdin.flush()
    # result = p.stdout.readline().strip()
    # print("c++ result: " + str((result)))
    # print("python result: " +str(float(value1) + float(value2)))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")