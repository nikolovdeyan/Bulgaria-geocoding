

def normalize_column(infile, outfile):
    with open(infile) as src, open(outfile, 'w') as dest:
        curr_name = None
        curr_ekt = None
        for line in src:
            curr_name = line.split(',')[0]
            curr_ekt = line.split(',')[1]
            children_ekts = line.split(',')[2].rstrip().split(' ')
            for ch in children_ekts:
                result = f'{curr_name};{curr_ekt};{ch}\n'
                dest.write(result)


          
if __name__ == '__main__':
    input_file = 'settlements_grounds_relationships.csv'
    output_file = 'fixed_relationships.csv'

    normalize_column(input_file, output_file)
