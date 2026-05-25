#multiplas funções -- Exercicios de Qualidade
def cabecalho():
    print("/n" + "=" * 30)
    print("SISTEMA DE QUALIDADE")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
        return "APROVADA"
    else:
        return "REPROVADA"
    
    cabecalho()
    peso_item = float(input("Digite o paso do item em gramas: "))
    status = verificar_status(peso_item)
    print(f"resultado da inspeção:{status}")
    print("=" * 30)