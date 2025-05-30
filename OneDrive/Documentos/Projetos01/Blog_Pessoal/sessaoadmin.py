from datetime import date
import os
import json

data_hj = date.today()
arquivo = 'arquivos.json'

class Artigos:
      
      def __init__(self):
            self.artigos = self.arquivo_json()
            
      def arquivo_json(self):
            if os.path.exists(arquivo):
                  with open(arquivo, 'r') as file:
                        try:
                              return json.load(file)
                        except json.JSONDecodeError:
                              return []
            else:
                  with open(arquivo, 'r') as file:
                        json.dump([], file)
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
            
            self.arquivo_json()
            
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
      
      def visualiza(self):
            for i in self.artigos:
                  print
                  
                  
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
      
      
