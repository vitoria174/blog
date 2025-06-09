from datetime import datetime


class Article:
      def __init__(self):
            self.article = []
      
      #criar um artigo      
      def create_article(self,title,description):
            
            article = {
                  'id':len(self.article)+1,
                  'data':str(datetime.now().date()),
                  'title':title,
                  'description':description
            }
            
            return article
      
      #leitura de artigo      
      def read_article(self):
            print('-----lISTA ARTIGOS-----')
            print('ID \t',end=' ')
            print('Titulo\t',end=' ')
            print('Descrição \t',end=' ')
            print('Data \t')
            for article in self.article:
                  print(f'{article['id']}\t',end=' ')
                  print(f'{article['title']}\t', end=' ')
                  print(f'{article['description']}\t', end=' ')
                  print(f'{article['data']}\t',end=' ')
                  print()
            return self.article
      
      #atualiza os artigos criados
      def update_article(self):                 
            update_id = int(input('Atualiar por Id: '))
            
            for c, i in enumerate(self.article):
                  if i['id'] == update_id:
                        new_title = input('titulo: ')
                        new_description = input('Descricao: ')
                        i['title']=new_title
                        i['description']=new_description
                        i['data']=str(datetime.now().date())
                        print('Artigo atualizado')
                 
                  
                        
      def delete_artigo(self):
            delete_for_id =int(input('Deletar por ID: '))
            
            for indice, article in enumerate(self.article):
                  if article['id'] == delete_for_id:
                        del self.article[indice]
                        
