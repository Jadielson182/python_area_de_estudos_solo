

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    
    def set_user(self,user):
        self.user = user


    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        Connection = cls()
        Connection.user = user
        Connection.password = password
        return Connection


    @staticmethod
    def log(msg):
        print('LOG:', msg)



Connection_1 = Connection.create_with_auth('luiz', '1234')
Connection.log('Login efetuado com sucesso')

print(Connection_1.user)
print(Connection_1.password)


# connection_2 = Connection()
# connection_2.set_user('luiz')
# connection_2.set_password('1234')

# print(connection_2.log('Mensagem de login'))
# print(connection_2.user)
# print(connection_2.password)


