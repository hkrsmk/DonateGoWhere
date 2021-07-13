# https://www.askpython.com/python/dictionary/merge-dictionaries
# https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file

import json

# file_name = "dataclean/orginfosamplejsonmake.json"
file_name = "datascraper/orginfojsonmake.json"

with open(file_name) as f:
    data = json.load(f)

    with open('orginfo4in1.json', 'a') as fp:
        fp.write('[')

        for i in range(int(len(data)/4)):
            j = 4*i
            print(i)
            print(j)
            combo = {}
            combo = {**data[j],**data[j+1],**data[j+2],**data[j+3]}
            json.dump(combo, fp)
            if i != 632:
                fp.write(',')

        fp.write(']')

print(data[0]['GoverningMembers'][0]['FullName'])