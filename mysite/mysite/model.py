import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
import sklearn

class Model:
    def __init__(self, request) -> None:
        self.boston = pd.read_csv('static/boston.csv')
        self.variables = request["variables"]
        self.values = request["values"]
        self.result = []
    
    def predict(self):
        # 데이터
        x_data = self.boston.loc[:, self.variables]

        y_data = self.boston.iloc[:, -2]
        #학습 셋 분리
        train_X, test_X, train_y, test_y = sklearn.model_selection.train_test_split(x_data, y_data, test_size = 0.33)
        #모델 생성
        multi_linear = LinearRegression(fit_intercept = True)
        # 모델 학습
        multi_linear.fit(train_X,train_y)
        # 예측결과
        np_array_value = np.array(self.values)
        x_to_pred = pd.DataFrame(np_array_value)
        y_pred = multi_linear.predict(x_to_pred)
        self.result["y_hat"] = y_pred


    def get_statics(self):
        x_data = self.boston.loc[:, self.variables]
        statics = x_data.describe().to_dict('dict')
        self.result["statics"] = statics

        
