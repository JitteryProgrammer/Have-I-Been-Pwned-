
# Código

#importação das bibliotecas
import hashlib
import requests

# função para verificar se a senha foi vazada
def verificar_senha_vazada(senha):
    # criptografando a senha
    criptografia = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
    # criando o cabeçalho
    cabecalho = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # url para verificar se a senha foi vazada
    url = 'https://api.pwnedpasswords.com/range/' + criptografia[:5]
    # fazendo a requisição
    response = requests.get(url, headers=cabecalho)
    # pegando os dados
    hash_senhas = response.text.splitlines()
    # percorrendo os dados
    for line in hash_senhas:
        # separando a senha
        senha_hash, ocorrencias = line.split(':')
        # verificando se a senha vazada é igual a senha do usuário
        if senha_hash == criptografia[5:]:
            # retornando a quantidade de vezes que a senha foi vazada
            return ocorrencias 
    # retornando 0 caso a senha não tenha sido vazada
    return 0

# solicitando a senha ao usuário
senha = input('Informe a senha a ser verificada: ')

# verificando se a senha foi vazada
ocorrencias = verificar_senha_vazada(senha)

# imprimindo o resultado
if ocorrencias == 0:
    print('A senha não foi vazada.')
else:
    print(f'A senha foi vazada {ocorrencias} vezes.')
