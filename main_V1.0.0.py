import tkinter as tk
from tkinter import ttk
import subprocess
import easygui
import os
import json
import webbrowser

# 配置文件路径
CONFIG_FILE = "config.json"

# 默认配置
default_config = {
    "mirror_source": "pypi.org",
}

# 读取配置文件
def load_config():
    # 如果配置文件存在，则读取配置文件
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        # 如果配置文件不存在，则返回默认配置
        return default_config.copy()

# 保存配置文件
def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)

# 获取镜像源列表
def get_mirror_sources():
    return {
        "pypi.org": "https://pypi.org/simple",
        "清华镜像": "https://pypi.tuna.tsinghua.edu.cn/simple",
        "阿里镜像": "https://mirrors.aliyun.com/pypi/simple",
        "中科大镜像": "https://pypi.mirrors.ustc.edu.cn/simple",
        "豆瓣镜像": "https://pypi.doubanio.com/simple",
    }

# 打开文件位置
def open_package_location(package_name):
    try:
        # 使用pip show命令获取包的安装位置
        package_location = subprocess.check_output(
            ["python", "-m", "pip", "show", package_name], universal_newlines=True
        )
        for line in package_location.splitlines():
            if line.startswith("Location:"):
                location = line.split(":", 1)[1].strip()
                # 打开文件位置
                webbrowser.open(location)
                return
        easygui.msgbox(f"未找到 {package_name} 的安装位置", title="错误")
    except subprocess.CalledProcessError as e:
        easygui.msgbox(f"无法获取安装位置: {str(e)}", title="错误")

# 查看已安装包的回调函数
def view_installed_packages():
    try:
        # 使用pip list命令获取已安装的包列表
        installed_packages = subprocess.check_output(["pip", "list"], universal_newlines=True)
        package_list = installed_packages.splitlines()[2:]  # 跳过标题行

        # 创建一个新的窗口，用于显示已安装的包
        top = tk.Toplevel(root)
        top.title("已安装的包")
        top.geometry("300x400")  # 设置窗口尺寸为200x200
        top.resizable(True, True)  # 允许用户调整窗口大小

        # 创建一个Frame来包含Listbox和Scrollbar
        frame = tk.Frame(top)
        frame.pack(expand=True, fill=tk.BOTH)

        # 创建Listbox显示已安装的包
        listbox = tk.Listbox(frame)
        listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # 创建Scrollbar并将其配置到Listbox
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

        # 将包列表插入到Listbox中
        for package in package_list:
            listbox.insert(tk.END, package)

        # 禁用编辑操作
        listbox.config(state=tk.DISABLED)

    except Exception as e:
        # 如果发生异常，显示错误信息
        easygui.msgbox(f"无法获取已安装的包: {str(e)}", title="错误")

# 加载配置
config = load_config()

# 创建主窗口
root = tk.Tk()
root.title("安装工具")

# 创建输入框
entry = ttk.Entry(root, width=50)
entry.place(x=20, y=20)

# 安装按钮回调函数
def install_package():
    package_name = entry.get()
    if not package_name:
        easygui.msgbox("请输入要安装的包名", title="错误")
        return

    mirror_source = mirror_source_var.get()
    mirror_url = get_mirror_sources().get(mirror_source, "")
    
    try:
        # 使用pip install命令安装包
        subprocess.check_call(
            ["python", "-m", "pip", "install", package_name, "-i", mirror_url]
        )
        easygui.msgbox(f"成功安装 {package_name}", title="成功")
    except subprocess.CalledProcessError as e:
        easygui.msgbox(f"安装失败: {str(e)}", title="错误")

# 卸载按钮回调函数
def uninstall_package():
    package_name = entry.get()
    if not package_name:
        easygui.msgbox("请输入要卸载的包名", title="错误")
        return

    mirror_source = mirror_source_var.get()
    mirror_url = get_mirror_sources().get(mirror_source, "")
    
    try:
        # 使用pip install命令安装包
        subprocess.check_call(
            ["python", "-m", "pip", "uninstall", "-y", package_name]
        )
        easygui.msgbox(f"成功卸载 {package_name}", title="成功")
    except subprocess.CalledProcessError as e:
        easygui.msgbox(f"卸载失败: {str(e)}", title="错误")
        
# 恢复默认值按钮回调函数
def reset_to_defaults():
    mirror_source_var.set(default_config["mirror_source"])

# 创建按钮
install_button = ttk.Button(root, text="安装", command=install_package)
install_button.place(x=20, y=70)

uninstall_button = ttk.Button(root, text="卸载", command=uninstall_package)
uninstall_button.place(x=110, y=70)

view_button = ttk.Button(root, text="查看已安装", command=view_installed_packages)
view_button.place(x=200, y=70)

reset_button = ttk.Button(root, text="恢复默认设置", command=reset_to_defaults)
reset_button.place(x=290, y=70)

# 创建镜像源复选框
mirror_source_label = ttk.Label(root, text="安装源:")
mirror_source_label.place(x=23, y=120)

mirror_source_var = tk.StringVar(value=config["mirror_source"])
mirror_sources = list(get_mirror_sources().keys())

mirror_source_combobox = ttk.Combobox(root, textvariable=mirror_source_var, values=mirror_sources, state='readonly')
mirror_source_combobox.place(x=80, y=120)

# 保存配置并退出
def on_close():
    config["mirror_source"] = mirror_source_var.get()
    save_config(config)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# 设置窗口大小和初始位置
root.geometry("400x200+100+100")

# 运行主循环
root.mainloop()