import json
import script


def write_data_to_json():
    nodes = script.get_all_repos()
    print(len(nodes))
    repos = []
    for item in nodes:
        data = {
            "nameOwner": item["nameWithOwner"],
            "nameRepository": item["name"],
            "url": item["url"],
            "sshUrl": item["sshUrl"],
            "createdAt": (item["createdAt"])[:10],
            "prMerged": item["mr"]["totalCount"],
            "prClosed": item["mc"]["totalCount"],
            "owner": item["owner"]["login"]
        }
        repos.append(data)
    with open("storage/repo_data.json", "w") as f:
        json.dump(repos, f, indent=4)
