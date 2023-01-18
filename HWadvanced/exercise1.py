def writefile(filename):
    with open(filename, "w")as file:
        file.write("Hi every one,'\n")
        file.write("my name is Hadeel Hassan'\n")
        file.write("I am 31 years old\n")
        file.write("my phone number 0525787713\n")

writefile("my_id.txt")