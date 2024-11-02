import re
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<t*>", "ELEPHANTS", string)
print(string)