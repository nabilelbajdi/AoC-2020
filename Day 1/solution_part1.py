#read input file
file = open("input")
test_input = file.read()
file.close()

#split input into seperate lines
test_input = test_input.splitlines()

#convert list of str to int
data = []
for elem in test_input:
    data.append(int(elem))

done = False

#solution
for n1 in data:
    for n2 in data:
        if n1 + n2 == 2020:
            print(n1 * n2)
            done = True
            break
    if done:
        break