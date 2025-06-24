# montecarlo_pi.py

import random
import math

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = math.sqrt(x ** 2 + y ** 2)

        if distance <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

def main():
    print("Monte Carlo法による円周率の推定")
    try:
        n = int(input("試行回数（例：10000）を入力してください："))
        result = estimate_pi(n)
        print(f"推定されたπの値（{n}回の試行）： {result}")
    except ValueError:
        print("整数を入力してください。")

if __name__ == "__main__":
    main()
