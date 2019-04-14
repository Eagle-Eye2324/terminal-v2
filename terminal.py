#!/usr/bin/env python


class Terminal:
    commands = {}
    name = ''
    __options = {
        'default_commands': True
    }

    def __init__(self, options, name = None,):
        if name is None:
            self.name = 'Terminal V2'
        else:
            self.name = name
        if 'default_commands' in options:
            self.__options['default_commands'] = options['default_commands']

