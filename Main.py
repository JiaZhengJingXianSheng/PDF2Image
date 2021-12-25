#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/25 19:29
# @Author : LYZ

import shutil
import fitz
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
import os


class PDF2Image:

    def __init__(self):

        self.ui = QUiLoader().load('ui/Main.ui')
        self.ui.pathButton.clicked.connect(self.getPath)

        self.ui.executiveButton.clicked.connect(self.execute)
        self.path = ""

        self.ui.output.setReadOnly(True)

    def getPath(self):
        self.dialog = QFileDialog()
        # 设置文件过滤器
        self.dialog.setFileMode(QFileDialog.Directory)
        # 设置显示文件的模式，这里是详细模式
        self.dialog.setViewMode(QFileDialog.Detail)

        if self.dialog.exec_():
            self.fileNames = self.dialog.selectedFiles()
            self.path = self.fileNames[0]

        QApplication.processEvents()
        self.ui.output.appendPlainText("PDF路径为: " + str(self.path))
        QApplication.processEvents()

    def execute(self):
        self.ui.output.clear()
        self.ui.output.appendPlainText("PDF路径为: " + str(self.path))
        if os.path.exists(self.path + "/../Image"):
            QApplication.processEvents()
            self.ui.output.appendPlainText("发现Image文件夹，正在重建...")
            QApplication.processEvents()
            self.ui.output.appendPlainText("重建完成\n")
            QApplication.processEvents()
            shutil.rmtree(self.path + "/../Image")

        self.toImage()

    def toImage(self):
        for file in os.listdir(self.path):

            QApplication.processEvents()
            self.ui.output.appendPlainText(file + "\t正在处理...")
            QApplication.processEvents()
            os.makedirs(self.path + "/../Image/" + str(file))
            pdf = fitz.open(self.path + "/" + file)

            # 逐页读取PDF
            for pg in range(0, pdf.page_count):
                page = pdf[pg]
                pm = page.get_pixmap()
                # 开始写图像
                pm.save(self.path + "/../Image/" + str(file) + "/" + str(pg) + ".png")

            pdf.close()
            QApplication.processEvents()
            self.ui.output.appendPlainText(file + "\t处理完成\n")
            QApplication.processEvents()

        QMessageBox.about(self.ui, "结果", "成功，对应图片存放在Image文件夹下!")


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon("ICO.ico"))
    pdf2image = PDF2Image()
    pdf2image.ui.show()
    app.exec_()
