def handle(argv):
    prop = properties()
    command_map = ('compile', 'test' , 'help')
    argv = argv[1:]
    if len(argv) == 0:
        raise Exception('scalu must be provided with a command to run: compile, test, help, etc')
    if argv[0] in command_map:
        prop.mode = argv[0]
    else:
        bad_arg(arg)
    return prop

def bad_arg(arg):
    raise Exception('A command has been provided that cannot be recognized: >>>> ' + arg + ' <<<<')


class properties():

    def __init__(self):
        self.mode = ''


