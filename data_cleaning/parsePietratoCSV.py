# List of wanted_fields we want
# Imports
import csv

# The fields we want
wanted_fields = ['Stone Name', 'Alternate Name(s)', 'Petrographic Definition/Details',
                 'Age', 'Appearance and Composition', 'General Density',
                 'Elastic Modulus', 'Poissons Ratio',
                 'Flexural Strength', 'Compressive Strength', 'Water Absorption',
                 'Quarry Location(s)', 'Dates of Use'
                ]
# List of dictionaries with wanted_fields
output_list = []

"""
This section of the script pulls in data from the parsed file and parses it based
on the delimiters in roman_tree.py. It assumes that everything in the scrape
worked correctly, so some html may slip through.  The final output is a Python
dict for each line that then is appended to a list.

By shifting indents these could easily be functionalized for repeated use.
"""
# Open file using 'with' so that it closes cleanly
with open('pietra.txt', encoding='utf-8') as f:
    for line in f:
        # Define rolling variables for string cuts and an aggregated dict
        start_cut = 0
        end_cut = 0
        aggregated_dict = {}
        for i in range(len(wanted_fields)):
            # Handle the first instance on a line
            if start_cut == 0:
                start_cut = line.find(":::")
                start_cut += 3
                end_cut = line.find(";;;")

                aggregated_dict[wanted_fields[i]] = line[start_cut:end_cut]
            # Handle all subsequent instances using previous start_ and end_cuts
            else:
                start_cut = line.find(":::", end_cut)
                end_cut += 1
                start_cut += 3
                end_cut = line.find(";;;", end_cut)

                aggregated_dict[wanted_fields[i]] = line[start_cut:end_cut]
        # Append the dict
        output_list.append(aggregated_dict)

"""
This section uses the csv module to write the dict to a standard CSV file that
defaults to settings Excel likes to see.
"""
# Open file
with open('pietra_output.csv', 'w') as csvfile:
    # Invoke the csv.Dictwriter as 'writer'
    writer = csv.DictWriter(csvfile, fieldnames=wanted_fields)

    # Write the header line
    writer.writeheader()

    # Loop through the list of dictionaries and write each to a line
    for dictionary in output_list:
        writer.writerow(dictionary)
