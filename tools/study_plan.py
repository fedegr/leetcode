from typing import Optional, List
import os
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


def get_titles(index_file, level=2):
    with open(index_file, 'r') as file:
        title_prefix = '#' * level + ''
        groups = []
        line = file.readline()
        while line != "":
            if line.startswith(title_prefix):
                groups.append(line[len(title_prefix):].strip())
            line = file.readline()
    return groups

if __name__ == '__main__':
    root = Path(os.path.abspath(__file__)).parent.parent


    plan_prefix = 'plan-'
    plan_suffix = '.md'
    
    plans = [
        f
        for f in os.listdir(root)
        if f.startswith(plan_prefix) and f.endswith(plan_suffix)
    ]
    plans.sort(key=lambda path: os.path.getmtime(f'./{path}'))
    plans = [p[len(plan_prefix):-len(plan_suffix)] for p in plans]

    plan = read_input(f"plan", plans[0]).lower()
    title = read_input('title')
    difficulty = read_input('difficulty', "Medium", options=["Easy", "Medium", "Hard"])

    last_group = None
    index_file = root / f'{plan_prefix}{plan}{plan_suffix}'
    if plan in plans:
        groups = get_titles(index_file)
        if len(groups) > 0:
            last_group = groups[-1]


    group = read_input('group', last_group)
    
    number, name = title.split('.')
    name_formatted = '-'.join(name.lower().split())
    fullname = number + '-' + name_formatted
    
    link = f"https://leetcode.com/problems/{name_formatted}/description/"
    file_path = root / 'python' / (fullname + '.py')

    open(file_path, 'a').close()

    with open(index_file, 'a') as readme:
        lines = []

        if plan not in plans:
            plan_name = ' '.join(plan.split('-'))
            lines.append('# ' + plan_name.capitalize() + ' problems')
            lines.append('Solutions for ' + plan_name + ' questions')

        if group != last_group:
            lines.append('')
            lines.append('## ' + group)
            lines.append('| Question | Difficulty | Solution |')
            lines.append('| -------- | ---------- | -------- |')


        row = [
            md_link(name, link),
            difficulty,
            md_link('Python', './' + str(file_path.relative_to(root))),
        ]
        lines.append(f"| {' | '.join(row)} |")
        print('\n'.join(lines), file=readme)

