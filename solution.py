import pandas as pd
import numpy as np


chat_id = 468819439 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = anderson_ksamp([x, y]).pvalue
    return pval < 0.04 # Ваш ответ, True или False
