import  re
pattern = r"([A-Z]+)(\d+)([A-Z]+)"
frolls = open('rollnos.txt','r')
a = frolls.read()
string = a
matches = re.findall(pattern, string, flags=0)
fo = open("123.txt",'a+')
for match in matches:
	fo.write(''.join(match)+'\n')