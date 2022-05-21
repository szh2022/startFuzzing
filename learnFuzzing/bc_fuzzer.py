import os.path
from fuzzer import fuzzer,runner
"""# a fuzzing of bc """

# tempfile is the name of dir ,base is the name of file
tempfile = "/home/zouyu/"
basename = "input"
FILE = os.path.join(tempfile, basename)

for i in range(100):
    data = fuzzer()
    with open(FILE, "w") as f:
        f.write(data)
    f.close()
    result = runner("/usr/bin/bc",FILE)
    print(result.stderr)


