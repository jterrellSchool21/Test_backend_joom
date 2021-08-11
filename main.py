from heapq import merge
from itertools import count, islice
from contextlib import ExitStack
from random import randint
from os import remove, getcwd, path

def create_gen():
    i = 0
    while i < 1000000:
        i += 1
        yield randint(1, 10000000)

def create_file():
    integers = create_gen()
    with open('input.txt', 'w+') as f:
        for i in integers:
            f.write(str(i))
            f.write('\n')

def main(file_name):
    ch_names = []
    lines = (line for line in open(file_name, 'r'))
    for ch in count(1):
        srt_ch = sorted(islice(lines, 50000))
        if not srt_ch:
            break
        ch_name = f'tmp_f_{ch}'
        ch_names.append(ch_name)
        with open(ch_name, 'w+') as t:
            t.writelines(srt_ch)

    with ExitStack() as stack, open('output.txt', 'w') as f:
        files = [stack.enter_context(open(ch)) for ch in ch_names]
        f.writelines(merge(*files))

    for i in ch_names:
        remove(path.join(getcwd(), i))

if __name__ == '__main__':
    file_name = 'input.txt'
    create_file()
    main(file_name)