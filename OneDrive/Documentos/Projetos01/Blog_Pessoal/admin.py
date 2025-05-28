class Admin:
      def __init__(self):
            self.nome = 'admin'
            self.usuario = 'adimn'
            self._senha = '12345'
            
      def autenticacao(self, usuario, senha):
           if self.usuario == usuario and self._senha == senha:
                 return True
           else:
                 return print(f'Erro! Login ou senha incorretos.')
           