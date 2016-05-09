for i in range(10000):

    random_string = "Hello\n"
    with open("input.txt", 'a') as write_file:

        print("line written")
        write_file.write(random_string)