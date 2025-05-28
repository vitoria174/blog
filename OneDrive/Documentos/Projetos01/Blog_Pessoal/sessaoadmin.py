from datetime import date
import os
import json

data_hj = date.today()
arquivo = 'arquivos.json'

class Artigos:
      
      def __init__(self):
            self.artigos = self.carregar_artigos()
            
      def carregar_artigos(self):
            if not os.path.exists(arquivo):
                  with open(arquivo, 'w') as file:
                        json.load(file)
            else:
                  return []
            
      def dump_arquivo(self):
            try:
                  with open (arquivo, 'w') as file:
                        json.dump(self.artigos, file, indent= 4)
            except:
                  return f'erro'
      
      def carregar_arquivo():
            try:
                  with open(arquivo, 'w') as file:
                        json.load(file)
            except:
                  return f'erro'
            
      def criar_artigo(self):
            
            self.carregar_artigos()
            
            titulo = input('Titulo:')
            data = data_hj
            descricao = input('Descricao:')
            
            artigo ={
                  'id':len(self.artigos)+1,
                   "data":str(data),
                   'titulo': titulo,
                   'Descricao':descricao
                   }
      
            self.artigos.append(artigo)
            self.dump_arquivo()
            
      def listar_artigo(self):
            sel
                  
      def update_artigo(self):
            id = int(input('id: '))
            
            for i in self.artigos:
                  if i['id'] == id:
                              titulo = input('Titulo: ')
                              descricao = input('Descricao: ')
                              data = str(data_hj)

                              i['titulo']=titulo
                              i['Descricao'] = descricao
                              i['data'] = data
      
      
