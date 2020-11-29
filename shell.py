from algos.kband_align import *
from algos.local_align import *
from algos.global_align import *
from algos.semiglobal_align import *
from algos.semiglobal_linear import *
from algos.global_linear import *
from algos.local_linear import *

class Shell(object):


    def __init__(self):

        self._gap = -2
        self._match = 1
        self._mismatch = -1
        self.last_result = None
        self.algoritms = self.get_algorithms()


    def run(self):
        self.command_line()


    def command_line(self):

        command = input("Enter a command: ")

        try:
            self.exec_command(command)
        except Exception as e:
            self.manage_exception(e, command)

        self.command_line()


    def get_algorithms(self):

        return {
            "global": GlobalAlign,
            "semiglobal": SemiglobalAlign,
            "local": LocalAlign,
            "globallineal": GlobalLinear,
            "semigloballineal": SemiglobalLinear,
            "locallineal": LocalLinear,
            "kband": KBandAlign
        }


    def manage_exception(self, exception, command):

        print("\nError: " + str(exception))
        name = command.split(" ")[0]
        option = self.find_option(name)

    def exec_option(self, option_name, option_args):

        option = self.find_option(option_name)
        if type(option) == str or type(option) == int:
            return str(option)
        if option is not None:
            return str(option(option_args))
        else:
            raise Exception("Option not available\n")


    def exec_help(self, option_name):

        option = self.find_option(option_name)
        if option is not None:
            return option.__doc__
        raise Exception("Help not available")


    def find_option(self, option_name):

        options = dir(self)
        if options.__contains__(option_name):
            return getattr(self, option_name)
        elif self.algoritms.__contains__(option_name):
            return self.algoritms[option_name]
        return None


    def exec_command(self, command):

        name = command.split(" ")[0]
        args = command.split(" ")[1::]
        return self.exec_option(name, args)

