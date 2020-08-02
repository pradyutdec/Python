import csv
def read_records(iterable):
    record = {}
    for line in iterable:
        if line.startswith('Question'):
            if record:
                yield record
            record = {}
        key, value = line.strip().split(":",1)
        record[key.strip()] = value.strip()
    if record:
        yield record

# Salida encabezados
headers = ("Question", "Option1", "Option2", "Option3", "Option4", "Answer")


with open("current1.txt") as infile, open("currenta.csv", 'w') as outfile:
    records = read_records(infile)
    writer = csv.DictWriter(outfile, headers, delimiter='^')
    writer.writeheader()

    # and write
    writer.writerows(records)
    print(records)