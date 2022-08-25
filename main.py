import csv
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

f = open("alphabet.csv", "a")


for h in range(0,26):
	f.write(alphabet[h])

for h in range(0,26):
	for i in range(0,26):
		f.write(alphabet[h]+alphabet[i]+"\n")

f.write("\n")

for h in range(0,26):
	for i in range(0,26):
		for j in range(0,26):
			f.write(alphabet[h]+alphabet[i]+alphabet[j]+"\n")

f.write("\n")

for h in range(0,26):
	for i in range(0,26):
		for j in range(0,26):
			for k in range(0,26):
				f.write(alphabet[h]+alphabet[i]+alphabet[j]+alphabet[k]+"\n")

f.close()