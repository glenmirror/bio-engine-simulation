import random
import math
import matplotlib.pyplot as plt

# --- 初期状態 ---
O = 1.0        # 酸素レベル (0〜1)
R = 0.5        # 呼吸能力
P_max = 1.0    # 最大出力

dt = 0.1

# 記録用
oxygen_history = []
performance_history = []
error_count = 0

# 遅延バッファ（入力を遅らせる）
input_buffer = []

# 仮の入力（プレイヤーが常に同じ方向に攻撃）
intended_direction = 0.0

for t in range(200):

    # --- ダメージイベント（首ダメージ） ---
    if t == 60:
        R *= 0.3  # 呼吸低下

    # --- 生体モデル ---
    P = P_max * O
    dO = R - 0.4 * P
    O += dO * dt

    # 範囲制限
    O = max(0, min(1, O))

    # --- 神経能力（酸素依存） ---
    cognitive = O  # シンプル化

    # --- ノイズ（方向ズレ） ---
    sigma = (1 - cognitive) * 0.5
    noisy_direction = intended_direction + random.gauss(0, sigma)

    # --- 遅延 ---
    delay_steps = int((1 - cognitive) * 10)
    input_buffer.append(noisy_direction)

    if len(input_buffer) > delay_steps:
        actual_direction = input_buffer.pop(0)
    else:
        actual_direction = intended_direction  # バッファ不足時

    # --- 暴発 ---
    error_prob = (1 - cognitive) * 0.2
    if random.random() < error_prob:
        actual_direction = random.uniform(-math.pi, math.pi)
        error_count += 1

    # --- 記録 ---
    oxygen_history.append(O)
    performance_history.append(P)

# --- グラフ ---
plt.figure()
plt.plot(oxygen_history, label="Oxygen")
plt.plot(performance_history, label="Performance")
plt.legend()
plt.title("Bio Simulation: Oxygen & Performance")
plt.xlabel("Time")
plt.ylabel("Level")
plt.show()

print("Total unintended actions:", error_count)