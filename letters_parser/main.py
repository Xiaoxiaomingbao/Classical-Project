import tkinter as tk


def update_output(event=None):
    # 获取用户输入的内容
    text = input_text.get("1.0", tk.END).strip()
    # 将用户输入的内容显示在输出文本框中
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, text)
    cursor_index = input_text.index(tk.INSERT)
    print(cursor_index)


# 创建主窗口
root = tk.Tk()
root.title("文本框示例")

# 创建输入文本框和标签
input_label = tk.Label(root, text="输入内容:")
input_label.pack()
input_text = tk.Text(root, width=100, height=20)
input_text.pack()
# 绑定<KeyRelease>事件，当用户释放键盘键时触发更新操作
input_text.bind("<KeyRelease>", update_output)
# 绑定<ButtonRelease-1>事件，当用户单击鼠标左键时触发更新操作
input_text.bind("<ButtonRelease-1>", update_output)

# 创建输出文本框和标签
output_label = tk.Label(root, text="输出内容:")
output_label.pack()
output_text = tk.Text(root, width=100, height=20)
output_text.pack()

# 初始化输出文本框内容
update_output()

# 运行主循环
root.mainloop()
