Projeto 1: Cadastre-me!

O objetivo desse projeto foi criar um programa de login que deverá obter informações do usuário.

Para começar, importei o módulo datetime para trazer a data atual para o projeto e o random para sortear aleatoriamente um valor da lista que irei criar.

Criei uma variável com input de nome e idade para o programa receber os dados do usuário e outra que receberá automaticamente a data atual vindo do datetime.

Criei a variável com a lista dos valores para o sorteio e outra que irá ficar o valor já sorteado através do random.choices

Depois criei a última variável do projeto com um input para o funcionário inserir sua data de aniversário. Esse valor que o usuário inseriu seria uma string, e para trabalhar com datas converti essa string usando datetime.strptime e depois especifiquei o formato desejado da data com '%d/%m/%Y'.

Por fim, fiz a apresentação do usuário com todos os dados inseridos anteriomente usando uma função dentro da string para retomar as variáveis que foram inseridas. Para especificar o dia do registro eu "quebrei" partes da data atual e imprimi apenas as partes que são necessárias.
