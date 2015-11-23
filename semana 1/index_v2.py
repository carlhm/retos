import sys
import csv
import string

path_in  = sys.argv[1]
path_out = sys.argv[2]

fr           = open(path_in, 'rb')
lines_in_csv = csv.reader(fr)
out_csv      = ''

pre_match = ['n00,n01,A\n','n10,n11,B\n']

for index,line in enumerate(lines_in_csv) :


    if not line[0].isdigit() or not 'TRUE' in line :
        continue

    true_pos = line.index('TRUE')
    ab       = int(true_pos > 2)
    match    = 'n' + str(ab) + str((true_pos - 1) % 2) + ''

    if not match in out_csv :
        out_csv += pre_match[ab]

    out_csv = out_csv.replace(match, line[0], 1)

out_csv = out_csv.replace('n00','0')
out_csv = out_csv.replace('n01','0')
out_csv = out_csv.replace('n10','0')
out_csv = out_csv.replace('n11','0')

fw = open(path_out,'wb')
fw.write(out_csv)
fw.close()
