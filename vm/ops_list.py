import sys


class OpsFuncs:
    def __init__(self, bin_generator):

        self.stack = []

        self.OpsMapping = {
            "0": self.OP_EOP,
            "1": self.OP_SET,
            "02": self.OP_PUSH,
            "03": self.OP_POP,
            "05": self.OP_ADD,
            "06": self.OP_SUB,
            "19": self.OP_PRINT,
            "21": self.OP_NOOP,
        }

        self.bin_generator = bin_generator

    def OP_EOP(self):
        return

    def OP_SET(self):
        print("End of Instruction")

    def OP_PUSH(self):
        to_push = int(self.bin_generator.__next__(), 16)
        self.stack.append(to_push)

    def OP_POP(self):
        self.stack.pop()

    def OP_ADD(self):
        total = self.stack[-1] + self.stack[-2]
        self.stack = self.stack[:-2]
        self.stack.append(total)

    def OP_SUB(self):
        total = self.stack[-1] - self.stack[-2]
        self.stack = self.stack[:-2]
        self.stack.append(total)

    def OP_PRINT(self):
        self.bin_generator.__next__()
        sys.stdout.write(chr(int(self.bin_generator.__next__())))

    def OP_NOOP(self):
        return
