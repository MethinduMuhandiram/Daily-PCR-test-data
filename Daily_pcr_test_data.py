import requests
import csv

req_covid = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
# requesting covid data  from  the api
covid_data = req_covid.json()
# convert html to json array
pcr_tst = covid_data['data']["daily_pcr_testing_data"]
# reading the data set in data --> daily_pcr_testing_data

with open('Daily PCR Testing Data - SL.csv', mode='w') as csv_file:
    # opening a csv file named "Daily PCR Testing Data - SL.csv"
    fieldnames = ['date', 'count']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # 'DictWriter()' class expects dictionaries for each row.
    csv_writer.writeheader()
    # writing the fieldnames as the header of the csv file

    for data in pcr_tst:
        csv_writer.writerow(data)
        # writing down the pcr test data row by row

