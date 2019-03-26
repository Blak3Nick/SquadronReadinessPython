import csv
import pandas as pd
import xlrd


def process_fitness(list_of_members, file_to_read):
    fitness_report = []
    excel_file = pd.read_excel(file_to_read, sheet_name='Detail', header=0, skiprows=12)

    print(excel_file.iat[1, 2])
    # with open(file_to_read) as f:
    #     csvReader = csv.reader(f)
    #     for row in csvReader:
    #         print(row)
    #         last_name = row[0]
    #         first_name = row[1]
    #         if last_name in list_of_members and first_name in list_of_members:
    #             fitness_report.append(row)
    # return fitness_report
