import json
import re

# load database
# database of IPCs
file_name = "datascraper/ipc_info4in1.json"
# for full database
# file_name = "datascraper/allcharityinfoallin1.json"

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

                        except Exception as e:
                            # print(e)
                            requests.write('N.A')
                            # requests.write('NA for ' + data[index]['CharityName'])
                        
                        make_csv(item2, requests, one_item2)

            requests.write('\n')
            index += 1
    
    return

def request_data_financial(item, key_value, year_requested):

    with open("requested_data.txt", "a") as requests:
        for i in range(len(data)):
            for one_item in item:
                try:
                    entire_item_array = json.loads(data[i][one_item])
                except:
                    requests.write("N.A.")
                    continue

                for one_item_array in entire_item_array:

                    if one_item_array[0]["Value"] in key_value:

                        # for if I want to make this print all values
                        # result_array = []
                        # for value in one_item_array[1:]:
                        #     result_array.append(value["Value"])

                        try:
                            requests.write(one_item_array[year_requested]["Value"])

                        except:
                            requests.write("N.A.")

            requests.write("\n")

    return

def make_csv(list, requests, i):
    ''' adds a comma after each item except the last item.
    Note that the file `requests` should be open already before running this function
    '''

    if len(list) > 1 and list.index(i) != (len(list)-1):
        requests.write(',')

    return

# Call examples:

# request_data(['UENNo'])
# request_data(['Objective'])
# request_data(['VisionMission'])
# request_data(['Website','ContactPerson','Email'])
# request_data(["FinancialInfos"], index2=1, item2=['Income'])

# request_data(["FinancialInfos"], index2=1, item2=['Income','Spending'], printname='no')
# request_data(["FinancialInfos"], index2=2, item2=['Income','Spending'], printname='no')

# request_data(["FinancialInfos"], index2=2, item2=['Income','Spending'], printname='no')

# observe the data to find out the year corresponding to the needed data
# Apr 2018 - Mar 2019 == 3
# Apr 2019 - Mar 2020 == 2
# Apr 2020 - Mar 2021 == 1
request_data_financial(["FinancialInfoBalanceSheet"],["Total Funds and Reserves"],3)