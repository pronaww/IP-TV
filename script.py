import os

f = open("BD IPTV.m3u", "r")

lines = f.read().split("\n")

names = []
links = []

for line in lines:
    if line == "#EXTM3U":
        continue
    if line[0]=='#':
        # print(line)
        names.append( line.split(",")[1] )
    else:
        links.append(line)

thisdict = {}

for i in range(len(names)):
    thisdict[links[i]] = names[i]

final_list = "#EXTM3U\n"

for x in thisdict:
    final_list = final_list + "#EXTINF:-1 ," + thisdict[x] + "\n" + x + "\n"
    # print(x), print(" "), print(thisdict[x])

f = open("new file.m3u", "w")
f.write(final_list)
f.close()
# final_list.write("new list.m3u")