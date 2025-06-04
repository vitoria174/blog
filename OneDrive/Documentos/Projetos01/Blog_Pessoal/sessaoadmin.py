from datetime import datetime
class Artigo:
      def __init__(self):
            self.artigos = []
            
      def criar_artigo(self):
            id = len(self.artigos) + 1
            titulo = str(input('Titulo: '))
            descricao = str(input('Descricao: '))
            
            artigo = {
                  'id':id,
                  'data':str(datetime.today()),
                  'titulo':titulo,
                  'descricao':descricao
            }
            
            self.artigos.append(artigo)
            
      def ler_artigo(self):
            print('-----lISTA ARTIGOS-----')
            for artigo in self.artigos:
                  print(f'Titulo: {artigo['titulo']}', end=' ')
                  print(f'Descricao: {artigo['descricao']}', end=' ')
                  print(f'Data: {artigo['data']}',end=' ')
                  print()
                  
      def atualizar_artigo(self):
            atualizar_id = int(input('Atualizar por ID: '))
            
            for id_artigo, conteudo_artigo in enumerate(self.artigos):
                  if atualizar_id == id_artigo+1:
                        titulo = input('titulo: ')
                        descricao = input('descricao: ')
                        data_atuaizada = str(datetime.today())
                        
                        artigo ={
                              'titulo':titulo,
                              'descricao':descricao,
                              'data':data_atuaizada
                        }
                        self.artigos[id_artigo]=artigo
                        
      def deletar_artigo(self):
            deletar_por_id = int(input('Deletar por id: '))
                  
            for id_deleta, deletar_artigo in enumerate(self.artigos):
                  if deletar_por_id == id_deleta+1:
                        del(self.artigos[deletar_por_id])
                  
                  
c = Artigo()
c.criar_artigo()
c.criar_artigo()
c.criar_artigo()
c.ler_artigo()
c.atualizar_artigo()
c.ler_artigo()
c.deletar_artigo()
c.ler_artigo()