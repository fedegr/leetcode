from typing import Optional, List
import os
from pathlib import Path


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


def create_file(number: int, name: str):
    name_formatted = '-'.join(name.lower().split())
    fullname = str(number) + '-' + name_formatted
    file_path = root / 'python' / (fullname + '.py')
    open(file_path, 'a').close()

    return file_path


if __name__ == '__main__':
    root = Path(os.path.abspath(__file__)).parent.parent
    import sys
    import json

    plan = sys.argv.get[1] if len(sys.argv) > 1 else 'leetcode-75'

    plan_prefix = 'plan-'
    plan_suffix = '.md'
    
    last_group = None
    plan_path = root / 'study-plans' / f'{plan}.json'
    plan_md_path = root / f'{plan_prefix}{plan}{plan_suffix}'

    with (
        open(plan_path) as plan_file,
        open(plan_md_path, 'a') as readme,
    ):
        d = json.load(plan_file)
        plan_data = d['data']['studyPlanV2Detail']

        lines = []

        lines.append('# ' + plan_data['name'])
        lines.append(plan_data['description'])
        lines.append('')

        for group in plan_data['planSubGroups']:
            lines.append('## ' + group['name'])
            lines.append('| Question | Difficulty | Solution |')
            lines.append('| -------- | ---------- | -------- |')
            for question in group['questions']:
                file_path = create_file(question['id'], question['title'])
                row = [
                    md_link(question['title'], f"https://leetcode.com/problems/{question['titleSlug']}/description/"),
                    question['difficulty'].capitalize(),
                    md_link('Python', './' + str(file_path.relative_to(root))),
                ]
                lines.append(f"| {' | '.join(row)} |")
            lines.append('')

        print('\n'.join(lines), file=readme)

