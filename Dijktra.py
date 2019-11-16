# coding: UTF-8
__author__ = 'Steeve'
__version__ = '1.0.0'

class GenericAplication:  

    def __getVizinhaza(self, listaresta, inVertice):
        objVizinhos = []
        for la in listaresta:                    
            if la['orig'] == inVertice:                        
                objVizinhos.append(la['dest'])
            elif la['dest'] == inVertice:
                objVizinhos.append(la['orig'])  
        return objVizinhos
    
    def __orderBy(self, obj):        
        # Insertion Sort para ordenar o objeto
        for p in range(0, len(obj)):
            current_element = obj[p]
            while p > 0 and obj[p - 1] > current_element:
                obj[p] = obj[p - 1]
                p -= 1
            obj[p] = current_element
        return obj[p]

    def __findCusto(self, verta, vertb, listaresta):        
        for lta in listaresta:
            if lta['orig'] == vertb and lta['dest'] == verta:
                return lta['valr']
            elif lta['orig'] == verta and lta['dest'] == vertb:
                return lta['valr']                
        return None

    def __findNextvertice(self, objDijktra):
        print(objDijktra)        
        objDijktra = sorted(objDijktra, key=lambda k: k['custo'], reverse=False)
        
        for obj in objDijktra:# Como ele vai estar ordenado o primeiro que nao estiver visitado e nao for infinito ou none ele ja me retorno o proximo
            if obj['custo'] != "" and obj['visitado'] == False:
                return obj['vertice']
        return None

    
    def __updateobjDijktra(self, objDijktra, custofind,  vorigem, vupdate):        
        for ind in range(len(objDijktra)):
            if objDijktra[ind]['vertice'] == vupdate:
                if objDijktra[ind]['custo'] == "" or objDijktra[ind]['custo'] > custofind:
                    objDijktra[ind]['custo'] = custofind 
                objDijktra[ind]['vindo'] = vorigem

    def run(self):        
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
                # nomearquivo = input('Informe o nome do arquivo :')
                # fileData = open(nomearquivo+'.txt', 'r')                                
                fileData = open('data.txt', 'r')
                lines  = fileData.readlines()
                if entrada == 'L' or entrada == 'l':                
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
                    objVizinhos = self.__getVizinhaza(listaresta, inVertice)
                    if len(objVizinhos)>0:
                        print('\n')
                        print('Conjunto vininhança de ',inVertice)
                        for vz in objVizinhos:
                            print('======> ',vz)
                        print('\n')
                elif entrada == 'S' or entrada == 's':          
                    objGraus = []
                    for i in range(int(lines[0])):
                        indice = i+1
                        vertice = lines[indice].strip()                                                
                        objViz = self.__getVizinhaza(listaresta, vertice)                        
                        if len(objViz)>0:
                            objGraus.append(len(objViz))

                    if len(objGraus) > 0:                        
                        print('\n')
                        self.__orderBy(objGraus)
                        print('Sequencia de grau do grafo :'+str(objGraus))
                        print('\n')

                elif entrada == 'D' or entrada == 'd':
                    objDijktra = []
                    vorigem = input('Informa o vertice de origem: ')
                    vdestino = input('Informar o vertice de destino: ')

                    # 1 acha ele no vertice
                    # 2 coloca ele como visitado verdadeiro 
                    # 3 Acha as vizinhanza dele

                    # Monta a tabela inicial para o algoritmo dijtra
                    for i in range(int(lines[0])):
                        indice = i+1
                        vertice = lines[indice].strip()
                        objDijktra.append({
                            "visitado": False,
                            "vertice": vertice,
                            "custo": "",
                            "vindo": ""
                        })
                    # Perrcorre para ver se o vertice existe
                    idc = 0     
                    vnextvertice = None                    
                    for ver in objDijktra:
                        objViz = []
                        
                        if ver['vertice'] == vorigem:
                            objDijktra[idc]['visitado'] = True # Indica que ja for visitado e procuramos o conjunto vizinhaza dele    
                            objViz = self.__getVizinhaza(listaresta, vorigem) # procua os conjuntos vizinhanza
                            self.__orderBy(objViz)    

                            for ind in range(len(objViz)):                                                                      
                                custofind = self.__findCusto(vorigem, objViz[ind], listaresta)
                                self.__updateobjDijktra(objDijktra, custofind, vorigem, objViz[ind])
                            
                            vorigem = self.__findNextvertice(objDijktra)
                            print(vorigem)
                        idc += 1
                    print(objDijktra)                  
                else:
                    print("Opção invalido !")


if __name__=='__main__':
    GenericAplication().run()                                