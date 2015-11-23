import sys
import csv
import string

path_in  = sys.argv[1]
path_out = sys.argv[2]

fr       = open(path_in, 'rb')
in_csv   = csv.reader(fr)
out_csv  = ''

pre_match = ['c00,c01,A\n','c10,c11,B\n']               # cAx, cAy, A | cBx, cBy, B -> posibles lines in the output

for index,line in enumerate(in_csv) :

    if not line[0].isdigit() or not 'TRUE' in line :    # Valid line -> Code as number & True between commas
        continue
                                                        # [code,Ax,Ay,Bx,By] -> [0,1,2,3,4] -> (-1) [0,1,2,3]
    true_pos = line.index('TRUE') - 1                   # find True into the array -> position
    ab       = int(true_pos > 1)                        # A: 0|1, B: 2|3 => (< 2) -> A -> 0, (>= 2) -> B -> 1
    match    = 'c' + str(ab) + str(true_pos % 2) + ''   # x: 0|2, y: 1|3 => %2 => c(A|B)(x|y) -> c(0|1)(0|1)

    if not match in out_csv :
        out_csv += pre_match[ab]

    out_csv = out_csv.replace(match, line[0], 1)        # replace c(0|1)(0|1) by the code

out_csv = out_csv.replace('c00','0')                    # replace all empty codes
out_csv = out_csv.replace('c01','0')
out_csv = out_csv.replace('c10','0')
out_csv = out_csv.replace('c11','0')

fw = open(path_out,'wb')                                # write output
fw.write(out_csv)
fw.close()
