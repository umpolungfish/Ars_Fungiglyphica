#!/usr/bin/env python3
"""Fix generated types.py: add missing closing '",' to description lines."""
import re, sys

path = sys.argv[1] if len(sys.argv) > 1 else 'ars_fungiglyphica/types.py'
with open(path, 'r') as f:
    content = f.read()

# Pattern: a line that starts with 4+ spaces, then a "description string that ends with ."
# followed by a newline then spaces then [
# The description is missing its closing ", before the list
# Fix: append ", to description lines that precede a list line
lines = content.split('\n')
fixed = []
for i, line in enumerate(lines):
    stripped = line.strip()
    # If this looks like a description line (indented, starts with ") 
    # and the next non-empty line starts with a list [ 
    if (len(line) - len(line.lstrip()) >= 4 and 
        stripped.startswith('"') and 
        not stripped.endswith('",') and
        not stripped.endswith('"""')):
        # Check if next line is a list
        next_line = ''
        for j in range(i+1, min(i+3, len(lines))):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
        if next_line.startswith('['):
            line = line.rstrip()
            if not line.endswith('"'):
                line = line + '"'
            line = line + ','
    fixed.append(line)

with open(path, 'w') as f:
    f.write('\n'.join(fixed))
print(f"Fixed {path}")
