from sessaoadmin import Artigos

blog = Artigos()

def main():
      print('1- Criar Post')
      print('0- Sair')
      
      while True:
            opcao = int(input('Opção: '))
            if opcao == 1:
                  blog.criar_artigo()
            
            if opcao == 0:
                  break            
main()