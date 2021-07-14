# How to use
## datareader.py
Get the requested data and outputs it into a `requested_data.txt` file, for pasting into google sheets. Just change the function call to info you want. The data is obtained from `orginfo4in1.json` - it is very big, you can download it but it's better not to open it. A sample can be found in `orginfosample4in1.json`.

For the database of all charities, use `allcharityinfoallin1.json` as the database. The format is a little weird - each item is a one-item list instead of just a string. But should be good enough.

# Below the hood
Aka, how I got this data.

## 1. IDScraper
In the below website, in status of charity, select 'IPCs' and click 'Search'
https://www.charities.gov.sg/Pages/AdvanceSearch.aspx?q=

I then downloaded all the pages individually as html files, and then ran a python script to get the links for each charity.

### Easier way
Observe the query and then write your own in cURL (see pictures and .out file)

If using the easier method, `CharityAccountCRMRecordID` should be encoded with base64 before putting in as a query for individual charities. The easier way was used to get information on all charities, not just IPCs.

## 2. datascraper folder
Uses curl in a bash script `curlscrape.sh` to get all the info of each individual charity - Profile, Financial Info, Annual Report, Code Compliance. This is all stored in the `orginfo.txt` file. The `orginfo.txt` file will be converted into an excel sheet with just the relevant info - a short description of the charity, Income vs Expenditure (for room for funding), and any other info for evaluating effectiveness. This is the longest step, since you'd have to query the government's database quite a lot of times.

## 3. dataclean.py
Remove the excessive commands and keep only the information we want. Now it should be a proper json file. Trailing commas had to be removed manually (the last one before the `]`)

## 4. datacombine.py or datacombine_2.ipynb
Combine everything with the same `CharityName` into one JSON object to make things easier. If the number of repeated `CharityName`s are different each time, use the .ipynb file instead. I couldn't make an itertools.groupby work properly in Python because it doesn't play well with json, so I switched to pandas and notebooks.