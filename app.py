import os

#função para exibir o nome do programa
def exibir_nome_do_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""𝕮𝖆𝖉𝖆𝖘𝖙𝖗𝖔 𝕯𝖊 𝕬𝖑𝖚𝖓𝖔𝖘""") 

#função do calculo das medias das notas
def calcular_media(notas):
    return sum(notas)

#função para cadastrar o aluno
def cadastrar_aluno(alunos):
    os.system
    print('Cadastrar Alunos\n')
    nome_aluno = input('Digite o nome do aluno: ')
    idade_aluno = input ('Digite a idade do aluno: ')
    notas = []
    for i in range( 1, 4):
        nota = float(input(f'Digite a nota {i} do aluno: '))
        notas.append(nota)
    media_notas = calcular_media(notas)
    soma_notas = sum(notas)  
    alunos.append({'nome':nome_aluno, 'idade':idade_aluno, 'nota':notas, 'media': media_notas,'soma': soma_notas})
    print(f"Aluno {nome_aluno} cadastro com sucesso!\n")
    
    
#função para exibir alunos cadastrados
def exibir_alunos(alunos):
    if alunos:
        print('\nAlunos cadastrados')
        for i, aluno in enumerate(alunos, start=1):
            print (f"{i}\nNome:{aluno['nome']}\nIdade:{aluno['idade']}\nNota:{aluno['nota']} /Média: {aluno['media']:.2f}\nSoma: {aluno['soma']:.2f}")
        else:
            if not alunos:
                print('\n nenhum aluno cadastrado.')

#função principal
def main():
    alunos = []
    while True:
        exibir_nome_do_programa()
        opcao = input('Você quer cadastrar um aluno? (s/n)').lower()
        if opcao == 's':
            cadastrar_aluno(alunos)
        elif opcao == 'n':
            exibir_alunos(alunos)
            break
        else:
            print("Opção Invalida. Digite outra opção")
#execução do programa
if __name__ == "__main__":
        main()