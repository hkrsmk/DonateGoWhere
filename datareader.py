import json

file_name = "orginfo4in1.json"

with open(file_name) as f:
    data = json.load(f)

def request_data(item, index2=-1, item2 = '', printname = 'no'):
    '''Gets the desired data'''

    index = 0
    with open("requested_data.txt", "a") as requests:
        for i in data:
            if printname == 'y':
                requests.write('CharityName: ' + data[index]['CharityName'])
                requests.write('\n')

            if index2 == -1:
                requests.write(data[index][item])

            if index2 != -1 and item2 == 'nil':
                try:
                    requests.write(str(data[index][item][index2]))
                except:
                    requests.write('N.A')
                    # requests.write('NA for ' + data[index]['CharityName'])

            if item2 != 'nil':
                try:
                    requests.write(data[index][item][index2][str(item2)])
                except:
                    requests.write('N.A')
                    # requests.write('NA for ' + data[index]['CharityName'])
                        
            requests.write('\n')
            index += 1
    
    return


# request_data('KeyOfficers')
# request_data('UENNo')
# request_data("FinancialInfos", index2=1, item2='Income', printname='no')
request_data("FinancialInfos", index2=1, item2='Spending', printname='no')
# full 'depth' of file: print(data[0]['FinancialInfos'][1]['crmDocumentRecords'][0]['FileName'])