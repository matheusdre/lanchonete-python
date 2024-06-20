import builtins
import json # JavaScript Object Notatiom

class Testes:
    
    def carregaArquivo( self ):
    
        with builtins.open("C:\\Users\\matheus.ctinti\\OneDrive - SENAC - SP\\Área de Trabalho\Python VS\\lanchonete-python\\texto.txt", "r") as dados:
            for linha in dados:
                print( linha.rstrip() )
                
    def carregaJson( self ):
        with open("C:\\Users\\matheus.ctinti\\OneDrive - SENAC - SP\\Área de Trabalho\\Python VS\\lanchonete-python\\usuarios.json", "r") as dados:          
            # recuperandoos dados do json 
            dadosJson = json.load( dados )
            
            print( dadosJson[1]["loginArmazenado"])
            
teste= Testes() 
teste.carregaJson()                