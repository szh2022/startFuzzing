# char_start and char_range can control the format of string
# if want a string consisted of number:  char_start = ord('0')
import subprocess
import random


def fuzzer(max_length=100, char_start=32, char_range=32):
    str_len = random.randrange(0, max_length + 1)
    # get random len of string
    fuzzing = ""
    for i in range(0, str_len):
        fuzzing += chr(random.randrange(char_start, char_start + char_range))
    return fuzzing


# return the state of program, which can help us to know whether the program is crashed
# result.stdout
# result.stderr
# program: the path of object program
# FILE: the path of path of input data
def runner(program, FILE):
    result = subprocess.run([program, FILE],
                            stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    return result