import builtins
import json # JavaScript Object Notatiom
# importando o modulo de telas
#from Telas import Telas

class GravaDados:
    
    # um atributo ou variavel vazia {GLOBAL}
    usuariosJson = None
    tela = Telas()

    def __init__(self):
        self.carregaJson()
    
    def carregaArquivo( self ):
    
        with builtins.open("C:\\Users\\matheus.ctinti\\OneDrive - SENAC - SP\\Área de Trabalho\Python VS\\lanchonete-python\\texto.txt", "r") as dados:
            for linha in dados:
                print( linha.rstrip() )
                
    def carregaJson( self ):
        with open("C:\\Users\\matheus.ctinti\\OneDrive - SENAC - SP\\Área de Trabalho\\Python VS\\lanchonete-python\\usuarios.json", "r") as dados:          
            
            # recuperandoos dados do json 
            dadosJson = json.load( dados )
            
            # retornamos os dados para que outra função utilize de forma direta 
            self.usuariosJson = dadosJson
    
            #print(f"Usuario: {dadosJson[1]["loginArmazenado"]) e a
            #senha { dadosJson[0]["senhaArmazenada"]} ")
            
    def cadastraUsuario( self, novoUsuario ):
    # pegamos os dados da variavel global
        usuariosCadastrados = self.usuariosJson

        # salva o novo usuario no vetor
        usuariosCadastrados.append( novoUsuario )

    #  abrir o arquivo json e escrevemos dados atualizados nele 
        with open("C:\\Users\\matheus.ctinti\\OneDrive - SENAC - SP\\Área de Trabalho\Python VS\\lanchonete-python\\usuarios.json", "w") as dados:
            
            # coloca os dados em formato json
            json.dump(usuariosCadastrados, dados )
            # fecha o arquivo
            dados.close()

            # exbir a tela da classe telas ()
            self.tela.mensagemSistema(" Cadastro Realizado com sucesso!!")

    def recuperaUsuario(self, buscar ):
        # busca o item do arquivo json escolhido
        # a programação executa apenas 1 item por vez, para processar mais itens usamos um laço de repetição - for
        for i, item in enumerate( self.usuariosJson  ):
        # vamos comparar o nome de usuario para o filtro
            if item["loginArmazenado"] == buscar:
                return item 
            else:
                # se não achou nada retorna nenhum usuario encontrado
                self.tela.mensagemSistema("Nenhum usuário encontrado!")    
                break

# teste = Testes() 


# escolhido = teste.recuperaUsuario(" cliente")


# print( escolhido )

# novoUsuario = {
# "loginArmazenado" : "matheus",
# "senhaArmazenada" : "1234",
# "nomeUsuario" : "Matheus Tinti"
# }

# teste.cadastraUsuario( novoUsuario )