# IDScraper
In the below website, in status of charity, select 'IPCs' and click 'Search'
https://www.charities.gov.sg/Pages/AdvanceSearch.aspx?q=

I then downloaded all the pages individually as html files, and then ran a python script to get the links for each charity.

## Easier way
Observe the query and then write your own in cURL (see pictures and .out file)

If using the easier method, `CharityAccountCRMRecordID` should be encoded with base64 before putting in as a query for individual charities.

# curlscrape.sh
Uses curl in a bash script to get all the info of each individual charity - Profile, Financial Info, Annual Report, Code Compliance. This is all stored in the `orginfo.txt` file. The `orginfo.txt` file will be converted into an excel sheet with just the relevant info - a short description of the charity, Income vs Expenditure (for room for funding), and any other info for evaluating effectiveness.