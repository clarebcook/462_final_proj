import csv

def csv_reader(filename):
    signame_to_points = dict()

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            sig_name = row[0]
            times = tuple(float(x) for x in row[1].strip('()').split(','))
            vals = tuple(float(x) for x in row[2].strip('()').split(','))
            signame_to_points[sig_name] = [times, vals]
    return signame_to_points