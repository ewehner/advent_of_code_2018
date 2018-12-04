if __name__ == '__main__':

    input_file = open("input_d01_p01.dat", "r")
    data = input_file.readlines()
    input_file.close()

    sum = 0
    num_loops = 0
    frequencies = []
    duplicate = False

    while duplicate is False:
        num_loops += 1
        print("Number of loops = {}".format(num_loops))
        for i in range(0, len(data)):
            sum += int(data[i])
            if sum in frequencies and duplicate is False:
                print("First frequency duplicated is: {}".format(sum))
                duplicate = True

            frequencies.append(sum)

    print("Puzzle 1: ")
    print("The final frequency is: {}".format(sum / num_loops))
