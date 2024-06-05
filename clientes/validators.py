import re
from validate_docbr import CPF
def cpf_valido(numero_do_cpf):
    cpf = CPF()
    numero_do_cpf = numero_do_cpf.replace('.', '')
    return cpf.validate(numero_do_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    # Veriicar se o celular é vadido ( 86 999960-5877 )
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.match(modelo, numero_do_celular)