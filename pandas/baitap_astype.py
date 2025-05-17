import pandas as pd
import numpy as np

data = {'IntCol': [1, 2, 3],
        'FloatCol': [1.1, 2.2, 3.3],
        'StringCol': ['a', 'b', 'c'],
        'BoolCol': [True, False, True],
        'DateStrCol': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'NumericStrCol': ['1', '2.5', '3.0'],}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
print("\nDataFrame dtypes:\n", df.dtypes)