# score_preprocessing.py

"""
課題B：成績データの可視化と統計処理
OECD PISA 2022 の数学・読解・科学リテラシー平均スコアを使用したサンプルデータ
"""

# サンプルデータ：国ごとの平均スコア
pisa_data = [
    {"country": "Japan",       "math": 536, "reading": 516, "science": 547},
    {"country": "USA",         "math": 465, "reading": 504, "science": 499},
    {"country": "Germany",     "math": 475, "reading": 480, "science": 492},
    {"country": "Singapore",     "math": 575, "reading": 543, "science": 561},
    {"country": "Korea",     "math": 527, "reading": 515, "science": 528},
    {"country": "UK",     "math": 489, "reading": 494, "science": 500},
    {"country": "France",     "math": 474, "reading": 474, "science": 487},
    {"country": "Israel",     "math": 458, "reading": 474, "science": 465},
    {"country": "Cambodia",     "math": 336, "reading": 329, "science": 347},
    {"country": "Indonesia",     "math": 366, "reading": 359, "science": 383},
    {"country": "Brazil",     "math": 379, "reading": 410, "science": 403},
    {"country": "Italy",     "math": 471, "reading": 482, "science": 477},
    {"country": "Mongolia",     "math": 425, "reading": 378, "science": 412},
    {"country": "Malaysia",     "math": 409, "reading": 388, "science": 416},
    {"country": "Viet Nam",     "math": 469, "reading": 462, "science": 472},
    {"country": "Chinese Taipei",     "math": 547, "reading": 515, "science": 537},
    {"country": "Thailand",     "math": 394, "reading": 379, "science": 409},
    {"country": "Sweden",     "math": 482, "reading": 487, "science": 494},
]

def get_dataframe():
    """PISAデータをpandas DataFrame形式で返す"""
    import pandas as pd
    df = pd.DataFrame(pisa_data)
    return df

def get_numpy_array():
    """PISAデータをNumPy配列形式で返す（数値データのみ）"""
    import numpy as np
    arr = np.array([[d["math"], d["reading"], d["science"]] for d in pisa_data])
    return arr

if __name__ == "__main__":
    df = get_dataframe()
    print("=== PISA 2022 OECD 平均スコア（サンプル）===")
    print(df)
    print()
    arr = get_numpy_array()
    print("NumPy 配列 →", arr.shape)
    print(arr)

