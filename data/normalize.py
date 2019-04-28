def normalize_column(infile, outfile):
    """
    Create a many-to-one relationship table from a multi-record column string.
    """
    with open(infile) as src, open(outfile, 'w') as dest:
        curr_ekt = None
        for line in src:
            curr_ekt = line.split(',')[0]
            # The parent always belongs to its respective grounds.
            children_ids = line.split(',')[1].rstrip().split(' ')
            for child_id in children_ids:
                if not child_id:
                    continue
                else:
                    child_rec = f'{curr_ekt};{child_id}\n'
                    dest.write(child_rec)


if __name__ == '__main__':
    input_file = 'settlements_grounds_relationships.csv'
    output_file = 'fixed_relationships.csv'

    normalize_column(input_file, output_file)
