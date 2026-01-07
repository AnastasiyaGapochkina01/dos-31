file_name = "file.txt"

with open(file=file_name, encoding='utf-8', mode='r',) as f:
    data = f.readlines()
  

with open(file="new_file.txt", mode='a', encoding='utf-8') as f:
    f.write("\nSome line 3")


with open(file=file_name, mode='r', encoding='utf-8') as infile, open(file="file-copy.txt", mode='a', encoding='utf-8') as outfile:
    outfile.write(infile.read())