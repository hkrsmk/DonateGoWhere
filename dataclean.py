import re

def uncurl(file_to_edit):
    '''remove curl commands, empty lines and 404s from the appended curl output, overwriting the final file each time
    taken from https://stackoverflow.com/questions/11968998/remove-lines-that-contain-certain-string
    https://stackoverflow.com/questions/3711856/how-to-remove-empty-lines-with-or-without-whitespace-in-python
    '''

    bad_words = ['--_curl_--https:', '&type=',
    '{"Error":"1","Message":"The remote server returned an error: (404) Not Found."}']

    with open(file_to_edit+'.txt') as oldfile, open(file_to_edit+'new.json', 'w+') as newfile:

        # new content with only non-curl lines written, and non-empty lines
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words) and not re.match(r'^\s*$', line):
                newfile.write(line)

    return

def json_maker(file):
    '''change the json object into an array by adding '[' ']' and also the relevant commas
    https://stackoverflow.com/questions/6791468/array-of-json-objects

    However, we have to remove the last trailing comma by hand.

    uncomment the code if the data is multi-line
    '''

    file_to_filter = open(file + 'new.json', 'r')

    with open(file + 'jsonmake.json', 'w') as jsonified_file:
        jsonified_file.write('[')

        for line in file_to_filter:
            # if line == '}\n':
                # jsonified_file.write(line + ',')
            # else:
                jsonified_file.write(line + ',')

        jsonified_file.write(']')

    return

def run_both(filename):
    '''runs both functions uncurl and json_maker in one command'''

    uncurl(filename)
    json_maker(filename)
    return

# uncurl('orginfosample')
# json_maker('orginfosample')
# uncurl('datascraper/orginfo')
# json_maker('datascraper/orginfo')

run_both('datascraper/allcharityinfo')