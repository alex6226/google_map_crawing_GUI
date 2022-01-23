import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image, ImageDraw
from crawing_model import *

# 創建一個視窗
app = tk.Tk()
# 視窗名稱
app.title('Google評論爬蟲app')
# 視窗大小
app.geometry('300x530')
# 背景顏色
app.configure(background='gray')
# 固定視窗大小
app.resizable(width=0, height=0)
# 背景圖片
img = ImageTk.PhotoImage(Image.open('images.png'))
label = tk.Label(app, height=150, width=300, bg='gray94', fg='red', image=img)
label.pack(padx=0, pady=0)

# 背景圖片
img2 = ImageTk.PhotoImage(Image.open('使用流程.jpg'))
# label2 = tk.Label(app, width=200, height=250,  bg='gray94', fg='red', image=img2)
# label2.pack(padx=0, pady=100)
label2 = tk.Label(app, image=img2)
label2.place(x=48, y=260, width=202, height=250)
# 字體設計
font_type = tkFont.Font(family="微軟正黑體", size=10, weight="bold")


def GUI():
    # 按鈕觸發事件
    def button_event():
        if input_button.get() != '':
            prompt_text['text'] = '請選擇要爬取評論的店家'

            # 設為全局變量
            global input_button2
            global store_dict

            store_dict = get_interrelate_store_name(input_button.get())

            # 下拉選單
            input_button2 = ttk.Combobox(app,
                                         values=list(store_dict.keys()), state="readonly")
            input_button2.place(x=60, y=190, width=175, height=25)
            input_button2.current(0)
            # Button['command']=button_event2
            Button['command'] = button_event2

    def button_event2():

        if input_button2.get():

            store_name = input_button2.get()
            store_id = store_dict[store_name]

            comment_df = get_comment(store_id)
            comment_df.to_csv(f'{store_name}.csv',
                              encoding='utf-8-sig', index=False)
            prompt_text['text'] = '資料爬取完成'
            Button['text'] = '完成'
            Button['command'] = button_event3

    def button_event3():

        if input_button.get():

            GUI()

    # 輸入框
    input_button = tk.Entry(app, bd=3)
    # input_button.pack(side='top',ipadx=20, pady=20)
    input_button.place(x=60, y=190, width=175, height=25)
    # 提示文字/bg:背景色/fg:字體色
    prompt_text = tk.Label(app, text='請輸入要爬取評論的店家關鍵字', bg="gray", fg="black")
    prompt_text.place(x=57, y=170)
    prompt_text.configure(font=font_type)
    # 按鈕
    Button = tk.Button(app, text='送出', command=button_event)
    Button.place(x=130, y=220)
    Button.configure(font=font_type)

GUI()
app.mainloop()  # 執行視窗
