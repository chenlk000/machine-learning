import re
fin = open("./temp.txt",'r+')
fout = open('./fuck.txt','w')
count = 0
pattern1 = re.compile(r'(\d+) -> Train ', re.M | re.I)
pattern2 = re.compile(r'(\d+).(\d+)', re.M | re.I)
pattern3 = re.compile(r'(\d+).(\d+)', re.M | re.I)
fout.write('iter loss score\n')
for s in fin.readlines():
    # print(s)
    matchObj1 = pattern1.search(s)
    if(matchObj1):
        matchObj2 = pattern2.search(s, matchObj1.span()[1])
        if(matchObj2):
            matchObj3 = pattern3.search(s, matchObj2.span()[1])
            sout = '{ite} {loss} {MAP}\n'.format(ite=matchObj1.group(1), loss=matchObj2.group(),MAP=matchObj3.group())
            fout.write(sout)

        # print(matchObj1.group(1))
        # print(matchObj2.group())
fin.close()
fout.close()