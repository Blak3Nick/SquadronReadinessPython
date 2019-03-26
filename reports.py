import csv


def process_fitness(list_of_members, file_to_read):
    fitness_report = []
    with open(file_to_read) as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            last_name = row[0].upper()
            first_name = row[1].upper()
            if last_name in list_of_members and first_name in list_of_members:
                fitness_report.append(row)
    return fitness_report
