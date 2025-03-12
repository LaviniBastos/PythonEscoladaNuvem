# Função que armazena as notas dos alunos, e quando o usuário digitar 'fim'o programa exibe a quantidade de notas inseridas e calcula à média de todas


def registro_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno ou fim para sair: ")
            if entrada.lower() == 'fim':
                break
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite uma nota entres 0 e 10. ")
                continue
        except ValueError:
            print("Entrada inválida. Digite uma nota valida ou fim para sair. ")
            
    if notas:
        media = sum(notas) / len(notas)
        print(f"Media da turma {media:.2f}")
        print(f"total de notas validas registradas: {len(notas)}")
    else:
            print("Nenhuma nota registrada")
registro_notas()
