import re
from bs4 import BeautifulSoup

def extract_urls(filename):
    ''' Extracts URLs and outputs into a file called output.txt'''

    # https://stackoverflow.com/questions/15517483/how-to-extract-urls-from-an-html-page-in-python
    links_source = str(BeautifulSoup(open(filename + ".html")))

    print(links_source)

    # https://stackoverflow.com/questions/7124778/how-to-match-anything-up-until-this-sequence-of-characters-in-a-regular-expres
    found_links = re.findall(r'https://www.charities.gov.sg/_layouts/15/CPInternet/SearchOrgProfile.aspx\?q=.+?(?=\")', links_source)

    print(found_links)
    output_file = open("output.txt", "a")

    for link in found_links:
        output_file.write(link)
        output_file.write("\n")
    return

def extract_urls_many(allfiles):
    for file in allfiles:
        extract_urls(file)
    return

# example command
# extract_urls("test")

# create a list of numbers [1, 2 ... 127] then go
# extract_urls_many(['1'])

# https://stackoverflow.com/questions/26320175/how-to-convert-integers-in-list-to-string-in-python
files = list(map(str, range(1, 128)))
extract_urls_many(files)