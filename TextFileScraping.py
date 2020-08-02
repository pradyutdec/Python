
data = open('saksham.txt', mode='w').readlines()

for n, line in enumerate(data):
    if "Pradyut" in line:
            data[n] = "\n......pradyut encountered......"

    if line.startswith("Q") or line[0].isdigit():
        data[n] = "\n" + line.rstrip()

    if line.startswith("(a)"):
        data[n] = "\n" + line.rstrip()

    if line.startswith("(b)"):
        data[n] = "\n" + line.rstrip()
    if line.startswith("(c)"):
        data[n] = "\n" + line.rstrip()
    if line.startswith("(d)"):
        data[n] = "\n" + line.rstrip()

print " ".join(data)
