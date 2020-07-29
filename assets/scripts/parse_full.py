import csv
import os

# parse owner information into a CSV file
def owner_info():
    # open CSV file
    with open('data/raw_csv/owner_info.csv', mode='w') as owner_info:
        write = csv.writer(owner_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # write header
        write.writerow(['account_number', 'sptb_code', 'roll_code', 'legal_description', 'acres', 'appraisal_district_number', 'street_name', 
                        'street_number', 'square_feet', 'lot_size', 'year_built', 'loan_number', 'map_number', 'mapsco_number', 'appraisal_map_number',
                        'name1', 'name2', 'address1', 'address2', 'city', 'state', 'postal_code', 'start_deferral_date', 'end_deferral_date', 'volume',
                        'page', 'deed_date', 'exemption_codes', 'delinquency_date', 'tax_unit_codes', 'non_billed_tax_units', 'land_value',
                        'improvement_value', 'value', 'exemptions', 'levy', 'amount_due', 'total_amount_due'])

        # open text file
        with open('data/raw_txt/owner_info.txt', mode='r') as read:
            # iterate through text file
            for record in read:
                record = record.strip()

                # assign variables
                account_number = record[0:30]
                sptb_code = record[30:33]
                roll_code = record[33:36]
                legal_description = record[36:160]
                acres = record[160:173]
                appraisal_district_number = record[173:203]
                street_name = record[203:228]
                street_number = record[228:238]
                square_feet = record[238:244]
                lot_size = record[244:250]
                year_built = record[250:254]
                loan_number = record[254:264]
                map_number = record[264:294]
                mapsco_number = record[294:314]
                appraisal_map_number = record[314:334]
                name1 = record[334:384]
                name2 = record[384:434]
                address1 = record[434:484]
                address2 = record[484:534]
                city = record[534:584]
                state = record[584:604]
                postal_code = record[604:622]
                start_deferral_date = record[622:632]
                end_deferral_date = record[632:642]
                volume = record[642:648]
                page = record[648:654]
                deed_date = record[654:664]
                exemption_codes = record[664:679]
                delinquency_date = record[679:689]
                tax_unit_codes = record[689:719]
                non_billed_tax_units = record[719:769]
                land_value = record[769:779]
                improvement_value = record[779:790]
                value = record[790:801]
                exemptions = record[801:811]
                levy = record[811:823]
                amount_due = record[823:835]
                total_amount_due = record[835:847]

                # write row to CSV file
                write.writerow([account_number, sptb_code, roll_code, legal_description, acres, appraisal_district_number, street_name, 
                                street_number, square_feet, lot_size, year_built, loan_number, map_number, mapsco_number, appraisal_map_number,
                                name1, name2, address1, address2, city, state, postal_code, start_deferral_date, end_deferral_date, volume,
                                page, deed_date, exemption_codes, delinquency_date, tax_unit_codes, non_billed_tax_units, land_value,
                                improvement_value, value, exemptions, levy, amount_due, total_amount_due])

# parse owner taxes into a CSV file
def owner_taxes():
    # open CSV file
    with open('data/raw_csv/owner_taxes.csv', mode='w') as owner_taxes:
        write = csv.writer(owner_taxes, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # write header
        write.writerow(['account_number', 'year', 'tax_unit_number', 'receivable_type_code', 'sequence_number', 'value', 'exemptions', 'levy',
                        'amount_due', 'delinquency_date', 'the_3307_date', 'judgment_date', 'suit_number', 'suit_date', 'bankruptcy_number',
                        'bankruptcy_date', 'status_codes', 'sequence_type_code', 'installment', 'installment_type', 'installment_start_date',
                        'installment_end_date', 'installment_paid_date'])

        # open text file
        with open('data/raw_txt/owner_taxes.txt', mode='r') as read:
            # iterate through text file
            for record in read:
                record = record.strip()
                
                # assign variables
                account_number = record[0:30]
                year = record[30:34]
                tax_unit_number = record[34:37]
                receivable_type_code = record[37:40]
                sequence_number = record[40:42]
                value = record[42:53]
                exemptions = record[53:64]
                levy = record[64:75]
                amount_due = record[75:87]
                delinquency_date = record[87:97]
                the_3307_date = record[97:107]
                judgment_date = record[107:117]
                suit_number = record[117:135]
                suit_date = record[135:145]
                bankruptcy_number = record[145:163]
                bankruptcy_date = record[163:173]
                status_codes = record[173:188]
                sequence_type_code = record[188:190]
                installment = record[190:191]
                installment_type = record[191:194]
                installment_start_date = record[194:204]
                installment_end_date = record[204:214]
                installment_paid_date = record[214:224]

                # write row to CSV file
                write.writerow([account_number, year, tax_unit_number, receivable_type_code, sequence_number, value, exemptions, levy,
                                amount_due, delinquency_date, the_3307_date, judgment_date, suit_number, suit_date, bankruptcy_number,
                                bankruptcy_date, status_codes, sequence_type_code, installment, installment_type, installment_start_date,
                                installment_end_date, installment_paid_date])

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
    print("parsing owner information...")
    owner_info()
    print("finished\n")

    # parse owner taxes text file and write rows to CSV file
    print("parsing owner taxes...")
    owner_taxes()
    print("finished\n")
