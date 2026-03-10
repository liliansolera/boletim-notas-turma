notas_turma = {} #create class list

def validar_numero(mensagem): #check if it's a number and if it's valid (>0)
    while True:
        try:
            entrada = input(mensagem)
            numero = float(entrada) 

            if numero < 0:
                print('Número inválido, tente de novo')
                continue ## volto pro while true
            return numero  
        
        except ValueError:
            print(f'"{entrada}" não é uma entrada válida, tente novamente')
            continue
        
def validar_nome(mensagem, turma): #check if name already exists
    while True:
        try: 
            nome = (input(mensagem)).lower().strip()
            if nome.isdigit(): # isdigit retorna true or false
                print(f'"{nome}" é um número, tente novamente')
                continue
            if nome in turma: # x in dict checks keys by default, to check both keys & values .items(), to check only values .values()
                print('Nome já existe, tente de novo')
                continue
            return nome 
        
        except ValueError:
            print(f'"{nome}" não é uma entrada válida, tente novamente')
            continue
    
def media(notas): #calc avg for each std
    media_aluno = {}
    for aluno, nota in notas.items():
        total = sum(nota)
        qntd_notas = len(nota)
        calculo = round((total / qntd_notas),1)
        media_aluno[aluno] = calculo #indented in the loop, so it's for each std
    return media_aluno #outta the loop, so collects the last result (if it were in the loop, would store only the last run)

def analisar_medias(resultado_media): #gets highest and lowest avg
    maior_nota = max(resultado_media.values())
    menor_nota = min(resultado_media.values())
    for aluno, media in resultado_media.items(): #goes through dict to get the match
        if maior_nota == media:
            aluno_maior = aluno
        elif menor_nota == media:
            aluno_menor = aluno
    return aluno_maior, aluno_menor

def remover_aluno(nome, turma):
    try: 
        if nome.isdigit(): # isdigit retorna true or false
            print(f'"{nome}" é um número, tente novamente')

        if nome in turma: 
            status_remover = input(f'Confirma remover o aluno {nome} da lista?').lower().strip()
            if status_remover == 'sim':
                turma.pop(nome)
                return True
        else:
                return False
        
    except ValueError:
        print(f'"{nome}" não é uma entrada válida, tente novamente')


## COLLECT DATA ##
while True:
    
    try:
        match notas_turma:
            case {}:
                tipo_processo = 'adicionar'
            case _:
                tipo_processo = input('Você deseja remover ou adicionar alunos? Preencha com "remover" ou "adicionar"').lower().strip()
            
        match tipo_processo:
            case 'adicionar': 
                qnt_alunos = int(validar_numero('Quantos alunos?')) 

                for i in range(qnt_alunos):
                    aluno = validar_nome('Digite o nome do aluno', notas_turma) # pergunto nome do aluno
                    qnt_notas = int(validar_numero('Quantas notas?')) #quantas notas para aquele aluno
                    
                    notas_aluno = [] #crio lista vazia para aquele aluno

                    for x in range (qnt_notas): #runs once for each grade
                        
                        nota = float(validar_numero('Digite a nota'))
                        notas_aluno.append(nota) #add grade to each  students list
                    notas_turma[aluno] = notas_aluno #cria {aluno:lista de notas}
            case 'remover': 
                aluno_removido = input('Qual o nome do aluno? Preencha nome completo')
                remocao = remover_aluno(aluno_removido,notas_turma)
                if remocao:
                    print(f'{aluno_removido} foi removido com sucesso')
            case _:
                print('Entrada inválida, tente novamente')
                continue
    except:
            print('Erro, tente novamente')
            continue
    
    status_processamento = input('Deseja adicionar ou remover mais alunos?').lower().strip()
    match status_processamento: 
        case 'sim':
            continue
        case 'nao' | 'não':
            print('Processamento encerrado')
            break
        case _:
            print('Comando inválido, reinicie o processo')
            break

        
## PROCESS AND DATA OUTPUT##

resultado_media = media(notas_turma) 
for aluno, nota in resultado_media.items():
    print(f'Aluno {aluno}, nota: {nota}')
if len(resultado_media) > 1:
    aluno_maior, aluno_menor = (analisar_medias(resultado_media))
    print(f'A maior média é {(resultado_media[aluno_maior])} do aluno {aluno_maior}')
    print(f'A menor média é {(resultado_media[aluno_menor])} do aluno {aluno_menor}')


