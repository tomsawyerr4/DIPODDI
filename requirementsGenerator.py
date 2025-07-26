import os
import re

def extract_dependencies(directory):
    deps = set()
    pattern = re.compile(r'^\s*import (\S+)|^\s*from (\S+) import')

    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        mod = match.group(1) or match.group(2)
                        base_mod = mod.split('.')[0]
                        deps.add(base_mod)

    return deps

# Exemple d'utilisation
modules = extract_dependencies(".")
with open("requirements.txt", "w", encoding="utf-8") as f:
    for module in sorted(modules):
        f.write(f"{module}\n")

print("✅ requirements.txt généré !")
