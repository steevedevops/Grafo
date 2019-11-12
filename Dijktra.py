# coding: UTF-8
__author__ = 'Steeve'
__version__ = '1.0.0'

class GenericAplication():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def run(self):
        print('Aplicativo funcionando')


if __name__=='__main__':
    print('\n')
    print('              WELCOM TO DIJKTRA APLICATION            ')
    print('=====================================================')
    print('|                       MENU                        |')
    print('=====================================================')
    print('|                   L - LEITURA                     |')
    print('|                   V - VIZINHANÇA                  |')
    print('|                   S – SEQUÊNCIA DE GRAUS          |')
    print('|                   D – DIJKSTRA                    |')
    print('|                   F – FIM                         |')   
    print('=====================================================')
    while True:
        entrada = input('Selecione uma opção: ')        
        if (entrada == 'F' or entrada == 'f'):
            print("Fim do programa.")
            break
        else:
            if entrada == 'L' or entrada == 'l':                
                # nomearquivo = input('Informe o nome do arquivo :')
                # fileData = open(nomearquivo+'.txt', 'r')
                fileData = open('data.txt', 'r')
                lines  = fileData.readlines()
                
                counter = 1
                linhas = len(lines)
                qtdVertice = None
                qtdAresta = None
                listaresta = []
                for l in lines:                    
                    if counter == 1: #pega o primeiro valor que existe que sera a quantia de vertise
                        qtdVertice = l.split()[0]            
                    elif counter > int(qtdVertice)+2:
                        listaresta.append({
                            "orig" : l.split()[1],
                            "dest" : l.split()[2],
                            "valr" : l.split()[3]
                        })                       
                    counter += 1
            elif entrada == 'V' or entrada == 'v':
                inVertice = input('Informe o vertice para ver sua Vizinhança: ')
                ver = None
                objVizinhos = []
                for la in listaresta:                    
                    if la['orig'] == inVertice:                        
                        objVizinhos.append(la['dest'])
                    elif la['dest'] == inVertice:
                        objVizinhos.append(la['orig'])                        
                if len(objVizinhos)>0:
                    print('\n')
                    print('Conjunto vininhança de ',inVertice)
                    for vz in objVizinhos:
                        print('======> ',vz)
                    print('\n')
                
                        
                
                
            
        