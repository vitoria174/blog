class Admin:
      def __init__(self, nome, usuario, senha):
            self.nome = nome
            self.usuario = usuario
            self._senha = senha
            
      def autenticacao(self, usuario, senha):
           if self.usuario == usuario and self._senha == senha:
                 print('Bem vindo')
           else:
                 return f'Erro'