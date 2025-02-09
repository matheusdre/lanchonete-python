#importando a classe Time do próprio Python
import time
import os
import json

class Telas:

    

    def entradaSistema( self ):
        
        self.limpaConsole

        print( f"+-------------------------------------------------------+" )
        print( f"|                                                                                   |" )
        print( f"|          ** Seja bem vindo ao sistema **                                               |" )
        print( f"|                                                                                   |" )
        print( f"+-------------------------------------------------------+" )

        self.esperaLimpa( )
            
        
    def esperaLimpa( self,tempo = 3 ):
        # esperar - delay Xsegundos
        time.sleep( tempo ) 
        
        # limpar a tela
        self.limpaConsole()
        
    def saidaSistema( self ):
        print( f"+-------------------------------------------------------+" )
        print( f"|                                                                                   |" )
        print( f"|            ** Obrigado por usar o Sistema **                                                 |" )
        print( f"|                                                                                   |" )
        print( f"+-------------------------------------------------------+" )

        self.esperaLimpa()
        return False

    def mensagemSistema( self, mensagem ):
        print( f"+-------------------------------------------------------+" )
        print( f"|                                                                                   |" )
        print( f"  ** {mensagem} **                                                |" )
        print( f"|                                                                                   |" )
        print( f"+-------------------------------------------------------+" )  

    def limpaConsole( self ):   
        
        if os.name == "nt": # windows nt - linux posix - Mac darwin
            os.system(" cls ")    
        else:
            os.system (" clear ")
    
    def InfosUsuarios( self, usuario ):              
        print( f"+-------------------------------------------------------+" )
        print( f"|  * Bem Vindo { usuario }           |" )
        print( f"|  * Menu - Escolha uma Opção:                          |" )
        print( f"|  1 - Cadastrar                                        |" )
        print( f"|  2 - Listar                                           |" )
        print( f"|  0 - Sair                                       |" )
        print( f"+-------------------------------------------------------+" )     

        while True:
        # convertemos para inteiro  string do input
            escolha = int(input("Digite a sua escolha:"))

            if escolha == 1:
                nome = input("Informe o nome do funcionário:")
                user =input("Informe o usuário:")
                senha = input("1234")

            # vetor com os dados cadastrados
                novoUsuario= { "loginArmazenado":{ user },
                        "senhaArmazenado" :{ senha },
                        "nomeUsuario"  : { nome }
                }

                #jsonManual = "{
            #   \"loginArmazenado\":\"\"
                #}"

    # enviar para o armazenamento
    with open("C:\\Users\\matheus.ctinti\\OneDrive - SENAC - SP\\Área de Trabalho\\Python VS\\lanchonete-python\\usuarios.json", "r+") as dados:
        
        dadosJson = json.load( novoUsuario )

        json.dump( novoUsuario, dados,indent=4)


        dados.close()

        self.mensagemSistama("Cadastro Realizado com sucesso!")


        self.infosUsuario( usuario )

        # if os.name == "nt": # windows nt - Linux posix - Mac darwin            
        #     os.system("cls")
        # elif os.name == "darwin":
        #     os.system (" clear ")
        # else: 
        #     os.system("clear")   
        
        # tipoSistema = os.name
        # switch( tipoSistema ):
        #     case "nt":
        #         os.system("cls")
        #         break: