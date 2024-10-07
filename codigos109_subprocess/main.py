import subprocess
import sys

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf-8'
plataform = sys.platform

if plataform == 'win32':
    encoding = 'cp850'
    cmd = ['ping', '127.0.0.1'] # fazendo a checkagem no if, nesse caso so usando 2 condição, mas caso queira checkar mais plataforma estender o if com outras condições, o else poderia ser 'sistema nao suportado'

#cp850 codificação de caracteres como utf-8, lguns tipos que pode ser usado caso utf nao funcione (cp1252, cp852, cp850)

proc = subprocess.run(
    cmd,capture_output=True,
    text=True, encoding= encoding,
)


# print(proc.args)
# print(proc.stderr)
print(proc.stdout) # pode ser usado encoding direto,  print (proc.stdout.decode('cp850'))
# print(proc.returncode)
print(sys.platform)
