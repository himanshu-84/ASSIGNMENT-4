data = input("Enter data: ")
with open("output.txt", "w") as f:
    f.write(data + "\n")
extra = input("Enter more data: ")
with open("output.txt", "a") as f:
    f.write(extra + "\n")


with open("output.txt", "r") as f:
    print("\nFinal file content:")
    print(f.read())