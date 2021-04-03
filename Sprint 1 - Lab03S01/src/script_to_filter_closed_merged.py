import json
import pandas as pd
import os


def run():
    try:
        with open('storage\\repo_data.json', 'r') as read_file:
            js = json.load(read_file)
        df = pd.DataFrame(js, columns=['nameRepository', 'prMerged', 'prClosed'], index=range(105))
        df["sum"] = df['prMerged'] + df['prClosed']
        df.to_csv(os.path.abspath(os.getcwd()) + f'/output_soma_prmerged_prclosed.csv', index=False, header=True)
        print(df)
    except Exception as e:
        print(f'Não foi possível ler o arquivo json: {e}')


if __name__ == "__main__":
    run()
    print('#' * 40)
    print('Successfully save data to CSV...')
    print('#' * 40)
