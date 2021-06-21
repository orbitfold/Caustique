import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self, *args):
        self.variables = dict([(var.name, var) for var in args])

    def pdf(self, **kwargs):
        mult = 1.0
        for variable in self.variables.keys():
            mult *= self.variables[variable].pdf(kwargs[variable], conditions)
            for parent in self.variables[variable].parents:
                mult *= self.variables[parent.name].pdf(kwargs[parent.name], conditions)
        return mult

class Variable:
    def __init__(self, name):
        self.children = []
        self.parents = []
        self.name = name
        
    def __rshift__(self, right):
        self.children.append(right)
        right.parents.append(self)
        return right

    def pdf(self, x):
        raise NotImplementedError

class Sample(Variable):
    def __init__(self, name, df):
        """Create a Variable representing a sample.

        Parameters
        ----------
        df: DataFrame
            A full data frame to be examined.
        """
        self.df = df
        super(Sample, self).__init__(name)

    def __eq__(self, other):
        return self.df[self.name] == other
    
    def pdf(self, x):
        pass

