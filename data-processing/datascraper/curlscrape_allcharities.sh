#!/bin/bash
# https://stackoverflow.com/questions/50602894/curl-through-list-in-bash
# https://codefather.tech/blog/curl-bash-script/
# gets the json file of the response and writes it into a file

# other stuff used:
# https://linoxide.com/make-bash-script-executable-using-chmod/
# https://stackoverflow.com/questions/40359012/how-to-append-a-file-with-the-existing-one-using-curl

# to test the curl command:
# curl 'https://www.charities.gov.sg/_layouts/15/CPInternet/SearchResultHandler.ashx?query=YjQwNTU3ZTktNzg2NS1lMzExLTgyZGItMDA1MDU2YjMwNDg0&type=Organisation%20Profile' -w '\n'

# when there are variables, you must use double quotation marks for the curl command.
# https://www.howtogeek.com/442332/how-to-work-with-variables-in-bash/

# the \ is for formatting and breaking up one command into many paragraphs.
# bugs: the script sometimes runs without charity_id
# line 30: orginfo.txt: command not found
# line 33: syntax error near unexpected token `done'
# line 33: `done < ID_list.txt'


while read -n48 -r charity_id; do
curl "https://www.charities.gov.sg/_layouts/15/CPInternet/SearchResultHandler.ashx\
?query=${charity_id}\
&type={Organisation%20Profile,\
Financial%20Information,\
Annual%20Report,\
Code%20Compliance}"\
 -w "\n" >> allcharityinfo.txt
# printf $charity_id
# done < ID_listtest.txt
done < allcharityIDs.txt