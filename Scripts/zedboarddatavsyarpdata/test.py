import re, os

title = ["1.txt","10.txt","30.txt","60.txt","70.txt","90.txt","100.txt"]

path = "/home/icub/Desktop/sinewave3.3square"
files = os.listdir(path)

print title[1][0]

for fi in files:
    file = os.path.join(path, fi)
    text = open(file, "r")
'''
    for line in text:
        if re.match("(.*)(hasse|hasst)(.*)", line):
            hit_count = hit_count + 1
            print >>  hate, title[book] + "|" + line,

    print title[book] + " => " + str(hit_count)
    text.close()
'''