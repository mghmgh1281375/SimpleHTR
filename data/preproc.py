
from pathlib import Path

get_value = lambda a: a.split('\t')[1]

true_dir = Path('/home/mohammad/Projects/SRU_PHN/data/true/')
with open('data/dataset/gt/words.txt', 'w') as _file:
    for _name in true_dir.iterdir():
        content = open(_name, 'r').read()
        lines = content.split('\n')
        _file.write(';'.join(map(get_value, (lines[2], lines[1])))+'\n')

