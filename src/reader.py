als=""
ai=[]
final=[]
data = open("tester")
deta = data.read().splitlines()
data.close()
print(deta)
temp=""
for i in deta:
    if "    " in i or "	" in i:
	if "    " in i:
	    temp = i.replace("    ","\t")
	else:
	    temp = i.replace("	","\t")
    else:
	temp= i
    ai.append("\n"+temp)
final.append("".join(ai))
print(final)
