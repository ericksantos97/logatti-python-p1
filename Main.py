import pymongo
from bson.objectid import ObjectId

from Diretor import Diretor
from Filme import Filme
from Genero import Genero
from Avaliacao import Avaliacao

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python"]
filme_col = mydb["filme"]
genero_col = mydb["genero"]
diretor_col = mydb["diretor"]
avaliacao_col = mydb["avaliacao"]
continuar = True


# Funções de erros

def mensagem_erro():
    print('\nOcorreu um problema na aplicação, tente novamente.')


# Funções Filme

def inserir_filme():
    novoFilme = preencher_filme()
    result = filme_col.insert_one(novoFilme.__dict__)
    if result.inserted_id:
        print(f'\nO Filme {novoFilme.get_nome()} foi inserido com sucesso.')


def listar_filmes():
    for filme in filme_col.find():
        print("\nID: ", filme["_id"], "\nNome: ", filme["nome"], "\nSinopse: ", filme["sinopse"],
              "\nGênero: ", filme["genero"]["descricao"], "\nDiretor: ", filme["diretor"]["nome"],
              "\nAvaliação: ",
              filme["avaliacao"]["descricao"] if filme["avaliacao"] else "Não contém avaliação.")


def atualizar_filme():
    id_filme = str(input("\nInforme o id do Filme: "))
    filmeAlterado = preencher_filme()

    result = filme_col.update_one({'_id': ObjectId(id_filme)}, {"$set": filmeAlterado.__dict__})
    if result.modified_count > 0:
        print(f'\nO Filme {filmeAlterado.get_nome()} foi alterado com sucesso.')


def excluir_filme():
    id_filme = str(input("\nInforme o id do filme: "))
    filme_col.delete_one({"_id": ObjectId(id_filme)})
    print("Filme excluído com sucesso!")


def preencher_filme():
    filme = Filme()
    filme.set_nome(str(input("Informe o nome do Filme: ")))
    filme.set_sinopse(str(input("Informe a sinopse do Filme: ")))

    id_genero = str(input("\nInforme o id do Gênero: "))
    generos = [i for i in genero_col.find({"_id": ObjectId(id_genero)})]

    id_diretor = str(input("\nInforme o id do Diretor: "))
    diretores = [i for i in diretor_col.find({"_id": ObjectId(id_diretor)})]

    filme.set_genero(generos[0])
    filme.set_diretor(diretores[0])
    filme.set_avaliacao(Avaliacao().__dict__)
    return filme


# Funções Gênero

def inserir_genero():
    genero = Genero()
    genero.set_descricao(str(input("\nInforme a descrição do Gênero: ")))

    result = genero_col.insert_one(genero.__dict__)
    if result.inserted_id:
        print(f'\nO Gênero {genero.get_descricao()} foi inserido com sucesso.')


def listar_generos():
    for genero in genero_col.find():
        print("\nID: ", genero["_id"], "\nDescrição: ", genero["descricao"])


# Funções Diretor

def inserir_diretor():
    diretor = Diretor()
    diretor.set_nome(str(input("\nInforme o nome do Diretor: ")))

    result = diretor_col.insert_one(diretor.__dict__)
    if result.inserted_id:
        print(f'\nO Diretor {diretor.get_nome()} foi inserido com sucesso.')


def listar_diretores():
    for diretor in diretor_col.find():
        print("\nID: ", diretor["_id"], "\nNome: ", diretor["nome"])

# Funções Avaliação

def listar_avaliacao():
    for avaliacao in avaliacao_col.find():
        print("\nID: ", avaliacao["_id"], "\nDescrição: ", avaliacao["descricao"])

# Funções Extras

def associar_avaliacao_filme():
    id_filme = str(input("\nInforme o id do filme: "))
    filmes = [i for i in filme_col.find({"_id": ObjectId(id_filme)})]
    filme = filmes[0]

    id_avaliacao = str(input("\nInforme o id da Avaliação: "))
    avaliacoes = [i for i in avaliacao_col.find({"_id": ObjectId(id_avaliacao)})]
    filme.set_avaliacao(avaliacoes[0])

    result = filme_col.update_one({'_id': ObjectId(id_filme)}, {"$set": filme.__dict__})
    if result.modified_count > 0:
        print(f'\nO Filme {filme.get_nome()} recebeu uma avaliação.')


while continuar:
    print("\n==========================Menu Filme=========================")
    print("\n1 - Inserir Filme")
    print("\n2 - Listar Filmes")
    print("\n3 - Atualizar Filme")
    print("\n4 - Excluir Filme")

    print("\n==========================Menu Gênero=========================")
    print("\n5 - Inserir Gênero")
    print("\n6 - Listar Gêneros")

    print("\n==========================Menu Diretor=========================")
    print("\n7 - Inserir Diretor")
    print("\n8 - Listar Diretores")

    print("\n==========================Menu Avaliacao=========================")
    print("\n9 - Listar Avaliações")

    print("\n==========================Extras=========================")
    print("\n10- Associar Avaliação ao Filme")
    print("\n0 - Sair")

    opcao = input('\nInforme a opção desejada: ')

    if opcao == '1':
        try:
            print("\n====================Adicionar Filme====================")
            inserir_filme()
        except:
            mensagem_erro()

    elif opcao == '2':
        try:
            print("\n====================Listar Filmes====================")
            listar_filmes()
        except:
            mensagem_erro()

    elif opcao == '3':
        try:
            print("\n====================Atualizar Filme====================")
            atualizar_filme()
        except:
            mensagem_erro()

    elif opcao == '4':
        try:
            print("\n====================Excluir Filme====================")
            excluir_filme()
        except:
            mensagem_erro()

    elif opcao == '5':
        try:
            print("\n====================Adicionar Gênero====================")
            inserir_genero()
        except:
            mensagem_erro()

    elif opcao == '6':
        try:
            print("\n====================Listar Gêneros====================")
            listar_generos()
        except:
            mensagem_erro()

    elif opcao == '7':
        try:
            print("\n====================Adicionar Diretor====================")
            inserir_diretor()
        except:
            mensagem_erro()

    elif opcao == '8':
        try:
            print("\n====================Listar Diretor====================")
            listar_diretores()
        except:
            mensagem_erro()

    elif opcao == '9':
        try:
            print("\n====================Listar Avaliações====================")
            listar_avaliacao()
        except:
            mensagem_erro()

    elif opcao == '10':
        print("\n====================Associar Avaliação ao Filme====================")
        associar_avaliacao_filme()

    elif opcao == '0':
        continuar = False

    else:
        print("\nOpção inválida.")
