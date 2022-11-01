import os
import urllib.request
import pandas as pd
from transliterate import translit, slugify

if __name__ == '__main__':

    if not os.path.exists('./output'):
        os.makedirs('./output')

    filename = 'input.csv'
    df = pd.read_csv(filename)

    counter = 0

    try:
        for index, row in df.iterrows():
            name = slugify(translit(row['name'], "ru"))
            logo = row['logo']

            if not pd.isnull(logo):
                extension = logo.split('.')[-1]

                if not os.path.exists(f'./output/{name}'):
                    os.makedirs(f'./output/{name}')

                s = f'./output/{name}/logo.png'.replace('\n', '')

                urllib.request.urlretrieve(logo, s)

                print(f'saved {name}')

                counter += 1
    except e:
        print('Error:\n', e)
    finally:
        print(f'Loading completed: {counter}/{df.shape[0]} files saved. Check output folder!')


