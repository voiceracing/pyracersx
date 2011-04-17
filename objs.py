# -*- coding: cp1252 -*-
# objs é uma classe para guardar os atributos de todos os carros do jogo.

#   Lista de classes e uso das mesmas:
#   Objeto - tudo o que vai se mexer no cenário
#   Scenary - todos os cenarios;
#   Menu - menus de opções;
#   Scenary_obj - objetos do cenário, faixas, arvores, obstaculos etc.
#   Marker - os marcadores do gameplay como, score, level e tempo.


#Car
class Objeto:
    def __init__(self, tipo, img, baseSpeed, tam, direc, random, colorKey):
        self.__tipo = tipo           # veiculo, arvore, placa, obstaculo
        self.__img = img             # local da imagem
        self.__baseSpeed = baseSpeed # velocidade no level 1 ( 1, 1.5, 2, 2.5, 3)
        self.__tam = tam             # tamanho do veiculo (x,y)
        self.__direc = direc         # direção (up, down)
        self.__random = random       # True or False (True usualmente para veiculos na contra mão)
        self.__colorKey = colorKey   # Coordenada RGB para o pygame (usualmente, (0,0,0))

    #Gets
            
    def getTipo(self):
        return self.__tipo
    def getImb(self):
        return self.__img
    def getBaseSpeed(self):
        return self.__baseSpeed
    def getTam(self):
        return self.__tam
    def getDirec(self):
        return self.__direc
    def getRandom(self):
        return self.__random
    def getColorKey(self):
        return self.colorKey

    # Sets

    def setTipo(self,tipo):
        self.__tipo = tipo
    def setImg(self,img):
        self.__img = img
    def setBaseSpeed(self,baseSpeed):
        self.__baseSpeed = baseSpeed
    def setTam(self,tam):
        self.__tam = tam
    def setDirec(self,direc):
        self.__direc = direc
    def setRandom(self,random):
        self.__random = random
    def setColorKey(self,colorKey):
        self.__colorKey = colorKey

class Scenary:
    
    def __init__(self, nome, img, scorexy, levelxy, timexy):
        self.__nome = nome
        self.__img = img
        self.__scorexy = scorexy
        self.__levelxy = levelxy
        self.__timexy = timexy
        self.__objetos = []             # todos os objetos do cenário devem estar nesta lista para aumentar as velocidades constantemente

    #Gets
            
    def getNome(self):
        return self.__nome
    def getImb(self):
        return self.__img
    def getScorexy(self):
        return self.__scorexy
    def getLevelxy(self):
        return self.__levelxy
    def getTimexy(self):
        return self.__timexy
    def getObjetos(self):
        return self.__objetos

    #Sets

    def setNome(self,nome):
        self.__nome = nome
    def setImg(self, img):
        self.__img = img
    def setScorexy(self, scorexy):
        self.__scorexy = scorexy
    def setLevelxy(self, levelxy):
        self.__levelxy = levelxy
    def setTimexy(self, timexy):
        self.__timexy = timexy

    #inserir objetos - o programa teoricamente deixa colocar dois objetos com mesmo nome, o que da problema na hora de remover
    def insObjeto(self, objeto):
        self.__objetos.append(objeto)

    #remover objetos - Função não testada
    def remObjeto(self, objeto):
        self.__objetos.remove(objeto)

    
                
                
            
        
