import os
from pathlib import Path
from datetime import datetime

# Save original working directory and use pathlib for operations
original_dir = Path.cwd()
print(f"Original directory: {original_dir}")

# exercise 1: Get current working directory
print("Exercise 1: current working directory:")
print(Path.cwd())

# exercise 2: Change into 'projects' (create if missing)
projects = Path('projects')
projects.mkdir(exist_ok=True)
os.chdir(projects)
print('\nExercise 2: changed into', Path.cwd())

# exercise 3: List directory contents
print('\nExercise 3: directory listing:')
print(os.listdir())
for child in Path('.').glob('*'):
    print(' -', child)

# exercise 4: Create a directory 'data'
print('\nExercise 4: creating data dir')
Path('data').mkdir(exist_ok=True)
print('data exists:', Path('data').exists())

# exercise 5: Create nested directories a/b/c
print('\nExercise 5: creating nested directories a/b/c')
Path('a/b/c').mkdir(parents=True, exist_ok=True)
print('a contents:', [p.name for p in Path('a').iterdir()])

# exercise 6: Remove a file named temp.txt (create it first to demonstrate)
print('\nExercise 6: create and remove temp.txt')
Path('temp.txt').write_text('temporary')
print('temp.txt exists before remove:', Path('temp.txt').exists())
Path('temp.txt').unlink()
print('temp.txt exists after remove:', Path('temp.txt').exists())

# exercise 7: Remove an empty directory 'old_data' (create then remove safely)
print('\nExercise 7: create and remove old_data')
old = Path('old_data')
old.mkdir(exist_ok=True)
print('old_data exists before remove:', old.exists())
old.rmdir()
print('old_data exists after remove:', old.exists())

# exercise 8: Rename example.txt to renamed_example.txt (create file first)
print('\nExercise 8: rename example.txt to renamed_example.txt')
Path('example.txt').write_text('example')
Path('example.txt').rename('renamed_example.txt')
print('renamed exists:', Path('renamed_example.txt').exists())

# exercise 9: Check whether 'target' is a file or directory
print('\nExercise 9: check target type')
# create a directory target and a file target_file to demonstrate both checks
Path('target').mkdir(exist_ok=True)
Path('target_file').write_text('file')
print("'target' is_dir:", Path('target').is_dir())
print("'target' is_file:", Path('target').is_file())
print("'target_file' is_file:", Path('target_file').is_file())

# Return to original directory
os.chdir(original_dir)
print('\nReturned to original directory:', Path.cwd())



# Exercise 10: Create and write to log.txt
print('\nExercise 10: create and write to "log.txt"')
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('First log line\n')
print('Wrote to log.txt')

# Exercise 11: Read the file
print('\nExercise 11: read "log.txt"')
with open('log.txt', 'r', encoding='utf-8') as f:
    print(f.read().rstrip('\n'))

# Exercise 12: Append a line
print('\nExercise 12: append to "log.txt"')
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('Second log line\n')
with open('log.txt', 'r', encoding='utf-8') as f:
    print(f.read().rstrip('\n'))

# Exercise 13: Write multiple lines to 'multi.txt'
print('\nExercise 13: write multiple lines to "multi.txt"')
lines = ['line one\n', 'line two\n', 'line three\n']
with open('multi.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Wrote 3 lines to multi.txt')

# Exercise 14: Read 'multi.txt' line by line
print('\nExercise 14: read "multi.txt" line by line')
with open('multi.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.rstrip()}")

# Exercise 15: Count lines
print('\nExercise 15: count lines in "multi.txt"')
with open('multi.txt', 'r', encoding='utf-8') as f:
    count = sum(1 for _ in f)
print('Line count:', count)

# Exercise 16: Read a file safely
print('\nExercise 16: safe read of "maybe_missing.txt"')
try:
    with open('maybe_missing.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('maybe_missing.txt does not exist — handled safely.')

# Exercise 17: Use pathlib to read/write
print('\nExercise 17: pathlib read/write')
pfile = Path('pathlib_example.txt')
pfile.write_text('Hello from pathlib\n')
print('pathlib_example.txt contains:', pfile.read_text().rstrip())

# Stretch goal: print size and modification time of 'data.csv'
print('\nStretch: file size and last modified time for "data.csv"')
data_csv = Path('data.csv')
if not data_csv.exists():
    data_csv.write_text('a,b,c\n1,2,3\n')
stat = data_csv.stat()
print('Size:', stat.st_size, 'bytes')
print('Last modified:', datetime.fromtimestamp(stat.st_mtime).isoformat())

print('\nAll Hands-On exercises completed.')



# Beginner-friendly cleanup: remove demo files and empty demo directories
# Don't worry about this section; it's just to clean up after ourselves.
print('\nCleanup: removing demo files and attempting to remove empty demo directories')
cleanup_files = ['log.txt', 'multi.txt', 'pathlib_example.txt', 'data.csv']
for name in cleanup_files:
    p = Path(name)
    if p.exists() and p.is_file():
        try:
            p.unlink()
            print(f'Removed file: {name}')
        except Exception:
            print(f'Could not remove file: {name}')

# Clean up the 'projects' demo folder contents (safe removals only)
projects = Path('projects')
if projects.exists() and projects.is_dir():
    # files we created there
    for fname in ['renamed_example.txt', 'target_file', 'temp.txt', 'example.txt']:
        fp = projects / fname
        if fp.exists() and fp.is_file():
            try:
                fp.unlink()
                print(f'Removed file in projects: {fname}')
            except Exception:
                print(f'Could not remove file in projects: {fname}')
    # try to remove nested directories we created (a/b/c)
    a = projects / 'a'
    if a.exists() and a.is_dir():
        b = a / 'b'
        c = b / 'c'
        for d in (c, b):
            if d.exists() and d.is_dir():
                try:
                    d.rmdir()
                    print(f'Removed dir: {d}')
                except Exception:
                    pass
        try:
            a.rmdir()
            print(f'Removed dir: {a}')
        except Exception:
            pass
    # try to remove other simple dirs if empty
    for dname in ['data', 'old_data', 'target']:
        dp = projects / dname
        if dp.exists() and dp.is_dir():
            try:
                dp.rmdir()
                print(f'Removed dir in projects: {dname}')
            except Exception:
                pass
    # attempt to remove the projects dir itself (only if empty)
    try:
        projects.rmdir()
        print('Removed projects directory')
    except Exception:
        print('Projects directory not removed (may not be empty)')

print('Cleanup completed.')
