from admin import Admin
from sessaoadmin import Artigos

adm = Admin()
artigo = Artigos()

def admin():
      usuario = input('usuario: ')
      senha = input('senha: ')
      validacao = adm.autenticacao(usuario,senha)
      
      if validacao == True:
            print('1- criar artigos')
            print('2- atualizar artigo')
            print('3- deletar artigo')
            
            opcao = int(input('opcao: '))
            if opcao == 1:
                  artigo.criar_artigo()
                  artigo.visualiza()
            if opcao == 2:
                  artigo.update_artigo()
            
      else:
            print('erro')
            
def visitante():
      artigo.visualiza()

while True:
      print('1- admin')
      print('2- visitante')
      
      op = int(input('Opção: '))
      
      if op == 1:
            admin()
      if op == 2:
            pass
      if op == 0:
            break
      
