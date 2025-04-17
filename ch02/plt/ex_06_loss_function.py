import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 使用Hiragino Sans GB字体（macOS系统字体）
font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc"
font_prop = font_manager.FontProperties(fname=font_path)

# 创建预测值范围（为了避免log(0)的问题，从一个很小的正数开始）
y_pred = np.linspace(0.001, 0.999, 1000)

# 计算真实值y=1时的均方误差
mse = (1 - y_pred) ** 2

# 计算真实值y=1时的交叉熵误差 (-log(y_pred))
cross_entropy = -np.log(y_pred)

# 创建一个新的图形
plt.figure(figsize=(12, 8))

# 绘制两条曲线
plt.plot(y_pred, mse, 'b-', linewidth=2.5, label='均方误差 (MSE)')
plt.plot(y_pred, cross_entropy, 'r-', linewidth=2.5, label='交叉熵误差 (CE)')

# 添加一条垂直线表示y=1
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=1, color='gray', linestyle='--', alpha=0.7)

# 添加标签和标题（使用指定字体）
plt.xlabel('预测值 (ŷ)', fontsize=14, fontproperties=font_prop)
plt.ylabel('误差', fontsize=14, fontproperties=font_prop)
plt.title('均方误差 vs 交叉熵误差 (当实际标签 y=1)', fontsize=16, fontproperties=font_prop)

# 设置图例（使用指定字体）
legend = plt.legend(fontsize=12)
for text in legend.get_texts():
    text.set_fontproperties(font_prop)

# 设置坐标轴范围
plt.xlim(0, 1.05)
plt.ylim(0, 5)

# 添加网格
plt.grid(True, alpha=0.3)

# 添加说明性文本（使用指定字体）
plt.annotate('交叉熵在预测值接近0时\n惩罚更为严重', xy=(0.1, 3), xytext=(0.2, 4),
            arrowprops=dict(facecolor='red', shrink=0.05, alpha=0.7), 
            fontsize=12, fontproperties=font_prop)
            
plt.annotate('均方误差呈抛物线形状', xy=(0.5, 0.25), xytext=(0.3, 0.6),
            arrowprops=dict(facecolor='blue', shrink=0.05, alpha=0.7), 
            fontsize=12, fontproperties=font_prop)

# 紧凑布局
plt.tight_layout()

# 保存图像并显示
plt.savefig('loss_functions_hiragino.png', dpi=300)
plt.show()