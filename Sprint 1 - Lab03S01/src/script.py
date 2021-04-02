import time
import requests
import constant

import script_to_txt
import script_to_json


# The function responsible for making requests in GitHub API
def run_github_query(json):
    request = requests.post(f'{constant.URL}', json=json, headers=constant.HEADERS)
    while request.status_code != 200:
        print("Error calling the API, processing again...")
        print(f'The query failed: {request.status_code}. {json["query"]}, {json["variables"]}')
        time.sleep(5)
        request = requests.post(f'{constant.URL}', json=json, headers=constant.HEADERS)
    return request.json()


def get_all_repos():
    json = {
        "query": constant.QUERY, "variables": {}
    }

    result = run_github_query(json)
    nodes = result['data']['search']['nodes']
    end_cursor = result['data']['search']['pageInfo']['endCursor']
    query = constant.QUERY.replace("first:5", "first:5{AFTER}")

    for i in range(0, 20):
        if result['data']['search']['pageInfo']['hasNextPage']:
            new_query = query.replace("{AFTER}", f", after:\"{end_cursor}\"")
            json = {
                "query": new_query, "variables": {}
            }
            result = run_github_query(json)
            end_cursor = result['data']['search']['pageInfo']['endCursor']
            nodes += result['data']['search']['nodes']
    return nodes


if __name__ == "__main__":
    script_to_txt.write_data_to_txt()
    script_to_json.write_data_to_json()
    print('#' * 100)
    print('\nSuccessfully generated txt and json file...')
