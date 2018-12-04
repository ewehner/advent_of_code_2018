def find_checksum(data):

    two_letters = 0
    three_letters = 0
    exactly_two = False
    exactly_three = False

    for s in data:
        l = list(s)
        l.sort()

        while l:
            first_letter = l[0]
            letter_count = l.count(first_letter)
            if letter_count == 2:
                exactly_two = True
            elif letter_count == 3:
                exactly_three = True
            l = l[letter_count:]

        if exactly_two:
            two_letters += 1
            exactly_two = False
        if exactly_three:
            three_letters += 1
            exactly_three = False

    return two_letters * three_letters

def find_matches(data):

    for i in range(len(data)-1):
        current_id = data[i]

        for j in range(i+1, len(data)):
            current_test_id = data[j]
            number_different = 0
            diff_location = 0

            for k in range(len(current_id)):
                if current_id[k] != current_test_id[k]:
                    number_different += 1
                    if number_different > 1:
                        break
                    diff_location = k

            if number_different == 1:
                index_id_1 = i
                index_id_2 = j
                break

    id_1 = data[index_id_1]

    print("ID 1: {}".format(id_1))
    print("ID 2: {}".format(data[index_id_2]))
    print("Index of difference: {}".format(diff_location))

    return id_1[:diff_location] + id_1[diff_location+1:]

if __name__ == '__main__':

    input_file = open("day2_input.dat", "r")
    data = input_file.readlines()
    input_file.close()

    print("Day 2 Puzzle 1: ")
    print("The checksum is: {}\n".format(find_checksum(data)))

    print("Day 2 Puzzle 2: ")
    print("The common ID letters are: {}".format(find_matches(data)))
