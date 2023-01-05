import re
line1 = "Match this. And match this!"
matchObj1 = re.search('this', line1)
if matchObj1:
    print(matchObj1.group())
else:
    print("No match!")


line2 = """The numbers 172 can be found on the back of the U.S. $5
dollar bill in the bushes at the base
of the Lincoln Memorial."""
matchObj2 = re.findall('\d+', line2)
if matchObj2:
    print(matchObj2)
else:
    print("No match!")

line3 = """__yellow__ __red__ and __blue__ are colors"""
matchObj3 = re.findall('__.*?__', line3)
if matchObj3:
    print(matchObj3)
else:
    print('No match!')
