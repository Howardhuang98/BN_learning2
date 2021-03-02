import base
import numpy as np
import pandas as pd


class Score_function():
    """
    评分函数类
    评分函数类需要data，以及一些data的计算能力，比如state count，对data的检查能力
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.variables = list(data.columns.values)

    def collect_state_names(self,variable):
        """收集数据中某个变量variable的状态名
        :param variable:
        """
        states = sorted(list(self.data.loc[:,variable].unique()))
        return states