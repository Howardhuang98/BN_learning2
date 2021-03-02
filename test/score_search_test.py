from estimator.score_search import *
import pandas as pd

data = pd.DataFrame(data={'A': ['a1', 'a1', 'a2'],
                          'B': ['b1', 'b2', 'b1'],
                          'C': ['c1', 'c1', 'c2']})
print(data)
sf = Score_function(data)
print(sf.collect_state_names(variable='A'))
print(sf.state_counts('A',parents=['B']))
