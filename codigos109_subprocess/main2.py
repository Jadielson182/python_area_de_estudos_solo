import subprocess
import sys

cmd = ['ls -lah /']
encoding = 'utf-8'
plataform = sys.platform

if plataform == 'win32':
    encoding = 'cp850'
    cmd = ['ls -lah /'] # fazendo a checkagem no if, nesse caso so usando 2 condição, mas caso queira checkar mais plataforma estender o if com outras condições, o else poderia ser 'sistema nao suportado'

#cp850 codificação de caracteres como utf-8, lguns tipos que pode ser usado caso utf nao funcione (cp1252, cp852, cp850)

proc = subprocess.run(
    cmd,capture_output=True,
    text=True, encoding= encoding,
    shell=True,
)
#esse procedimento com shell e para mostra umas diferença, la em cima o comando nao foi separado, esse modo e para exibir mais coisa, mas esse comando pode nao funcionar bem no windows


# print(proc.args)
# print(proc.stderr)
print(proc.stdout) # pode ser usado encoding direto,  print (proc.stdout.decode('cp850'))
# print(proc.returncode)
print(sys.platform)
