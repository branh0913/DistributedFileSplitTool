import itertools

'''
Beginning of project which will become a file distribution split solution.
'''


with open('input.txt', 'r') as split_file:

    file_no = 1
    for i in range(0, sum(1 for x in open('input.txt')), 100):
        for line in itertools.islice(split_file, i, i+100):

            with open('output_tex'+str(file_no), 'a') as output_file:

                output_file.write(line)

        file_no += 1


