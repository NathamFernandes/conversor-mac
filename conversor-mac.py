while True:
    endereco_entrada = str(input("Insira o endereço MAC: "))
    tipo =  int(input('- Windows "-" (1) \n- Intelbras "." (2) \n- HP ":" (3) \n \nInsira para qual tipo você quer converter: '))
    elementos = list(endereco_entrada)
    quantidade = len(elementos)
    nova_lista = []
    if quantidade == 17:
        if tipo == 1:
            elementos[2] = "-"
            elementos[5] = "-"
            elementos[8] = "-"
            elementos[11] = "-"
            elementos[14] = "-"
            endereco_saida = ''.join(elementos)
            print("Enderço MAC (Windows): " + endereco_saida)
            if continuar.upper == "S":
                break
        elif tipo == 2:
            elementos[2] = "."
            elementos[5] = "."
            elementos[8] = "."
            elementos[11] = "."
            elementos[14] = "."
            endereco_saida = ''.join(elementos)
            print("Enderço MAC (Intelbras): " + endereco_saida)
            if continuar.upper == "S":
                break
        elif tipo == 3:
            elementos[2] = ":"
            elementos[5] = ":"
            elementos[8] = ":"
            elementos[11] = ":"
            elementos[14] = ":"
            endereco_saida = ''.join(elementos)
            print("Enderço MAC (HP): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? S/N: "))
            if continuar.upper == "S":
                break
        else:
            print("Opção inválida. Programa encerrado.")
    else:
        print("\nSeparação inválida.\n")

