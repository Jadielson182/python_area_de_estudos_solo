lista1 = {
    'nome': 'marcos',
    'sobrenome': 'Silva',
    'idade': 18,
}

lista2 = {
    'altura': 1.75,
    'sexo': 'Masculino'
}

pessoa = {**lista1, **lista2}
print(pessoa)

#.\venv\scripts\activate
# deactivate  desativa

# venv\scripts\python "argumento" "arumento" para ativivar codigos diretos no venve em ativar venv

# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']