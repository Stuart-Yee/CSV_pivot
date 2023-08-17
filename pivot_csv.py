def flip_table(filename, new_filename):
    from pprint import pprint
    import csv
    code_dict = {}
    with open(filename, newline="") as source_file:
        csv_reader = csv.reader(source_file)

        for row in csv_reader:
            if len(row[1]) > 0:
                if code_dict.get(row[1]):
                    code_dict[row[1]] = code_dict.get(row[1]) + f",{row[0]}"
                else:
                    code_dict[row[1]] = row[0]
    
    codes_list = []
    for key, val in code_dict.items():
        codes_list.append([key, val])

    pprint(codes_list)

    if new_filename[-4:] != ".csv":
        new_filename += ".csv"

    print(new_filename)

    with open(new_filename, "w") as new_csv:
        csv_write = csv.writer(new_csv)
        csv_write.writerows(codes_list)



if __name__ == "__main__":
    source = input("Enter file path of source .csv ")
    destination = input("Enter name of output .csv ")
    flip_table(source, destination)