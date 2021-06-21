import numpy as np
import pandas as pd
from caustique import Model, Sample

def test_sample_pdf():
    np.random.seed(1234)
    n = 10000
    x_data = np.random.binomial(1, 0.5, size=n)
    y_data = np.random.binomial(1, np.exp(4.0 * x_data - 2.0) / (1.0 + np.exp(4.0 * x_data - 2.0)))
    z_data = np.random.binomial(1, np.exp(2.0 * (x_data + y_data) - 2.0) / (1.0 + np.exp(2.0 * (x_data + y_data) - 2.0)))
    data = {'X' : x_data, 'Y' : y_data, 'Z' : z_data}
    df = pd.DataFrame(data)
    x = Sample('X', df)
    y = Sample('Y', df)
    z = Sample('Z', df)
    x >> y
    y >> z
    model = Model(x, y, z)
    pdf = model.pdf(x, y, z)
    import pdb; pdb.set_trace()
