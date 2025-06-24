# score_plot.py

import matplotlib.pyplot as plt

def bar_plot(df):
    """国別に科目別スコアを棒グラフ表示"""
    df.plot(x="country", y=["math", "reading", "science"], kind="bar", figsize=(12,6))
    plt.title("OECD PISA 2022 Average score")
    plt.ylabel("Score")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def line_plot(df):
    """科目別のスコア推移（折れ線グラフ）"""
    subjects = ["math", "reading", "science"]
    for subj in subjects:
        plt.plot(df["country"], df[subj], label=subj)
    plt.title("OECD PISA 2022")
    plt.ylabel("Score")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

