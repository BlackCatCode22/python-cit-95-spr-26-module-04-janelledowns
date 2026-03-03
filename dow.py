han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    if len(wds) or < 3 wds[0] != 'From :
        continue
    print(wds[2])
