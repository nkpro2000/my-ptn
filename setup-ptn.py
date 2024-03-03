#TODO add shebang with proper python env.
# This is the first file to run after cloning so that all are configured as intended.
# See comments ######### for steps involved in this process done by this script.
# Will be run by user like `python setup-ptn.py`, after cloning this repo (follow README.md).

import os

PTN = '/ptn/'
PTN_GIT = PTN+ '.'+os.environ['USER'] +'/PtnTable_git/'


# Making Dirs and Symlinking
#############################
#/ptn/
##├── _ (meta)    info/detail files
##├── b (binary)  /0001  /0100  /1001  ...
##├── d (decimal) /1     /4     /9     ...
##├── r (Label)   /LiveO /WinOS /LBuVM ...
##├── s (label)   /liveo /winos /lbuvm ...
##├── x (extra)   /tmp /ram ...
##├── 1 (first partition)
##├── l (linux)   /bak
##├── w (windows) /main  /esp
##└── v (ventoy)  /main  /esp
TREE = (
    ( 1, 'LiveO', 'drb'),
    ( 2, 'VTESP', 'drb'),
    ( 3, 'EFISP', 'drb'),
    ( 4, 'WinOS', 'drb'),
    ( 5, 'WinRP', 'drb'),
    ( 6, 'WinSP', 'drb'),
    ( 7, 'MSwRP', 'drb'),
    ( 8, 'Linux', 'drb'),
    ( 9, 'LBuVM', 'drb'),
    ( 0, 'LinEx', 'r'), # not yet decided '#'
)
ops = []
rops = []
for i in 'bdrs':
    ops.append(f'mkdir -p {PTN}{i}')
    rops.append(f'rm {PTN}{i}/*')
    rops.append(f'rmdir {PTN}{i}/')
for d, r, dirs in TREE:
    b = bin(d)[2:].zfill(4)
    s = r.lower()
    ops.append(f'ln -sf /dev/disk/by-label/{r} {PTN}s/{s}')
    for i in dirs:
        ops.append(f'ln -sf ../s/{s} {PTN}{i}/{locals()[i]}')
for i in 'lwv':
    ops.append(f'mkdir -p {PTN}{i}')
for i in ['1', 'l/bak', 'w/main', 'w/esp', 'v/main', 'v/esp']:
    ops.append(f'mkdir -p {PTN}{i}')
    rops.append(f'rmdir {PTN}{i}')
for i in 'lwv':
    rops.append(f'rmdir {PTN}{i}')

script = r'''# shellcheck shell=sh

#rm -rf /ptn/* ## not safe if mounted

# Removing tree
'''
script+= '\n'.join(rops)
script+= '''

# Creating dir/link tree
'''
script+= '\n'.join(ops)

with open(PTN_GIT+'ops-todo.sh', 'w') as f:
    f.write(script)
print('I> To run bash Script to create the dir/link tree')
print('$> sh> sudo bash '+ PTN_GIT+'ops-todo.sh # Ctrl+D to skip')
os.system('sudo bash '+ PTN_GIT+'ops-todo.sh')
os.system('rm '+ PTN_GIT+'ops-todo.sh')

os.system('sudo cp '+ PTN_GIT+'mnt ' +PTN)
os.system('sudo chmod +x '+ PTN+'mnt')

os.system('sudo -K')
