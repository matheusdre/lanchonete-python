class Usuario:
  """
  Documentação da Classe no Python
  Funções do usuário padrão da lanchonete
  """
  # propriedade da classe (variáveis)
  #cadeia - string - str - "texto 1234" "1234"
  loginInformado:str = "cliente"
  senhaInformada:str = "1234"

  # Array - matriz ou vetor nomeado
  dadosUsuarios = {
      "loginArmazenado" : "cliente",
      "senhaArmazenada" : "1234",
      "nomeUsuario" : "joão dos santos",
    }

  # Método Construtor: executado ao instanciar a classe
  # self refere-se à instância da classe
  #propriedades são variáveis da classe

  #Método construtor
  def __init__( self ):

  #chamando o método logar da classe
   self.logar()

  def logar( self ):

    self.loginInformado = input( " Informe o login: \n")
    self.senhaIformado = input ("Iforme a senha : \n")
    #Comparação - Condicionais - Se - If
    #senão - else - falso
    if self.loginInformado == self.dadosUsuarios["loginArmazenado"]:
      self.monstraMensagens(" Bem Vindo ao sistema ")
      self.exibirInfosDoUsuario
    else:
      print("Falha ao se conectar, tente novamente")

  def sair( self ):
    print( "Logout do sistema" )

  def exibirInfosDoUsuario ( self ):
    print("Os Dados do usuário são: \n Nome: \n login :")

  def monstraMensagens(self, mensagem ):
    """ Exibi as mensagens enviadas pelo parâmetro
    """    
    print( f"-------------------- \n")
    print( f"| {mensagem} |\n ")
    print( f" -------------------- \n")


# Uma classe convencional precisa ser Instanciada para que seus objetos possam ser usados.
# Instanciar uma classe é colocar uma cópia ( instância ) em uma variável ( objeto )
#instanciar a classe (usá-lá)
#objeto da classe
# operador de atribuição =
#atendente = Usuario() # objeto da classe

#sair do sistema
#atendente.sair()