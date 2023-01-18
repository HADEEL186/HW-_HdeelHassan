def countappear(a):
    dict1 = {}
    with open(a,"r") as file:
        readtxt = file.read()
        lines = readtxt.split()
    for word in lines:
            if word in dict1:
                dict1[word] +=1
            else:
                dict1[word] = 1
    return dict1
print(countappear("text.txt"))
