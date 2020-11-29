import os
from shell import *
from timem import *

def open_file(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content

class MAIN(Shell):
    def run(self):
        print("\nAvailable options: alignment, match, mismatch, gap, resources, exit.\nRefer ReadMe for more information.")
        super().run()

    def alignment(self, args):
        if len(args) != 3 and len(args) != 4:
            raise Exception("Incorrect Number of Arguments.")
        v_text = open_file(args[1]) if os.path.isfile(args[1]) else args[1]
        h_text = open_file(args[2]) if os.path.isfile(args[2]) else args[2]
        alignment = self.find_option(args[0] + " linear" if len(args) == 4 else args[0])
        if args[0] == "kband":
            kvalue = int(input("Enter a value for k: "))
            self.last_result = alignment(v_text, h_text, self._match, self._mismatch, self._gap, kvalue)
        else:
            self.last_result = alignment(v_text, h_text, self._match, self._mismatch, self._gap)
        self.optimal(args)
        self.tables("arrows")
   
    def tables(self, args):
        print("\n Table obtained")
        if self.last_result is not None:
            self.last_result.show_arrows = args.__contains__("arrows")
            print(self.last_result)
        else:
            print("Without calculations\n")

    def optimal(self, args):
        print("\nOptimal value: ")
        if self.last_result is not None:
            print("Value: " + self.last_result.calc_score().astype(str) + "\n")
        else:
            print("Value: 0 \n")
        print("Alignment obtained: ")
        if self.last_result is not None:
            string_1, string_2 = self.last_result.reconstruction()
            print(string_1)
            print(string_2 + "\n")
        else:
            print("Alignment: Without calculation \n")

    def lists(self, args):
        print("\nAlgorithm Implemented: ")
        algorithms = list(self.algoritms.keys())
        for i in range(len(algorithms)):
            print(str(i) + ". " + str(algorithms[i]))
        print("")
  
    def match(self, args):
        self.config(["match"] + args)

    def mismatch(self, args):
        self.config(["mismatch"] + args)

    def gap(self, args):
        self.config(["gap"] + args)
    
    def config(self, args):
        if len(args) == 0:
            self.val(args)
        else:
            if len(args) == 2:
                exec("self._" + args[0] + " = " + args[1])
            print("\n Actual value")
            eval("print('" + args[0] + ": ' + " + "str(self._" + args[0] + ") + '\\n' )")

    def exit(self, args):
        print("Exiting the program. Thank you!\n")
        sys.exit(0)

    def resources(self, args):
        print("\nResources utilized")
        print("Time: %.10f seconds" % Timem.last_time)
        print("Memory: %s bytes\n" % str(Timem.last_memory_usage))

if __name__ == "__main__":
    main = MAIN()
    main.run()


