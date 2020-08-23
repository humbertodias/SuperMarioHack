import sys
from Enderecos import *

if sys.platform == 'linux':
    from gerenciadorDeMemoriaLinux import gerenciadorDeMemoria
else:
    from gerenciadorDeMemoriaWindows import gerenciadorDeMemoria

class hack(object):

    gerenciadorDeMemoria = None
    vidaAoPegarMoeda = None
    def __init__(self,nomeProcesso):
        self.gerenciadorDeMemoria = gerenciadorDeMemoria(nomeProcesso)
        self.vidaAoPegarMoeda = False
        self.fixarStatusMario = False
        pass

    def fixarStatusPenaMario(self):
        statusMarioAgora = self.gerenciadorDeMemoria.lerByte(STATUSMARIO)
        print("statusMarioAgora:%s" % statusMarioAgora)
        if (statusMarioAgora != MARIO_PENINHA):
            self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,MARIO_PENINHA.to_bytes(1,byteorder='little'))

    def valorfixoMoedas(self):
        valorPadraoDeMoedas = 99
        quantidadeAtualDemoedas = self.gerenciadorDeMemoria.lerByte(MOEDAS)
        print("quantidadeAtualDemoedas:%s" % quantidadeAtualDemoedas)
        if (quantidadeAtualDemoedas!=99):
            self.gerenciadorDeMemoria.escreverByte(MOEDAS,valorPadraoDeMoedas.to_bytes(1,byteorder='little'))
