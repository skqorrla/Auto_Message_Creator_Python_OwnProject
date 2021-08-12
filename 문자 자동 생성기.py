from tkinter import *
from tkinter import messagebox
import tkinter.ttk

window = tkinter.Tk()

#윈도우창 속성 설정 
window.title("윤대영어 문자 생성 프로그램")
window.geometry("800x600")
window.resizable(1,1)
title = Label(window, text="안내문 작성")
title.pack()

#Notebook 생성
notebook = tkinter.ttk.Notebook(window, width=800, height=600, takefocus=True)
notebook.pack(expand=True)

#frame1
frame1 = tkinter.ttk.Frame(notebook, width=400, height=280)
frame1.pack(expand=True)
notebook.add(frame1, text="1. 학생 정보 불러오기")

#frame2
frame2 = Frame(window)
notebook.add(frame2, text="2. 진행 강좌 및 진도 안내")

#frame3
frame3 = Frame(window)
notebook.add(frame3, text="3. TEST 안내")

#frame4
frame4 = Frame(window)
notebook.add(frame4, text="4. 과제물 안내")

#frame5
frame5 = Frame(window)
notebook.add(frame5, text="5. 안내사항")

#frame6
frame6 = Frame(window)
notebook.add(frame6, text="6. 개인 안내사항")

#윈도우창 무한 실행 
window.mainloop()


