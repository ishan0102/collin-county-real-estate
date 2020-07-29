import csv
import os

# parse condensed owner information into a CSV file
def owner_info_condensed():
    # open CSV file
    with open('data/raw_csv/owner_info.csv', mode='w') as owner_info:
        write = csv.writer(owner_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # write header
        write.writerow(['account_number', 'legal_description', 'name1', 'address1', 'delinquency_date', 'value', 'amount_due', 'total_amount_due'])

        # open text file
        with open('data/raw_txt/owner_info.txt', mode='r') as read:
            # iterate through text file
            for record in read:
                record = record.strip()

                # assign variables
                account_number = record[0:30]
                legal_description = record[36:160]
                name1 = record[334:384]
                address1 = record[434:484]
                delinquency_date = record[679:689]
                value = record[790:801]
                amount_due = record[823:835]
                total_amount_due = record[835:847]

                # write row to CSV file
                write.writerow([account_number, legal_description, name1, address1, delinquency_date, value, amount_due, total_amount_due])

# parse condensed owner taxes into a CSV file
def owner_taxes_condensed():
    # open CSV file
    with open('data/raw_csv/owner_taxes.csv', mode='w') as owner_taxes:
        write = csv.writer(owner_taxes, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # write header
        write.writerow(['account_number', 'year', 'amount_due', 'delinquency_date', 'bankruptcy_date'])

        # open text file
        with open('data/raw_txt/owner_taxes.txt', mode='r') as read:
            # iterate through text file
            for record in read:
                record = record.strip()
                
                # assign variables
                account_number = record[0:30]
                year = record[30:34]
                amount_due = record[75:87]
                delinquency_date = record[87:97]
                bankruptcy_date = record[163:173]

                # write row to CSV file
                write.writerow([account_number, year, amount_due, delinquency_date, bankruptcy_date])

if __name__ == "__main__":
    print("\nThis will load the owner information and taxes CSV files from the appropriate text files.\n")

    # remove CSV files if they already exist
    try:
        os.remove('data/raw_csv/owner_info.csv')
        os.remove('data/raw_csv/owner_taxes.csv')
        print("The old owner_info.csv and owner_taxes.csv files have been removed.\n")
    except:
        print("The files don\'t exist yet. They will be created automatically.\n")

    # parse owner information text file and write rows to CSV file
    print("Parsing owner information...")
    owner_info_condensed()
    print("owner_info.csv has been loaded.\n")

    # parse owner taxes text file and write rows to CSV file
    print("Parsing owner taxes...")
    owner_taxes_condensed()
    print("owner_taxes.csv has been loaded.\n")
