import time
import random

version = 'v1.0.00'

class Node:
    def __init__(self, name, _children = []):
        self.name = name
        self.children = {}
        self.parent = None
        
        for child in _children:
            self.add(child)
    
    @property
    def path(self):
        if self.parent is None:
            return self.name
        return f'{self.parent.path}\{self.name}'
    
    def __str__(self):
        return self.path

    def add(self, child):
        child.parent = self
        self.children[child.name] = child

    def cd(self, name) -> "Node":
        return self.children[name]

ROOT = Node('ROOT', [
    Node('DOORSOS', [
        Node('USERS', [
            Node('GUEST'),
            Node('ADMIN')
        ])
    ])
])

current_dir = ROOT.cd("DOORSOS").cd("USERS")

def status_bar(percent):
    loaded = '=' * percent
    remaining = ' ' * (100 - percent)

    print(f'[{loaded}{remaining}] {percent}%')

def open():

    print(f'DOORS OS {version}')
    time.sleep(0.2)
    print(f'LOADING...')

    load_status = 0

    while load_status < 100:
        status_bar(load_status)
        load_status += random.randint(10, 30)

    status_bar(100)
    print('LOADING COMPLETE')
    print('READY TO PROCEED')

open()

while True:

    command = input(f'{current_dir} >>>')

    args = command.split(' ')

    if command == 'HELP':
        print('''--------HELP--------
--------COMMANDS--------
SHUTDOWN: DURATION:INT -> NULL
    PREFORM SYSTEM SHUTDOWN AND WAKEUP IN [DURATION] MILLISECONDS
ECHO: ARG1 ARG2 ARG3 ARG4... -> NULL
    PRINTS ALL ARGUMENTS''')

    if 'SHUTDOWN' in command:
        print('INITIALIZING SHUTDOWN')

        try:
            restart_time = int(args[1])
        except:
            break

        time.sleep(restart_time/1000)

        open()

    if 'ECHO' in command:
        for arg in args:
            if arg == 'ECHO':
                pass
            else:
                print(arg)

    if 'LS' in command:
        print(f'''{current_dir}
--------
{current_dir.children}''')