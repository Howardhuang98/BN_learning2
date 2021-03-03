import base
import numpy as np
import pandas as pd


class ScoreFunction():
    """
    评分函数类
    评分函数类需要data，以及一些data的计算能力，比如state count，对data的检查能力
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.variables = list(data.columns.values)
        self.state_names = dict()
        for var in self.variables:
            self.state_names[var] = self.collect_state_names(var)

    def collect_state_names(self, variable):
        """收集数据中某个变量variable的状态名
        :param variable:
        """
        states = sorted(list(self.data.loc[:, variable].unique()))
        return states

    def state_counts(self, variable, parents=[]):
        """
        计算该变量的状态数，得到一个交叉表。例如
        variable = 'C', parents=['A', 'B']
        A  a1      a2
        B  b1  b2  b1  b2
        C
        c1  1   1   0   0
        c2  0   0   1   0
        :param variable:
        :param parents:
        :return:
        """

        if not parents:
            state_count_data = self.data.loc[:, variable].value_counts()
            state_counts = (
                state_count_data.reindex(self.state_names[variable])
                    .fillna(0)
                    .to_frame()
            )
        else:
            parents_states = [self.state_names[parent] for parent in parents]
            # count how often each state of 'variable' occured, conditional on parents' states
            state_count_data = (
                self.data.groupby([variable] + parents).size().unstack(parents)
            )
            if not isinstance(state_count_data.columns, pd.MultiIndex):
                state_count_data.columns = pd.MultiIndex.from_arrays(
                    [state_count_data.columns]
                )

            # reindex rows & columns to sort them and to add missing ones
            # missing row    = some state of 'variable' did not occur in data
            # missing column = some state configuration of current 'variable's parents
            #                  did not occur in data
            row_index = self.state_names[variable]
            column_index = pd.MultiIndex.from_product(parents_states, names=parents)
            state_counts = state_count_data.reindex(
                index=row_index, columns=column_index
            ).fillna(0)
        return state_counts
