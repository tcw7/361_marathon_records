import requests
from bs4 import BeautifulSoup

URL_men = "https://www.worldathletics.org/records/all-time-toplists/road-running/marathon/outdoor/men/senior"
URL_women = "https://www.worldathletics.org/records/all-time-toplists/road-running/marathon/outdoor/women/senior"

print('\nWaiting for next request...')

# enter loop to continually read the marathon_records.txt file
while True:
    # open file for reading
    records = ""
    records_file = open('./marathon_records.txt', 'r')

    # program is requested to run
    if records_file.read(3) == 'run':
        print('\nReceived request for marathon records...')

        # get records

        # mens
        records += "MENS_RECORDS_BEGIN\n"
        mens_page = requests.get(URL_men)
        mens_soup = BeautifulSoup(mens_page.content, "html.parser")
        mens_record = mens_soup.find("table", class_="records-table")
        mens_record_arr = [s for s in mens_record.strings]
        for i in mens_record_arr:
            record_stripped = i.strip()
            if record_stripped == "":
                continue
            records += record_stripped
            records += "\n"

        # womens
        records += "WOMENS_RECORDS_BEGIN\n"
        womens_page = requests.get(URL_women)
        womens_soup = BeautifulSoup(womens_page.content, "html.parser")
        womens_record = womens_soup.find("table", class_="records-table")
        womens_record_arr = [s for s in womens_record.strings]
        for i in womens_record_arr:
            record_stripped = i.strip()
            if record_stripped == "":
                continue
            records += record_stripped
            records += "\n"

        # overwrite current file
        records_file.close()
        records_file = open('./marathon_records.txt', 'w')
        records_file.write(records)
        records_file.close()
        print(f'\nRecords found. "marathon_records.txt" has been overwritten.')
        print('\nWaiting for next request...')

    else:
        records_file.close()
