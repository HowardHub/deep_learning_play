# gui_recognizer.py

import tkinter as tk
from PIL import Image, ImageGrab, ImageOps
import numpy as np
import os
import sys

from scipy.ndimage import center_of_mass, shift



# 如果 ex_06_two_layer_net.py 在父目录，可以取消下面两行注释
# sys.path.append(os.pardir)
from ex_06_two_layer_net import TwoLayerNet

# ———————— 1. 加载模型 ————————
data = np.load('two_layer_net_params.npz')
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
network.params['W1'] = data['W1']
network.params['b1'] = data['b1']
network.params['W2'] = data['W2']
network.params['b2'] = data['b2']

# ———————— 2. 预处理函数 ————————
def preprocess_and_save(pil_img, save_path="processed_28x28.png"):
    # 1. 灰度 + 反转
    img = pil_img.convert('L')
    img = ImageOps.invert(img)

    # 2. 直接把整个画布等比缩到 28×28
    # 缩放时用最近邻
    img28 = img.resize((28,28), resample=Image.Resampling.NEAREST)
    arr = np.array(img28, dtype=np.float32) / 255.0
    # 二值化保留边缘
    arr = (arr > 0.2).astype(np.float32)

    # 3. 计算重心并平移到中心
    cy, cx = center_of_mass(arr)
    shift_y = 14 - cy
    shift_x = 14 - cx
    arr = shift(arr, shift=(shift_y, shift_x), mode='constant')

    # 4. 转回 PIL 并保存
    out_img = Image.fromarray((arr * 255).astype(np.uint8))
    out_img.save(save_path)

    # 5. 返回网络输入格式
    return arr.reshape(1, 784)

# ———————— 3. 预测函数 ————————
def predict_from_canvas(canvas, root):
    # 计算画布在屏幕上的坐标（记得加上 Retina 缩放）
    scale = root.tk.call('tk', 'scaling')
    x = int((root.winfo_rootx() + canvas.winfo_x())  * scale)
    y = int((root.winfo_rooty() + canvas.winfo_y())  * scale)
    x1 = int((x + canvas.winfo_width())  * scale)
    y1 = int((y + canvas.winfo_height()) * scale)

    # 抓图
    img = ImageGrab.grab(bbox=(x, y, x1, y1))
    # 预处理并保存到本地
    x_input = preprocess_and_save(img, save_path="last_processed.png")
    y = network.predict(x_input)
    return np.argmax(y, axis=1)[0]

# ———————— 4. 搭建 GUI ————————
class App:
    def __init__(self, root):
        self.root = root
        root.title("手写数字识别")

        # 画布
        self.canvas = tk.Canvas(root, width=200, height=200, bg='white')
        self.canvas.pack(padx=10, pady=10)

        # 绑定鼠标事件
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.last_x, self.last_y = None, None

        # 按钮区
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="识别", command=self.on_recognize).pack(side='left', padx=5)
        tk.Button(btn_frame, text="清空", command=self.on_clear).pack(side='left', padx=5)

        # 结果显示
        self.label = tk.Label(root, text="请在上方画板写数字", font=('Arial', 14))
        self.label.pack(pady=5)

    def on_button_press(self, event):
        # 每次落笔先重置，防止与上一笔连线
        self.last_x, self.last_y = None, None

    def on_button_release(self, event):
        # 提笔时重置，确保新一笔独立
        self.last_x, self.last_y = None, None

    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(
                self.last_x, self.last_y, x, y,
                width=8, capstyle=tk.ROUND, smooth=True
            )
        self.last_x, self.last_y = x, y

    def on_clear(self):
        self.canvas.delete("all")
        self.label.config(text="请在上方画板写数字")
        self.last_x, self.last_y = None, None

    def on_recognize(self):
        digit = predict_from_canvas(self.canvas, self.root)
        self.label.config(text=f"识别结果： {digit}")

if __name__ == '__main__':
    # 运行
    root = tk.Tk()
    App(root)
    root.mainloop()


