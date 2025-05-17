try:
    file_name = input("Enter file name: ")
    file = open(file_name, 'r')
    text = file.read()
    words = text.split()
    print("Total words:", len(words))
    file.close()
except FileNotFoundError:
    print("File not found. Please check the name.")
