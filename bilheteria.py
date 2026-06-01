#aluno1: Formato do nome do filme
def formatar (nome):
    return nome.upper()
#aluno2: Verificação de Acesso
def verificador(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não autorizado"
#aluno3: Mensagem de retorno
def gerar_mensagem(status):
    if status == "autorizado":
        return "tenha uma otima sessão"
    else:
        return "sinto muito, idade não autorizada"
#aluno4: Integrador do projeto
nome_filme = input("Digite o nome do filme:")
idade_filme = int(input("Digite a sua idade"))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(f"\nfilme:{filme}")
print(f"status:{status_final}")
print(f"Aviso:{mensagem}")
        