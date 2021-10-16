import csv

file_name = "data/newHivInfections.csv"
write_file = "data/incidenceOfHIV.csv"

field_names = ['Location', 'Period', 'Total']
input_file = csv.DictReader(open(file_name))
write_file = csv.DictWriter(open(write_file, 'w'), fieldnames=field_names, delimiter=",", lineterminator='\n')
write_file.writeheader()

for row in input_file:
    data =  row["First Tooltip"].split()[0]

    if data[0] != "N":
        if data[0] == "<":
            data = data[1:]
        if row["Dim1"][0] == "B":
            write_file.writerow({
                "Location": row["ï»¿Location"],
                "Period": row["Period"],
                "Total": data
            })