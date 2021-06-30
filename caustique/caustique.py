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

    def __eq__(self, value):
        return Sample(self.name, self.df[self.df[self.name] == value])
    
    def pdf(self, value):
        return len(self.df[self.df[self.name] == value]) / float(len(self.df))

def apply_conditions(df, conditions):
    """Apply conditions to a DataFrame.
    
    Parameters
    ----------
    df: DataFrame
        A DataFrame with data subject to analysis.
    conditions: dict
        A dictionary with variable names as keys and bool functions as values.
    
    Returns
    -------
    DataFrame
        A DataFrame with conditions applied.
    """
    pass

def ecdf(df, variables, dag, alpha):
    """Will calculate an empirical joint CDF with confidence regions and under causal assumptions.

    Parameters
    ----------
    df: DataFrame
        A pandas DataFrame with empirical data for which this CDF will be computed.
    variables: list
        A list of strings where each string is a column name in df. Represents variables
        for which this CDF needs to be computed.
    dag: dict
        A dictionary where keys are variable names and values are list of variable names
        representing parents of that variable in the causality graph.
    alpha: float
        A value for which to compute the confidence region (e.g. 0.01)
    """
    def _cdf(**kwargs):
        result = 1.0
        for variable in variables:
            df_ = df
            for parent in dag[variable]:
                df_ = df_[df_[parent] <= kwargs[parent]]
            result *= len(df_[df_[variable] <= kwargs[variable]]) / float(len(df_))
        return result
    return _cdf
