"""File Handling in Python
File handling is an essential aspect of programming that allows you to read from and write to files on your system.
Python provides built-in functions and methods to work with files easily.
Common file operations include opening a file, reading from it, writing to it, and closing it.
Files can be opened in different modes, such as read ('r'), write ('w'), append ('a'), and binary modes ('rb', 'wb').
It's important to properly close files after operations to free up system resources.
Using the 'with' statement is a best practice for file handling, as it automatically handles closing the file for you.
"""

# File modes (quick notes)
# r  -> read
# w  -> write (overwrite)
# a  -> append
# x  -> create only
# r+ -> read + write
# w+ -> write + read
# a+ -> append + read
# b  -> binary mode

# Writing some content
with open("sample.txt", "w") as f:
    f.write("Python File Handling\n")
    f.write("Learning read and write\n")
    f.write("Line three here\n")

# Append content
with open("sample.txt", "a") as f:
    f.write("This line is appended\n")

# read() -> reads entire file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# read(n) -> reads specific number of characters
with open("sample.txt", "r") as f:
    chars = f.read(10)
    print(chars)

# readline() -> reads one line at a time
with open("sample.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)

# readlines() -> reads all lines into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# iterating through file using loop (best for large files)
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# tell() -> current cursor position
with open("sample.txt", "r") as f:
    print("Cursor position:", f.tell())
    f.read(5)
    print("After reading 5 chars:", f.tell())

# seek() -> move cursor to specific position
with open("sample.txt", "r") as f:
    f.seek(0)
    print("After seek:", f.read(10))

# Binary file example (image, pdf, etc.)
# with open("photo.jpg", "rb") as f:
#     data = f.read()
#     print(type(data))  # bytes
#     print(len(data))
