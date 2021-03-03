from estimator.score_search import *
import pandas as pd

data = pd.DataFrame(data={'A': [1, 1, 2],
                          'B': [1, 1, 1],
                          'C': [0, 1, 0]})
print(data)
sf = ScoreFunction(data)
print(sf.collect_state_names(variable='A'))
print(sf.state_counts('A',parents=['B','C']))

bic = BicScore(data)
LS = bic.local_score('A','B')
print(LS)