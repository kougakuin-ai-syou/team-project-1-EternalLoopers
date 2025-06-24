# score.py
# すべてのモジュールを読み込み、統合して結果出力

from score_preprocessing import get_dataframe, get_numpy_array
from score_df import basic_stats, country_score
from score_stats import calc_std, calc_var, calc_corrcoef
from score_plot import bar_plot, line_plot

def main():
    df = get_dataframe()
    arr = get_numpy_array()

    print("=== DataFrame 統計情報 ===")
    stats = basic_stats(df)
    print("平均:\n", stats["mean"])
    print("最大:\n", stats["max"])
    print("最小:\n", stats["min"])
    print()

    print("=== NumPy 統計値 ===")
    print("標準偏差:", calc_std(arr))
    print("分散:", calc_var(arr))
    print("相関係数:\n", calc_corrcoef(arr))
    print()

    # グラフ描画
    bar_plot(df)
    line_plot(df)

if __name__ == "__main__":
    main()


