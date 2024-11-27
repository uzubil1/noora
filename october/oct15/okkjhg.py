import re

for match in re.findall("\d[a-z]","1ab23c"):
    print(match)

if re.findall("\d[a-z]", "1abcdef"):
         print("Found at least one match!")
else: 
      print("No match!")