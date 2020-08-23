import sys, threading
from hack import *
from time import *

processo = "zsnes" if sys.platform == 'linux' else "zsnesw.exe"
hackMario = hack(processo)

while True:
    hackMario.fixarStatusPenaMario()
    hackMario.valorfixoMoedas()
    sleep(0.5)
