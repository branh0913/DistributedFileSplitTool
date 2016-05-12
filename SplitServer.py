import itertools

import argparse

'''
Beginning of project which will become a file distribution split solution.
'''


class SplitUtil:

    def split_file(self, input_file, split_length, prefix_name):

        with open(input_file, 'r') as split_file:

            file_no = 1
            for i in range(0, sum(1 for x in open(input_file)), split_length):
                for line in itertools.islice(split_file, i, i+split_length):
                    with open(prefix_name+str(file_no), 'a') as output_file:
                        output_file.write(line)
                file_no += 1

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="File Split tool")
    parser.add_argument('-file', '--file', help="Enter the file")
    parser.add_argument('-split', '--split', help="Enter the split of the file you want to make")
    parser.add_argument('-prefix', '--prefix', help="Name of the files that are split")
    args = parser.parse_args()

    split_inst = SplitUtil()

    split_inst.split_file(args.file, int(args.split), args.prefix)

