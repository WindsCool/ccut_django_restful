import tkinter as tk
import requests
from Base import Base
class Login(Base):
    def __init__(self):
        super().__init__()
        self.window.title('CCUT登录')
        self.window.geometry('380x300')
        self.canvas = tk.Canvas(self.window, height=200, width=500)
        self.image_file = tk.PhotoImage(file='welcome.gif')
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')
        tk.Label(self.window, text='User name: ').place(x=50, y= 150)
        tk.Label(self.window, text='Password: ').place(x=50, y= 190)
        self.var_user_name = tk.StringVar()
        self.var_user_name.set('201xxxxx')
        self.entry_user_name = tk.Entry(self.window, textvariable=self.var_user_name)
        self.entry_user_name.place(x=160, y=150)
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=160, y=190)

        self.btn_login = tk.Button(self.window, text='Login', command=self.login)
        self.btn_login.place(x=170, y=230)
        self.btn_sign_up = tk.Button(self.window, text='Sign up', command=self.signup)
        self.btn_sign_up.place(x=270, y=230)
        self.is_login=''

    def login(self):
        user_id = self.entry_user_name.get()
        user_password = self.entry_usr_pwd.get()
        data = {'user_id':user_id,'user_password':user_password}
        r = requests.post(url='http://127.0.0.1:8000/login/', json=data).text
        if r == 'error':
            self.destroy()
        else:
            self.is_login = eval(r)['user_id']

    def signup(self):
        pass

a = Login()
a.start()
