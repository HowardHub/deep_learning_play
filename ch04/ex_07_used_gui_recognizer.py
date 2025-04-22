import tkinter as tk
from PIL import Image, ImageGrab, ImageOps, ImageTk
import numpy as np
import os
import sys
from scipy.ndimage import center_of_mass, shift, binary_dilation, gaussian_filter

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

# ———————— 2. 改进的预处理函数 ————————
def preprocess_and_save(pil_img, save_path="processed_28x28.png"):
    # 1. 灰度 + 反转
    img = pil_img.convert('L')
    img = ImageOps.invert(img)
    
    # 2. 提取有效区域（裁剪空白区域）
    # 转换为numpy数组处理
    img_array = np.array(img)
    # 找到非零像素的边界
    rows = np.any(img_array > 20, axis=1)
    cols = np.any(img_array > 20, axis=0)
    if np.any(rows) and np.any(cols):  # 确保有内容
        ymin, ymax = np.where(rows)[0][[0, -1]]
        xmin, xmax = np.where(cols)[0][[0, -1]]
        # 添加一点边距
        ymin = max(0, ymin - 2)
        ymax = min(img_array.shape[0] - 1, ymax + 2)
        xmin = max(0, xmin - 2)
        xmax = min(img_array.shape[1] - 1, xmax + 2)
        # 裁剪到只包含数字的区域
        img = img.crop((xmin, ymin, xmax, ymax))
    
    # 3. 保留宽高比，但添加白边使其成为正方形
    width, height = img.size
    if width > height:
        # 宽大于高，需要在上下添加白边
        new_img = Image.new('L', (width, width), 0)
        paste_y = (width - height) // 2
        new_img.paste(img, (0, paste_y))
        img = new_img
    elif height > width:
        # 高大于宽，需要在左右添加白边
        new_img = Image.new('L', (height, height), 0)
        paste_x = (height - width) // 2
        new_img.paste(img, (paste_x, 0))
        img = new_img
    
    # 4. 缩放到20x20，然后在28x28的画布上居中放置，保留边距
    img = img.resize((20, 20), resample=Image.BICUBIC)
    padded_img = Image.new('L', (28, 28), 0)
    padded_img.paste(img, (4, 4))  # 留出4像素的边距
    
    # 5. 二值化，但使用自适应阈值
    arr = np.array(padded_img, dtype=np.float32) / 255.0
    # 计算合适的阈值
    if arr[arr > 0].size > 0:  # 确保有非零像素
        threshold = max(0.1, arr[arr > 0].mean() * 0.5)  # 至少10%的阈值
    else:
        threshold = 0.1
    arr = (arr > threshold).astype(np.float32)
    
    # 6. 确保数字笔画有足够粗细（避免细线消失）
    # 轻微膨胀操作使线条更粗
    arr = binary_dilation(arr, iterations=1).astype(np.float32)
    
    # 7. 平滑处理
    arr = gaussian_filter(arr, sigma=0.5)
    
    # 8. 保存处理后的图像
    out_img = Image.fromarray((arr * 255).astype(np.uint8))
    out_img.save(save_path)
    
    # 9. 返回网络输入格式
    return arr.reshape(1, 784)

# ———————— 3. 改进的GUI ————————
class ImprovedApp:
    def __init__(self, root):
        self.root = root
        root.title("手写数字识别")
        
        # 框架布局
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10)
        
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, padx=10)
        
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, padx=10)
        
        # 主画布 - 增大尺寸并添加边框
        self.canvas = tk.Canvas(left_frame, width=280, height=280, bg='white', 
                              highlightthickness=1, highlightbackground="gray")
        self.canvas.pack()
        
        # 绑定鼠标事件
        self.canvas.bind("<Button-1>", self.reset_last_pos)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.last_x, self.last_y = None, None
        
        # 预览框 - 显示28x28处理后的图像
        preview_label = tk.Label(right_frame, text="预处理后的图像:")
        preview_label.pack(pady=(0, 5))
        
        self.preview_canvas = tk.Canvas(right_frame, width=140, height=140, bg='black',
                                      highlightthickness=1, highlightbackground="gray")
        self.preview_canvas.pack()
        
        # 按钮框架
        btn_frame = tk.Frame(left_frame)
        btn_frame.pack(pady=10)
        
        # 粗细调整
        thickness_frame = tk.Frame(btn_frame)
        thickness_frame.pack(side=tk.LEFT, padx=5)
        tk.Label(thickness_frame, text="笔粗:").pack(side=tk.LEFT)
        self.thickness = tk.IntVar(value=16)  # 默认粗细
        tk.Scale(thickness_frame, from_=6, to=24, orient=tk.HORIZONTAL, 
               variable=self.thickness, length=80).pack(side=tk.LEFT)
        
        # 操作按钮
        tk.Button(btn_frame, text="识别", command=self.on_recognize).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="清空", command=self.on_clear).pack(side=tk.LEFT, padx=5)
        
        # 结果显示
        self.result_var = tk.StringVar(value="请在左侧画板写数字")
        result_frame = tk.Frame(right_frame, height=100)
        result_frame.pack(pady=10, fill=tk.X)
        
        self.prob_labels = []
        # 显示所有数字的概率
        tk.Label(result_frame, text="识别概率:").pack(anchor=tk.W)
        for i in range(10):
            prob_frame = tk.Frame(result_frame)
            prob_frame.pack(fill=tk.X, pady=2)
            digit_label = tk.Label(prob_frame, text=f"数字 {i}:", width=8, anchor=tk.W)
            digit_label.pack(side=tk.LEFT)
            prob_label = tk.Label(prob_frame, text="0%", width=10, anchor=tk.W)
            prob_label.pack(side=tk.LEFT)
            self.prob_labels.append((digit_label, prob_label))
        
        # 最终结果
        self.result_label = tk.Label(right_frame, text="识别结果: ?", 
                                    font=('Arial', 24, 'bold'))
        self.result_label.pack(pady=10)
        
        # 帮助提示
        tk.Label(left_frame, text="提示: 尽量写大一些，笔画清晰", 
               font=('Arial', 9), fg='gray').pack(pady=(5, 0))
        
        # 添加网格线
        self.draw_grid()
    
    def draw_grid(self, line_distance=40):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        if canvas_width == 1:  # 窗口尚未完全加载
            self.root.after(100, self.draw_grid)
            return
            
        # 垂直线
        for x in range(line_distance, canvas_width, line_distance):
            self.canvas.create_line(x, 0, x, canvas_height, fill="#f0f0f0")
        # 水平线
        for y in range(line_distance, canvas_height, line_distance):
            self.canvas.create_line(0, y, canvas_width, y, fill="#f0f0f0")
    
    def reset_last_pos(self, event):
        self.last_x, self.last_y = None, None
    
    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x is not None:
            # 画线，使用用户选择的粗细
            self.canvas.create_line(self.last_x, self.last_y, x, y, 
                                  width=self.thickness.get(), 
                                  capstyle=tk.ROUND, 
                                  smooth=True)
        self.last_x, self.last_y = x, y
    
    def on_release(self, event):
        # 松开鼠标时更新预览
        self.update_preview()
    
    def update_preview(self):
        # 抓取当前画布并生成预览
        scale = self.root.tk.call('tk', 'scaling')
        x = int((self.root.winfo_rootx() + self.canvas.winfo_x()) * scale)
        y = int((self.root.winfo_rooty() + self.canvas.winfo_y()) * scale)
        x1 = int((x + self.canvas.winfo_width()) * scale)
        y1 = int((y + self.canvas.winfo_height()) * scale)
        
        try:
            img = ImageGrab.grab(bbox=(x, y, x1, y1))
            # 预处理但不进行识别
            preprocess_and_save(img, save_path="preview.png")
            # 加载并显示预览
            preview = Image.open("preview.png")
            # 放大显示
            preview = preview.resize((140, 140), Image.NEAREST)
            self.preview_img = ImageTk.PhotoImage(preview)
            self.preview_canvas.create_image(70, 70, image=self.preview_img)
        except Exception as e:
            print(f"预览更新失败: {e}")
    
    def on_clear(self):
        self.canvas.delete("all")
        # 重新绘制网格
        self.draw_grid()
        # 清空预览
        self.preview_canvas.delete("all")
        # 重置结果
        self.result_label.config(text="识别结果: ?")
        # 重置概率
        for _, prob_label in self.prob_labels:
            prob_label.config(text="0%")
        self.last_x, self.last_y = None, None
    
    def on_recognize(self):
        # 更新预览
        self.update_preview()
        
        scale = self.root.tk.call('tk', 'scaling')
        x = int((self.root.winfo_rootx() + self.canvas.winfo_x()) * scale)
        y = int((self.root.winfo_rooty() + self.canvas.winfo_y()) * scale)
        x1 = int((x + self.canvas.winfo_width()) * scale)
        y1 = int((y + self.canvas.winfo_height()) * scale)
        
        img = ImageGrab.grab(bbox=(x, y, x1, y1))
        # 预处理
        x_input = preprocess_and_save(img, save_path="last_processed.png")
        # 获取完整预测结果
        y_pred = network.predict(x_input)
        digit = np.argmax(y_pred, axis=1)[0]
        # 显示最终结果
        self.result_label.config(text=f"识别结果: {digit}")
        
        # 计算softmax以获得更有意义的概率
        exp_scores = np.exp(y_pred)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        
        # 更新各数字的概率
        for i in range(10):
            prob = float(probs[0, i]) * 100
            _, prob_label = self.prob_labels[i]
            # 高亮显示最高概率
            if i == digit:
                prob_label.config(text=f"{prob:.1f}%", fg="red", font=('Arial', 9, 'bold'))
            else:
                prob_label.config(text=f"{prob:.1f}%", fg="black", font=('Arial', 9))

if __name__ == '__main__':
    # 运行
    root = tk.Tk()
    app = ImprovedApp(root)
    root.mainloop()




