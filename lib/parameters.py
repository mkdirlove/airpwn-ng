## Python3
try:
    from queue import Queue, Empty
## Python2
except ImportError:
    from Queue import Queue, Empty

import binascii

class VictimParameters(object):
    """An instance of this class is always necessary to run the application

    This class holds your injections.

    Define victim detection parameters.
    For targeted mode, this is a property of Victim.
    For broadcast mode, this is a property of PacketHandler
    """

    def __init__(self, *positional_parameters, **keyword_parameters):
        self.inject_file = keyword_parameters.get('inject_file')
        self.in_request = keyword_parameters.get('in_request')
        self.in_request_handler = keyword_parameters.get('in_request_handler')
        self.covert = keyword_parameters.get('covert')
        if self.covert is None:
            self.covert = False

        if self.inject_file is None and self.in_request is None:
            print ('[ERROR] Please specify victim parameters')
            exit(1)

        if self.in_request is not None and self.inject_file is None:
            print ('[ERROR] You must select an inject file for use with in_request')
        else:
            if self.inject_file is not None:
                self.file_inject = self.load_injection(self.inject_file)
                self.file_injected = 0


    def load_injection(self, injectionfile):
        """Loads an injection from file if --injection is set."""
        f = open(injectionfile, 'r')
        try:
            data = f.read()
        finally:
            f.close()
        return data
