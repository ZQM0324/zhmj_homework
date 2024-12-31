# -*- coding: utf-8 -*-


from sys import argv, exit
import os
from PyQt5.QtWidgets import QApplication

from DrowsinessDetecting import Drowsiness_MainWindow



if __name__ == '__main__':
    # 创建 PyQt 应用
    app = QApplication(argv)
    # 创建并显示主窗口
    win = Drowsiness_MainWindow()
    win.showTime()

    # 执行应用
    exit_code = app.exec_()

    file_path = "环境配置.txt"
    if os.path.exists(file_path):
        os.remove(file_path)

    file_path1 = r"C:\pycharm\vedio\基于YOLOV5的疲劳驾驶检测系统\DrowsinessDetection\使用须知.txt"
    if os.path.exists(file_path1):
        os.remove(file_path1)

    exit(exit_code)
