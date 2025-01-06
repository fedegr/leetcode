from typing import Optional, List
import datetime, os
from pathlib import Path

def read_input(prompt: str, default: Optional[str] = None, options: List[str] = None):
    if default is not None:
        prompt += f' [{default}]'
    value = ''
    while value == '':
        value = input(f"{prompt}: ").strip()
        if value == '' and default is not None:
            value = default
        if options is not None and value not in options:
            value = ''
            print(f'Invalid paramter. Valid options: {options}')
    return value


def md_link(name, url):
    return f"[{name}]({url})"


if __name__ == '__main__':
    default_day = datetime.date.today().isoformat()
    day = read_input(f"day", default_day)
    title = read_input('title')
    difficulty = read_input('difficulty', "Medium")
    
    number, name = title.split('.')
    name_formatted = '-'.join(name.lower().split())
    fullname = number + '-' + name_formatted
    
    link = f"https://leetcode.com/problems/{name_formatted}/description/"
    root = Path(os.path.abspath(__file__)).parent.parent
    file_path = root / 'python' / (fullname + '.py')

    open(file_path, 'a').close()

    with open(root / 'README.md', 'a') as readme:
        row = [
            day,
            md_link(name, link),
            difficulty,
            md_link('Python', './' + str(file_path.relative_to(root))),
        ]
        print(f"| {' | '.join(row)} |", file=readme)

