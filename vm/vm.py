from vm.ops_list import OpsFuncs


def load(bin_file):
    def _bytes_from_file(file):
        with open(file, "rb") as f:
            while True:
                for b in f.read():
                    yield str(b)

    return _bytes_from_file(bin_file)


def exec_bins(bin_gen: iter):

    Ops = OpsFuncs(bin_gen)

    for op in bin_gen:
        func = Ops.OpsMapping.get(op)
        ret = func() if func is not None else op


def run_program(bin_file):
    bin_gen = load(bin_file)
    exec_bins(bin_gen)
