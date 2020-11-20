#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author: anne.yang

from win32com.client import gencache, Dispatch, constants
import pythoncom
import os


# 文件转换逻辑
class PDFConverter:
    """office文件转换为PDF"""
    def __init__(self, pathname):
        self._handle_postfix = ['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx']  # 支持转换的文件类型
        self._filename_list = list()   # 列出文件
        self._export_folder = os.path.join(os.path.abspath('E:\\test\\'), 'PDF\\')   # 将路径进行拼接
        print('===========导出路径是：', self._export_folder)
        if not os.path.exists(self._export_folder):
            os.mkdir(self._export_folder)
        self._enumerate_filename(pathname)

    def _enumerate_filename(self, pathname):
        # 读取所有文件名
        full_pathname = os.path.abspath(pathname)  # 返回绝对路径
        print('===========文件路径是：', full_pathname)
        if os.path.isfile(full_pathname):  # 判断是否为文件
            if self._is_legal_postfix(full_pathname):   # 判断文件后缀
                self._filename_list.append(full_pathname)
            else:
                raise TypeError('文件{}后缀名不合法！仅支持如下文件类型：{}'.format(pathname, '、'.join(self._handle_postfix)))
        elif os.path.isdir(full_pathname):  # 判断是否为目录
            for root, dirs, files in os.walk(full_pathname):  # os.walk()通过在目录树中游走输出在目录中的文件名，向上或者向下
                print('root={},\ndirs={},\nfiles={}\n'.format(root, dirs, files))
                for name in files:
                    filename = os.path.join(root, name)   # 将目录和文件名合成一个路径
                    print('=============文件完整路径是：', filename)
                    if self._is_legal_postfix(filename):
                        self._filename_list.append(os.path.join(filename))
        else:
            raise TypeError('文件/文件夹{}不存在或不合法！'.format(pathname))

    def _is_legal_postfix(self, filename):
        # basename()返回文件名
        return filename.split('.')[-1].lower() in self._handle_postfix and not os.path.basename(filename).startswith('~')

    def run_convert(self):
        print('需要转换的文件数是：', len(self._filename_list))
        for filename in self._filename_list:
            postfix = filename.split('.')[-1].lower()
            # postfix是文件后缀，每个后缀都有一个方法，故这里返回pdfConverter实例的方法doc()/ppt()/xls()等的地址
            funcCall = getattr(self, postfix)
            # print(type(funcCall), funcCall)
            print('原文件：', filename)
            funcCall(filename) # funcCall指向的是pdfConverter.doc()/xls()/ppt()等方法的地址，故可以直接调用
        print('转换完成！')

    # doc/docx转换为PDF
    def doc(self, filename):
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        print('保存PDF文件：', exportfile)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        pythoncom.CoInitialize()
        w = Dispatch("Word.Application")
        pythoncom.CoInitialize()  # 加上防止 CoInitialize 未加载
        doc = w.Documents.Open(filename)
        doc.ExportAsFixedFormat(exportfile, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        w.Quit(constants.wdDoNotSaveChanges)

    def docx(self, filename):
        self.doc(filename)

    # ppt/pptx 转换为 PDF
    def ppt(self, filename):
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        pythoncom.CoInitialize()
        p = Dispatch("PowerPoint.Application")
        pythoncom.CoInitialize()
        ppt = p.Presentations.Open(filename, False, False, False)
        ppt.ExportAsFixedFormat(exportfile, 2, PrintRange=None)
        print('保存 PDF 文件：', exportfile)
        p.Quit()

    def pptx(self, filename):
        self.ppt(filename)

    # xls/xlsx 转换为 PDF
    def xls(self, filename):
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        pythoncom.CoInitialize()
        xlApp = DispatchEx("Excel.Application")
        pythoncom.CoInitialize()
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(filename, False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        print('保存 PDF 文件：', exportfile)
        xlApp.Quit()

    def xlsx(self, filename):
        self.xls(filename)

if __name__ == '__main__':
    '''
    支持文件夹批量导入, 也支持单个文件的转换
    '''
    pathname = r"E:\test\test-2"
    pdfConverter = PDFConverter(pathname)
    pdfConverter.run_convert()

