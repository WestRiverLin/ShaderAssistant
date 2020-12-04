# -*- encoding:utf8 -*-
from tkinter import *
from tkinter.messagebox import *
import tkinter.font as tf
import tkinter as tk
import tkinter.filedialog
import os


note = Tk()
note.title('Shader Assistant')
note.iconbitmap(".\\hand_128px.ico")
# 初始大小显示以及定位位置，注意一定要使用x而非*
note.geometry('800x600+200+200')

filename = ''

# 定义版本子菜单对应的相关函数
def autor():
    tkinter.messagebox.askokcancel('作者', 'Made by Lin Shangjing')

def about():
    tkinter.messagebox.askokcancel('版权', 'ShaderAssistant.Copyright')

# 定义文件子菜单对应的相应函数
def openfile():
    global filename
    filename = tkinter.filedialog.askopenfilename(defaultextension='.txt')

    if filename == '':
        filename = None
    else:
        note.title('新建文本:' + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r', encoding='utf-8')  # 注意后面要加上读取的编码格式，否则报编码错误
        textPad.insert(1.0, f.read())
        f.close()


def new():
    global filename
    note.title = ("新建文本")
    filename = None
    textPad.delete(1.0, END)


def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()


def saveas():
    global filename
    f = tkinter.filedialog.asksaveasfilename(initialfile='新建文本.txt', defaultextension='.txt')
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    note.title('新建文本:' + os.path.basename(f))


# 退出系统
def exit():
    # if askokcancel(note,'你确定要退出吗？'):
    note.destroy()


# 创建编辑子菜单的对于函数
def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


def selectAll():
    textPad.tag_add('sel', '1.0', END)


def search():
    topsearch = Toplevel(note)
    topsearch.geometry('300x30+200+250')
    labell = Label(topsearch, text='Find')
    labell.grid(row=0, column=0, padx=5)
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找')
    button1.grid(row=0, column=2)

# Shader功能
import shadercode

def addColorProperty():
    textPad.insert(tk.INSERT, shadercode.addColorProperty())

def addTextureProperty():
    textPad.insert(tk.INSERT, shadercode.addTextureProperty())

def addFloat1Property():
    textPad.insert(tk.INSERT, shadercode.addFloat1Property())

def addFloat2Property():
    textPad.insert(tk.INSERT, shadercode.addFloat2Property())

def addFloat3Property():
    textPad.insert(tk.INSERT, shadercode.addFloat3Property())

def addFloat4Property():
    textPad.insert(tk.INSERT, shadercode.addFloat4Property())

def addSchlickFresnelFunction():
    textPad.insert(tk.INSERT, shadercode.addSchlickFresnelFunction())

def addRGB2HSVFunction():
    textPad.insert(tk.INSERT, shadercode.addRGB2HSVFunction())

def addHSV2RGBFunction():
    textPad.insert(tk.INSERT, shadercode.addHSV2RGBFunction())

def addPseudoRandomFunction():
    textPad.insert(tk.INSERT, shadercode.addPseudoRandomFunction())

def addClassic2DPerlinNoiseFunction():
    textPad.insert(tk.INSERT, shadercode.addClassic2DPerlinNoiseFunction())

# 创建主菜单
menubar = Menu(note)
note.config(menu=menubar)

# 创建文件子菜单
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='文件', menu=filemenu)

filemenu.add_command(label='新建', accelerator='Ctrl+N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl+O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl+S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=saveas)
filemenu.add_command(label='退出', command=exit)



# 创建编辑子菜单
editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='编辑', menu=editmenu)

editmenu.add_command(label='撤销', accelerator='Ctrl+z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl+y', command=redo)
# 添加分割线
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl+X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl+C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl+V', command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl+F', command=search)
editmenu.add_command(label='全选', accelerator='Ctrl+A', command=selectAll)


# 创建 Shader 功能菜单
shaderMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Shader', menu=shaderMenu)

# 创建 添加变量 功能菜单
addShaderProperty = Menu(menubar, tearoff=False)
shaderMenu.add_cascade(label='变量', menu=addShaderProperty)

# 创建 Float参数 功能菜单
addFloatProperty = Menu(menubar, tearoff=False)
addShaderProperty.add_cascade(label='Float参数', menu=addFloatProperty)

# 添加命令
addShaderProperty.add_command(label='颜色', command=addColorProperty)
addShaderProperty.add_command(label='纹理贴图', command=addTextureProperty)
addFloatProperty.add_command(label='Float', command=addFloat1Property)
addFloatProperty.add_command(label='Float2', command=addFloat2Property)
addFloatProperty.add_command(label='Float3', command=addFloat3Property)
addFloatProperty.add_command(label='Float4', command=addFloat4Property)

# 创建 添加函数 功能菜单
addShaderFunction = Menu(menubar, tearoff=False)
shaderMenu.add_cascade(label='函数', menu=addShaderFunction)

addShaderFunction.add_command(label='Schlick菲涅尔近似', command=addSchlickFresnelFunction)
addShaderFunction.add_command(label='RGB转HSV', command=addRGB2HSVFunction)
addShaderFunction.add_command(label='HSV转RGB', command=addHSV2RGBFunction)
addShaderFunction.add_command(label='伪随机数', command=addPseudoRandomFunction)
addShaderFunction.add_command(label='经典2D柏林噪声', command=addClassic2DPerlinNoiseFunction)

# 添加版权子菜单
aboutmenu = Menu(menubar, tearoff=False)
aboutmenu.add_command(label='作者', command=autor)
aboutmenu.add_command(label='版权', command=about)
menubar.add_cascade(label='关于', menu=aboutmenu)

# 添加工具栏
toolbar = Frame(note, height=30, bg='#808080')
shortButton = Button(toolbar, text='打开', command=openfile, width=10, bg='#505050', fg='#B0B0B0', bd=0)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text='保存', command=save, width=10, bg='#505050', fg='#B0B0B0', bd=0)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO, fill=X)

# 添加状态栏
status = Label(note, text= "Line", bd=1, relief=SUNKEN, anchor=W, bg='#808080')
status.pack(side=BOTTOM, fill=X)

# 添加编辑界面以及滚动条
lnlabel = Label(note, width=2, bg='#505050')
lnlabel.pack(side=LEFT, fill=Y)

ft = tf.Font(size=10)
textPad = Text(note, undo=True, fg='#B0B0B0', background='#303030', insertbackground='#BBBBBB',\
               font = ft, selectbackground='#505090',selectforeground = '#D0D0D0',\
               spacing1 = 1,spacing2 = 1, spacing3 = 1)
textPad.pack(expand=YES, fill=BOTH)
textPad.focus_force()


scroll = Scrollbar(textPad)

textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

# 显示页面
note.mainloop()