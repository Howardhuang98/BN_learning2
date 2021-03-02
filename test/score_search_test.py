from estimator.score_search import *
import pandas as pd

data = pd.DataFrame(data=[1,2,3,4])
print(data)
sf = Score_function(data)
print(sf.collect_state_names(variable=0))