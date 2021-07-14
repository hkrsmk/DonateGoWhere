# https://www.askpython.com/python/dictionary/merge-dictionaries
# https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file

import json
import itertools

def combine_data(file_name,number_of_charities):
    '''combines the four different tabs with same charity ID into one file.
    Finally makes the file a nice json to use.
    '''
    with open(file_name + "jsonmake.json") as f:
        data = json.load(f)

        with open(file_name + '4in1.json', 'a') as fp:
            fp.write('[')
            for i in range(int(len(data)/4)):
                j = 4*i
                # print(i)
                # print(j)
                combo = {}
                combo = {**data[j],**data[j+1],**data[j+2],**data[j+3]}
                json.dump(combo, fp)
                if i != (number_of_charities-1):
                    fp.write(',')

            fp.write(']')
    return

# combine_data("dataclean/orginfosample",633)
# combine_data("datascraper/allcharity",2958)