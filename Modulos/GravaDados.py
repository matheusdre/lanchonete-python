import builtins
import json
class GravaDados:
    
    usuariosCadastrados = {
    "loginArmazenado" : "cliente",
    "senhaArmazenada" : "1234",
    "nomeUsuario" : "João dos Santos",
    }
    
    def salvaDados( self ):
        #open( nomeArquivo,modoAbertuta) é uma função do python3 que lê e escreve arquivos
        # w - write - escrita
        # r - read - leitura
        # r+ - escrita/leitura
        
        with open("lanchonete-python\\Modulos\\dados.txt","w") as dados:   
            # converter o vetor em json
            dadosJson = json.dumps( self.usuariosCadastrados)
            dados.write( dadosJson)
            dados.close()
            print("Dados armazenado")  
        
            
    def leDados( self ):
        # para ler usamos a classe builtins do python3
        with builtins.open("lanchonete-python\\Modulos\\dados.txt","r") as dados: 
                
            print(f"No arquivo temos: \n ")
            
            # for é um laço de repetição
            # para cada linha do arquivo de texto 
        for linha in dados.readlines() :
                print( linha.rstrip() )
   
    def adicionaCadastro( self,novoUsuario ):
        # pegamos o json no arquivo de dados
        with builtins.open("lanchonete-python\\Modulos\\dados.txt","r") as dados:
            
        # adicionado um novo item ao nosso vetor 
    
        
        # salvar novamente o arquivo
        
        
        self.usuariosCadastrados = self.usuariosCadastrados.append( novoUsuario )
            
    def exportaDados( self ):
        print("")
        
dados = GravaDados()
dados.adicionaCadastro()      
dados.salvaDados()      
dados.leDados()      
