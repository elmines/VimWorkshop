import sys
filename = sys.argv[1]
badLine = 53742
with open(filename, "w") as w:
	w.write("//There's a ; missing on line {0}, but you can open up this file like so to fix it: vim {1} +{0}\n".format(badLine, filename))
	w.write("//But since you're already in the file, you can just hit :{0} to go to the exact line.\n".format(badLine))
	w.write("#include<stdio.h>\n")
	w.write("int main(void){\n")
	for i in range(5, 100000):
		w.write("     printf(\"Alabama has the best football team ever!!!\\n\")")
		if i != badLine:
			w.write(";\n")
		else:
			w.write("\n")
	w.write("     return 0;\n")
	w.write("}\n")
	sys.stdout.close()
