

class Node:
    def __init__(self, input_required=False):
        self.ins = []
        self.outs = []
        self.input_required = input_required
        
    def __str__(self):
        return self.name if self.name is not None else self.__class__.__name__    
        
    def __repr__(self):
        return self.__str__()

    def compute(self, inputs):
        pass

    @property
    def in_degree(self):
        return len(self.ins)

    @property
    def out_degree(self):
        return len(self.outs)

    @staticmethod
    def add_edge(src, dst):
        if dst not in src.outs:
            src.outs.append(dst)

        if src not in dst.ins:
            dst.ins.append(src)

    @staticmethod
    def nary_function(klass, *args):   
        c = klass()
        for n in args:
            Node.add_edge(n, c)
        return c