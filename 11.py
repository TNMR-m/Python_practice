from sys import argv

with open(argv[1], encoding="utf-8") as f:
    f_str = f.read()

f_str_2 = f_str.replace('\t',' ')

print(f_str_2)