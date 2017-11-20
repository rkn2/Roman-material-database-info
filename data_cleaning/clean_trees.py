import csv

first = True;

def getLoHiUnit(string):
    a = string.find('(') + 1
    b = string.find(')')
    sub = string[a:b]
    c = sub.find('-')
    d = sub[c:].find(' ') + c
    lo = sub[:c].strip(' ').strip('-')
    hi = sub[c:d].strip(' ').strip('-')
    unit = sub[d:].strip(' ').strip('-')
    return [lo,hi,unit]

def getValUnit(string):
    a = string.find('(') + 1
    b = string.find(')')
    sub = string[a:b]
    c = sub.find(' ')
    d = sub[c:].find(' ') + c
    val = sub[:c].strip(' ').strip('-')
    unit = sub[d:].strip(' ').strip('-')
    return [val,unit]

def rowToCSV(row):
    newRow = []
    for item in row:
        newRow.append('"%s"'%str(item))
    return newRow

newRows = [];
with open ('output.csv') as fid:    
    reader = csv.reader(fid,delimiter=',',quotechar='"')
    for row in reader:
        if first and len(row) > 0:
            headers = row;
            first = False;
            continue
        try:
            # parse sizes (height, diameter)
            sizes = row[3].split(',')
            tall = getLoHiUnit(sizes[0])
            diam = getLoHiUnit(sizes[1])
            sizes = []
            sizes.extend(tall)
            sizes.extend(diam)
            del row[3]
            row.insert(3,sizes)
            # parse miscellaneous other properties
            for i in range(4,9):
                vals = getValUnit(row[i])
                del row[i]
                row.insert(i,vals)
            # parse shinkage
            shrinkages = []
            for s in row[9].split(','):
                shrinkages.extend(getValUnit(s.strip(' ')))
            del row[9]
            row.insert(9,shrinkages)
            # expand list
            cleaned = []
            for item in row:
                if type(item) == type([]):
                    cleaned.extend(item)
                else:
                    cleaned.append(item)
            newRows.append(rowToCSV(cleaned))
        except:
            pass
    
with open('output_cleaned.csv','w') as fid:    
    for row in newRows:
        fid.write(','.join(row)+'\n')