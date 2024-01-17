## Objetivo de projeto

# * Criar um módulo de login de aplicativo

### Funcionalidades do projeto
from datetime import datetime
import random

#1. Nome do usuário
nome = input('Digite seu nome: ')

#2. Idade do usuário
idade = int(input('Agora digite sua idade: '))

#3. Registro automático da data do cadastro do usuário, usando a data do registro como data de registro
data_atual = datetime.now()
#4. Cada novo funcionário que é registrado na empresa receberá um dos seguintes cartões que é sorteado de forma aleatória:
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao = random.choice(cartoes)
#5. Informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
aniversário = datetime.strptime(
    input('Digite sua data de aniversário no formato dd/mm/aaaa: '), '%d/%m/%Y')

#6. Apresentação do usuário
print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_atual.day}/{data_atual.month}/{data_atual.year}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}!')
