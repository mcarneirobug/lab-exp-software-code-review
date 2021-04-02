import os
import os.path
import script


# The function responsible for saving GitHub repository urls in .txt file
def export_urls_to_txt(urls_git_to_save_file):
    path = os.getcwd() + r"\urls_repos.txt"
    file = open(path, "w+")
    file.write(urls_git_to_save_file)
    file.close()


# The function responsible for write GitHub repository urls in .txt file with name
def write_data_to_txt():
    ans = script.get_all_repos()
    # print(len(ans))
    urls_git_to_save_file = ""
    counter = 0
    for item in ans:
        # strip -> methods removes any spaces at the beginning and spaces at the end
        urls_git_to_save_file += item['url'].strip() + "," + item['nameWithOwner'] + item['name'] + "\n"

        counter += 1
        print(f'Saving in txt file... {counter}')
    export_urls_to_txt(urls_git_to_save_file)
