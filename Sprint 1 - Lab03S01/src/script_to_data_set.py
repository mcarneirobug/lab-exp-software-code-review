import constant
import requests
import os
import time
import os.path
import json


def run_github_query_to_data_set(query):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=constant.HEADERS)
    while request.status_code == 502:
        time.sleep(2)
        request = requests.post(
            'https://api.github.com/graphql', json={'query': query}, headers=constant.HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))


def mine(quantidade_repo, owner, name):
    end_cursor = "null"  # Primeira página da iteração
    merged_prs = []  # lista para armazenar os merged request
    # Vai iterar pela quantidade de repositórios que serão passados através do arquivo txt
    for x in range(quantidade_repo):
        query_pr_merged = """
        {
          repository(owner: "%s", name: "%s") {
            merged: pullRequests(first: 5, after: %s, states: MERGED) {
              pageInfo {
                endCursor
              }
              totalCount
              nodes {
                createdAt
                mergedAt
                bodyText
                id
                reviews {
                  totalCount
                }
                participants {
                  totalCount
                }
                files {
                  totalCount
                }
              }
            }
          }
        }
    """ % (owner, name, end_cursor)

        # Variável armazena o resultado que contém a próxima página com os nodes
        resultado_query = run_github_query_to_data_set(query_pr_merged)
        # Variável armazena a quantidade de iterações que faremos para armazenar os merged de um repositório
        tamanho_query = len(resultado_query['data']['repository']['merged']['nodes'])
        # Variável pega o endCursor para próxima página dos merged (after)
        end_cursor = '"{}"'.format(
            resultado_query['data']['repository']['merged']['pageInfo']['endCursor'])
        # Só itera caso não for None e 0 e monta e adiciona o objeto de merged request em uma lista
        if tamanho_query is not None or 0:
            for y in range(tamanho_query):
                # Vai montar em um dicionário os resultados da query dos merged request
                data = dict(total_count=resultado_query['data']['repository']['merged']['totalCount'],
                            created_at=resultado_query['data']['repository']['merged']['nodes'][y]['createdAt'],
                            merged_at=resultado_query['data']['repository']['merged']['nodes'][y]['mergedAt'],
                            body_text=resultado_query['data']['repository']['merged']['nodes'][y]['bodyText'],
                            id_pr=resultado_query['data']['repository']['merged']['nodes'][y]['id'],
                            reviews=resultado_query['data']['repository']['merged']['nodes'][y]['reviews']['totalCount'],
                            participants=resultado_query['data']['repository']['merged']['nodes'][y]['participants'][
                                'totalCount'],
                            files=resultado_query['data']['repository']['merged']['nodes'][y]['files']['totalCount'])
                # Adiciona na lista os resultados obtidos
                merged_prs.append(data)
                print(merged_prs)
    # Salva em um arquivo JSON os resultados obtidos na lista a cada iteração
    with open("merged_data.json", "w") as file:
        json.dump(merged_prs, file, indent=4)


def run():
    # Vai pegar o caminho onde está nossos repositórios e seus respectivos nome, owner, etc
    path_arquivo_txt = os.getcwd() + r"\storage\urls_repos.txt"
    repos_list = ""
    # Iremos tentar abrir o arquivo para armazenar em uma lista
    try:
        with open(path_arquivo_txt) as file:
            repos_list = list(file)
    except Exception as e:
        print(f"Ocorreu um problema na execução do script, o arquivo não pode ser lido: {e}")

    # Para cada repositório armazenado na lista iremos pegar o owner e o nome do repositório
    for url_repo in repos_list:
        dividir_repo_pela_vircula = url_repo.split(',')

        owner_repositorio = dividir_repo_pela_vircula[2].strip()
        nome_repositorio = dividir_repo_pela_vircula[3].strip()

        print(mine(len(repos_list), owner_repositorio, nome_repositorio))


if __name__ == "__main__":
    run()
    print('#' * 100)
print('\nSuccessfully generated txt and json file...')
