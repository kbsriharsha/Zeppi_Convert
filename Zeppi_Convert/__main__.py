import sys
import argparse
import os
import json
import codecs

# parser for general
def zeppi_all(zeppi_ntbk):
    py_scrt = []
    try:
        for i in zeppi_ntbk['paragraphs']:
            pgm = i["text"].splitlines()
            ident = pgm[0]
            code = pgm[1:]
            if ('%' in ident):
                pgm = '\n'.join(code)
                py_scrt.append(pgm)
            else:
                pgm = '\n'.join(pgm)
                py_scrt.append(pgm)
        final_text = '\n\n'.join(py_scrt)
    except ValueError:
        print('ERROR: Wrong file format')
        sys.exit(1)
    return final_text

# parser for interpreter specific
def zeppi_int(zeppi_ntbk, interpreter):
    int_scrt = []
    try:
        for i in zeppi_ntbk['paragraphs']:
            pgm = i["text"].splitlines()
            ident = pgm[0][1:]
            code = pgm[1:]
            if ((ident == interpreter) and (len(code) > 0)):
                code = '\n'.join(code)
                int_scrt.append(code)
        final_text = '\n\n'.join(int_scrt)
    except ValueError:
        print('ERROR: Wrong file format')
        sys.exit(1)
    return final_text

# Saving back to file
def sav_file(text, outfile = None):
    if outfile is None:
        outfile = "zeppiconvert.txt"
    try:
        with open(outfile, 'w') as output_file:
            output_file.write(text)
    except ValueError:
        print('Error Opening the output File')
        sys.exit(1)
    return True

def main():
    # Specifying the arguments to be passed
    parser = argparse.ArgumentParser(description = 'Type your input and output file locations')
    parser.add_argument('-i', \
                        dest = 'in_file', \
                        required = True, \
                        help='input file (.json format)')
    parser.add_argument('-o', \
                        dest = 'out_file', \
                        required = False, \
                        help='Output file location')
    parser.add_argument('-int', \
                        dest = 'interpreter', \
                        required = False, \
                        help='Type the particular interpreter')

    # Collecting the arguments
    args = parser.parse_args()
    input_filename = args.in_file
    output_filename = args.out_file
    interpreter = args.interpreter
    print(os.getcwd())

    try:
        os.path.exists(input_filename)
    except:
        print("Please check input file location")
        sys.exit()

    try:
        zeppi_ntbk = json.load(codecs.open(args.in_file, 'r', 'utf-8-sig'))
    except ValueError:
        print('ERROR: Invalid JSON')
        sys.exit(1)

    # Parsing the json script depending on the interpreter argument

    if interpreter == None:
        text = zeppi_all(zeppi_ntbk)
        save = sav_file(text, output_filename)
    else:
        text = zeppi_int(zeppi_ntbk, interpreter)
        save = sav_file(text, output_filename)

    print("Job Completed")

if __name__ == '__main__':
    main()


'''
args = sys.argv[1:]
print('count of args :: {}'.format(len(args)))
for arg in args:
    print('passed argument :: {}'.format(arg))
'''
