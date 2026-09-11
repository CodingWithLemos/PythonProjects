username = "andre.lemos"
n = 9000

fpath = f"C:\\users\\{username}\\downloads\\input.txt"

with open(fpath, "w") as file:

    def fibonacci(n):
        a, b = 0, 1
        while a < n:
            print(a, end=" ", file=file)
            a, b = b, a + b
        print("Reached EOF", file=file) 

    fibonacci(n)

print(f"Finished writing fibonacci sequence to file up to {n}.")

with open(fpath, "r") as file:
    data = file.read()
    print('The file content is:\n', data)

file.close()

