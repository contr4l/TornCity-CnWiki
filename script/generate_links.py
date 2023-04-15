
import re, os

def process(filename):

    if not os.path.exists(filename):
        return 

    res = set()
    with open(filename, encoding='utf8') as f:
        for line in f.readlines():
            tmp = re.findall("\[[^\]]*\]\([^)]*\.md\)", line)
            for i in tmp:
                res.add(i)

    for link in res:
        print("- " + link)

import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)

    process(sys.argv[1])