import argparse
from pathlib import Path

get_value = lambda a: a.split('\t')[1]

parser = argparse.ArgumentParser()
parser.add_argument('--true_dir', help='true folder path', required=True, type=Path)
args = parser.parse_args()

true_dir = Path(args.true_dir)
with open('data/gt/words.txt', 'w') as _file:
    for _name in true_dir.iterdir():
        content = open(_name, 'r').read()
        lines = content.split('\n')
        _file.write(';'.join(map(get_value, (lines[2], lines[1])))+'\n')

