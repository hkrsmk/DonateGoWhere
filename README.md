## Scraper

In the below website, in status of charity, select 'IPCs' and click 'Search'
https://www.charities.gov.sg/Pages/AdvanceSearch.aspx?q=

I then downloaded all the pages individually as html files, and then ran a python script to get the links for each charity.

## Easier way
Observe the query and then write your own in cURL (see pictures and .out file)

If using the easier method, `CharityAccountCRMRecordID` should be encoded with base64 before putting in as a query for individual charities.