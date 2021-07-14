import json
import re

# load database
file_name = "orginfo4in1.json"

with open(file_name) as f:
    data = json.load(f)

# full 'depth' of file:
# print(data[0]['FinancialInfos'][1]['crmDocumentRecords'][0]['FileName'])

def request_data(item, index2=-1, item2 = [], printname = 'no'):
    '''Gets the desired data. The data is of the format [list][dict][list][dict][list][dict].
    Thus we input an integer and a string alternatively for 3 layers (but I've only built up to two).
    May consider switch statement instead of all the 'if's.
    `printname='y'` will show the CharityName for each charity at the start of the output.
    '''

    index = 0
    with open("requested_data.txt", "a") as requests:
        for i in data:
            if printname == 'y':
                requests.write('CharityName: ' + data[index]['CharityName'])
                requests.write('\n')

            for one_item in item:
                if index2 == -1:
                    # change output into a one-liner before writing
                    # https://stackoverflow.com/questions/4903938/removing-all-whitespace-characters-except-for

                    one_item_data = data[index][one_item]
                    newline_removed = re.sub(r'[^\S ]+', "", str(one_item_data))
                    requests.write(newline_removed)

                    make_csv(item, requests, one_item)

                if index2 != -1 and item2 == []:
                    try:
                        requests.write(str(data[index][one_item][index2]))
                    except:
                        requests.write('N.A')
                        # requests.write('NA for ' + data[index]['CharityName'])

                if item2 != []:
                    for one_item2 in item2:
                        try:
                            requests.write(data[index][one_item][index2][str(one_item2)])

                            make_csv(item2, requests, one_item2)

                        except Exception as e:
                            # print(e)
                            requests.write('N.A')
                            # requests.write('NA for ' + data[index]['CharityName'])
                        
            requests.write('\n')
            index += 1
    
    return

def make_csv(list, requests, i):
    ''' adds a comma after each item except the last item.
    Note that the file `requests` should be open already before running this function
    '''

    if len(list) > 1 and list.index(i) != (len(list)-1):
        requests.write(',')

    return

# Call examples:

# request_data(['VisionMission'])
# request_data(['ContactPerson','Email'])
# request_data(["FinancialInfos"], index2=1, item2=['Income'])
# request_data(["FinancialInfos"], index2=2, item2=['Income','Spending'], printname='no')