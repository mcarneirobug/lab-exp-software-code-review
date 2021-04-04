import constant
import requests
import os
import time
import os.path
import json
import dateutil.parser


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
            closed: pullRequests(first: 5, after: %s, states: CLOSED) {
              pageInfo {
                endCursor
              }
              totalCount
              nodes {
                createdAt
                closedAt
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
        print(f'\nO resultado da query: {resultado_query}')

        # Variável armazena a quantidade de iterações que faremos para armazenar os merged de um repositório
        tamanho_query = len(resultado_query['data']['repository']['closed']['nodes'])
        print(f'O tamanho da query: {tamanho_query}')

        # Se o tamanho for zero, nós iremos fazer a próxima iteração
        if tamanho_query != 0:
            # Variável pega o endCursor para próxima página dos merged (after)
            end_cursor = '"{}"'.format(
                resultado_query['data']['repository']['closed']['pageInfo']['endCursor'])

            print(f'\nO cursor final é: {end_cursor}\n')

            # Só itera caso não for None e 0 e monta e adiciona o objeto de merged request em uma lista
            if tamanho_query is not None:
                for y in range(tamanho_query):
                    # Pegarmos a quantidade de caracteres do comentário do commit do PR
                    if len(resultado_query['data']['repository']['closed']['nodes'][y]['bodyText']) > 0:
                        quantidade_caracteres_body_text = len(
                            resultado_query['data']['repository']['closed']['nodes'][y]['bodyText'])
                    else:
                        quantidade_caracteres_body_text = 0

                    print(f'A quantidade de caracteres do body text: {quantidade_caracteres_body_text}')

                    # Iremos pegar a data de criação do PR e a data de MERGE REQUEST e iremos comparar
                    # Se não foi feito por um BOT ou CI/CD, então tem que ter pelo menos uma hora de diferença
                    created_at = resultado_query['data']['repository']['closed']['nodes'][y]['createdAt']
                    closed_at = resultado_query['data']['repository']['closed']['nodes'][y]['closedAt']

                    # Só iremos verificar caso a data não seja None, pois, é impossível saber o tempo
                    if created_at is not None and closed_at is not None:
                        created_parse = dateutil.parser.parse(created_at)
                        merged_parse = dateutil.parser.parse(closed_at)
                        diferenca_entre_criacao_e_merge = merged_parse - created_parse
                        calc_diferenca_datas = diferenca_entre_criacao_e_merge.seconds / 3600 % 24

                        print(f'A hora entre a diferença entre as datas: {calc_diferenca_datas}')

                        # Só iremos colocar no dicionário request que tenham pelo menos uma revisão
                        # E também a data de criação do PR tenha pelo menos uma hora
                        reviews_quantidade = resultado_query['data']['repository']['closed']['nodes'][y]['reviews']['totalCount']

                        # Caso o reviews for None automaticamente ele não tem nenhum valor
                        # e não irá dar problema na condicional
                        if reviews_quantidade is None:
                            reviews_quantidade = 0

                        print(f'A quantidade de reviews: {reviews_quantidade}\n')

                        if reviews_quantidade >= 1 and calc_diferenca_datas >= 1:
                            # Vai montar em um dicionário os resultados da query dos merged request

                            try:
                                if resultado_query['data']['repository']['closed']['nodes'][y]['files']['totalCount'] is None:
                                    result_files = "without_data"
                                else:
                                    result_files = str(resultado_query['data']['repository']['closed']['nodes'][y]['files']['totalCount'])
                                if resultado_query['data']['repository']['closed']['nodes'][y]['participants']['totalCount'] is None:
                                    result_participants = "without_data"
                                else:
                                    result_participants = str(resultado_query['data']['repository']['closed']['nodes'][y]['participants']['totalCount'])
                                if resultado_query['data']['repository']['closed']['nodes'][y]['id'] is None:
                                    result_id = "without_data"
                                else:
                                    result_id = str(resultado_query['data']['repository']['closed']['nodes'][y]['id'])
                                if resultado_query['data']['repository']['closed']['totalCount'] is None:
                                    result_total_count = "without_data"
                                else:
                                    result_total_count = str(resultado_query['data']['repository']['closed']['totalCount'])

                                print(f'Total PRs MERGED: {result_total_count}')
                                print(str(resultado_query['data']['repository']['closed']['nodes'][y]['createdAt']))
                                print(str(resultado_query['data']['repository']['closed']['nodes'][y]['closedAt']))
                                print(f'Id: {result_id}')
                                print(f'Quantidade de reviews: {reviews_quantidade}')
                                print(f'Quantidade participantes: {result_participants}')
                                print(f'Quantidade arquivos: {result_files}')

                                # data = dict(total_count=result_total_count,
                                #             created_at=created_at,
                                #             closed_at=closed_at,
                                #             body_text=quantidade_caracteres_body_text,
                                #             id_pr=result_id,
                                #             reviews=reviews_quantidade,
                                #             participants=result_participants,
                                #             files=result_files)
                                merged_prs.append(
                                    {
                                        "total_count": result_total_count,
                                        "created_at": created_at,
                                        "closed_at": closed_at,
                                        "body_text": quantidade_caracteres_body_text,
                                        "id_pr": result_id,
                                        "reviews": reviews_quantidade,
                                        "participants": result_participants,
                                        "files": result_files
                                    }
                                )
                            except Exception as e:
                                print(f'Deu ruim em algum lugar: {e}')
                                continue

                # Salva em um arquivo JSON os resultados obtidos na lista a cada iteração por página (5 por página)
                with open(f"data_json_closed\\merged_data_{owner}_{name}_{quantidade_repo}.json", "w") as file:
                    json.dump(merged_prs, file, indent=4)
            else:
                continue


"""
Metódo responsável por abrir o arquivo txt e armazenar os repositórios em uma lista
e após isso iterar por essa lista e chamando o método para minerar baseado no nome 
do dono do repositório e o nome do repositório
"""


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
        # iremos transformar nossa string em uma lista separando pelas vírgulas
        dividir_repo_pela_vircula = url_repo.split(',')
        # iremos pegar o owner do repositório
        owner_repositorio = dividir_repo_pela_vircula[2].strip()
        # iremos pegar o nome do repositório
        nome_repositorio = dividir_repo_pela_vircula[3].strip()

        print(mine(len(repos_list), owner_repositorio, nome_repositorio))


if __name__ == "__main__":
    run()
    print('#' * 100)
print('\nSuccessfully...')
