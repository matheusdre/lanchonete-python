import builtins

class GravaDados:
    
    usuarioCadastrados = {
     "loginArmazenado" : "cliente",
    "senhaArmazenada" : "1234",
    "nomeUsuario" : "João dos Santos",
  }
    
    def salvaDados( self ):
        #open( nomeArquivo,modoAbertuta) é uma função do python3 que lê e escreve arquivos
        # w - write - escrita
        # r - read - leitura
        # r+ - escrita/leitura
        
        with open("Lanchonete-python\\Modulos\\dados.txt","w") as dados:   
            dados.write(self.usuarioCadastrados)
            dados.close()
            print("Dados armazenado")  
        
            
    def leDados( self ):
        # para ler usamos a classe builtins do python3
        with builtins.open("Lanchonete-python\\Modulos\\dados.txt","r") as dados: 
                
            print(f"No arquivo temos: \n ")
            
            # for é um laço de repetição
            # para cada linha do arquivo de texto 
        for linha in dados.readlines() :
                print( linha.rstrip() )
                
    def exportaDados( self ):
        print("")
        
dados = GravaDados()      
dados.salvaDados()      
dados.LeDados()      
