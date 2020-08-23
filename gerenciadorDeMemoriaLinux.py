import ptrace.debugger
from ptrace.linux_proc import *  # For the searchProcessByName func
from ptrace.binding import *     # For ptrace funcs
from datetime import datetime
import time

class gerenciadorDeMemoria(object):

    pid = 0
    process = None

    def __init__(self,nomeProcesso):
        self.pid = searchProcessByName(nomeProcesso)
        self.conectarProcesso()

    def conectarProcesso(self):
        self.process = ptrace.debugger.PtraceDebugger().addProcess(self.pid, False)

    def lerByte(self,endereco):
        print('%s - lerByte: %s' % (datetime.now(), hex(endereco)) )
        bytes = self.process.readBytes(endereco,1)
        return int.from_bytes(bytes, byteorder='little')


    def escreverByte(self,endereco,valor):
        print('%s - escreverByte: %s' % (datetime.now(), hex(endereco)) )
        self.process.writeBytes(endereco, valor)
        self.process.cont()
        pass
        