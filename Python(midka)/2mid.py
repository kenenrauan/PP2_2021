with open("test.txt", 'r') as f, open("output.txt", "w") as f2:
    data = f.readlines()
    for index in range(1, len(data)):
        if len(data[index]) <= len(data[index-1]):
            f2.write("No");
            exit(0)
    f2.write("Yes")