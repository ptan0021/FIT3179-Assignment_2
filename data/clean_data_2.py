import csv

file_name = "data/incedenceOfTuberculosis.csv"
write_file = "data/incidenceOfTuberculosis.csv"

field_names = ['Location', 'Period', 'Total']
input_file = csv.DictReader(open(file_name))
write_file = csv.DictWriter(open(write_file, 'w'), fieldnames=field_names, delimiter=",", lineterminator='\n')
write_file.writeheader()

for row in input_file:
    data =  row["First Tooltip"].split()[0]

    if data[0] == "<":
        data = data[1:]
    
    try:
        data = float(data)
        write_file.writerow({
            "Location": row["ï»¿Location"],
            "Period": row["Period"],
            "Total": data
        })
    except:
        pass