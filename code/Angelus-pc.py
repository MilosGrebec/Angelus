import customtkinter as ck
from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import webbrowser
import pygame
import cv2
import imutils
import threading
import socket
import struct
import pickle
import random
import urllib.request

class App:
    def __init__(self,window,window_title):
        self.window=window
        self.window.title(window_title)

        self.vid = cv2.VideoCapture(1)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.frame1= ck.CTkFrame(master=window)
        self.frame1.pack(pady=20,padx=60,fill="both",expand=True)

        self.label = ck.CTkLabel(master=self.frame1, text="Angelus", font=("Roboto",30))
        self.label.pack(pady=12,padx=10)

        self.con = ck.CTkLabel(master=self.frame1, text="NOT CONNECTED", font=("Roboto", 20))
        self.con.pack(padx=10)

        self.host_ip = '192.168.1.8'
        host_name = socket.gethostname()
        host_ip = host_ip = socket.gethostbyname(host_name)
        text2 = "If host IP, isn't working"
        text3 = "Go to cmd and input ipconfig, then input that ip"

        self.conn_text2 = ck.CTkLabel(master=self.frame1, text=text2, font=("Roboto", 13), anchor="nw")
        self.conn_text2.pack(pady=1, padx=10, anchor=NW)

        self.conn_text3 = ck.CTkLabel(master=self.frame1, text=text3, font=("Roboto", 13), anchor="nw")
        self.conn_text3.pack(pady=1, padx=10, anchor=NW)

        self.videoframe=ck.CTkCanvas(master=self.frame1)
        self.videoframe.pack(pady=30,padx=70)

        texth = "Host IP: " +host_ip

        self.text = ck.CTkLabel(master=self.frame1, text=texth, font=("Roboto",24), anchor="nw")
        self.text.pack(pady=12,padx=10)

        self.text2 = " "

        self._, self.start_frame = self.vid.read()

        self.start_frame = imutils.resize(self.start_frame, width=500)
        self.start_frame = cv2.cvtColor(self.start_frame, cv2.COLOR_BGR2GRAY)
        self.start_frame = cv2.GaussianBlur(self.start_frame, (21, 21), 0)

        self.alarm = False
        self.alarm_mode = False
        self.alarm_counter = 0

        self.button = ck.CTkButton(master=self.frame1, text="START", command=self.start)
        self.button.pack(pady=12,padx=12)

        self.press = ck.CTkLabel(master =self.frame1, text="after you input your IP addres press START to connect", font=("Roboto",18), anchor="nw")
        self.press.pack(pady=12,padx=12)


        self.entry = ck.CTkEntry(self.frame1, width=250)
        self.entry.pack(pady=10)

        self.slider = ck.CTkSlider(master=self.frame1, from_=0, to=5000, command=self.update_thresh)
        self.slider.pack(pady=12,padx=12)

        self.slider_text = ck.CTkLabel(master= self.frame1, text="TURN LEFT FOR MORE SENSITIVITY", font = ("Roboto",15), anchor="nw")
        self.slider_text.pack(pady=12,padx=12)
        self.diff = 2500

        frame1_bg_color = "black"

        self.button_image = ck.CTkImage(Image.open("angelus.png"), size=(200, 200))

        self.image_button = ck.CTkButton(master=self.frame1,image=self.button_image, text="", command=self.sound, fg_color="transparent")
        self.image_button.pack(side="bottom", anchor="se",padx=40,pady=40)


        self.window.mainloop()

    def update_thresh(self,value):
        self.diff = value

    def sound(self):
        threading.Thread(target=self.play_sound_thread).start()

    def play_sound_thread(self):
        pygame.mixer.init()
        pygame.mixer.music.load("zvukovi/hii.mp3")
        pygame.mixer.music.play()
        while True:
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:

                audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google_cloud(audio, "key.json")
                print(text)
                input_text = text
                expected_text="who are you"
                if expected_text.lower() in input_text.lower():
                    print("wow")
                    pygame.mixer.init()
                    pygame.mixer.music.load("zvukovi/who_are_you.mp3")
                    pygame.mixer.music.play()
                expected_text = "where is"
                if expected_text.lower() in input_text.lower():
                    pygame.mixer.init()
                    pygame.mixer.music.load("zvukovi/here.mp3")
                    pygame.mixer.music.play()
                    location = input_text.lower().replace(expected_text.lower(),"")
                    maps_url = f"https://www.google.com/maps/place/{location}"
                    webbrowser.open(maps_url)
                expected_text = "search"
                if expected_text.lower() in input_text.lower():
                    pygame.mixer.init()
                    pygame.mixer.music.load("zvukovi/sure.mp3")
                    pygame.mixer.music.play()
                    search = input_text.lower().replace(expected_text.lower(),"")
                    search_url = f"www.google.com./search?q=" + search
                    webbrowser.open(search_url)
                expected_text = "when are you happy"
                if expected_text.lower() in input_text.lower():
                    pygame.mixer.init()
                    pygame.mixer.music.load("zvukovi/happy.mp3")
                    pygame.mixer.music.play()
                expected_text = "sing me a song"
                if expected_text.lower() in input_text.lower():
                    x = random.randint(1,5)
                    if x==1:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/music1.MP3")
                        pygame.mixer.music.play()
                    elif  x==2:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/music2.MP3")
                        pygame.mixer.music.play()
                    elif x == 3:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/music3.MP3")
                        pygame.mixer.music.play()
                    elif x == 4:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/music4.MP3")
                        pygame.mixer.music.play()
                expected_text = "give me a random fact"
                if expected_text.lower() in input_text.lower():
                    y = random.randint(1,4)
                    if y==1:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/facts1.MP3")
                        pygame.mixer.music.play()
                    elif y==2:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/facts2.MP3")
                        pygame.mixer.music.play()
                    elif y == 3:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/facts34.MP3")
                        pygame.mixer.music.play()
                    elif y == 4:
                        pygame.mixer.init()
                        pygame.mixer.music.load("zvukovi/facts4.MP3")
                        pygame.mixer.music.play()
                expected_text= "stop"
                if expected_text.lower() in input_text.lower():
                    pygame.mixer.init()
                    pygame.mixer.music.load("zvukovi/bye.mp3")
                    pygame.mixer.music.play()
                    break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    def start(self):
        self.user_input = self.entry.get()
        self.text2 = self.button.cget("text")
        if self.text2 == "START":
            self.text.configure(text="HOST IP: " + self.user_input)
            client_thread = threading.Thread(target=self.connect)
            client_thread.start()
            self.button.configure(text="STOP")
            self.text2 = self.button.cget("text")
        else:
            self.window.destroy()
            self.button.configure(text="START")

    def connect(self):
        self.user_input = self.entry.get()
        self.host_ip = self.user_input
        self.entry.destroy()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 1055
        port2 = 1077
        socket_address = (self.host_ip, port)
        data_address = (self.host_ip, port2)

        server_socket.bind(socket_address)
        data_socket.bind(data_address)
        server_socket.listen(5)
        data_socket.listen(5)

        print("LISTENING AT: ", socket_address)
        print("LISTENING AT: ", data_address)
        client_socket, addr = server_socket.accept()
        client_data, addr2 = data_socket.accept()
        print('GOT CONNECTION FROM: ', addr)
        print('GOT CONNECTION FROM: ', addr2)
        self.con.configure(text="CONNECTED")
        self.press.configure(text="press STOP to exit")
        self.update_frame(client_socket,client_data)


    def alarm_data(self,client_data):
        _, frame2 = self.vid.read()
        frame2 = imutils.resize(frame2, width=500)
        if self.alarm_mode:
            frame_bw = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

            difference = cv2.absdiff(frame_bw, self.start_frame)
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
            self.start_frame = frame_bw
            if threshold.sum() > self.diff:
                self.alarm_counter += 1
                data_thread = threading.Thread(target=self.moves, args=(client_data,))
                data_thread.start()
            else:
                if self.alarm_counter > 0:
                    self.alarm_counter -= 1
            notmoving = threading.Thread(target=self.not_moving,args=(client_data,))
            notmoving.start()
        if self.alarm_counter > 10:
            if not self.alarm:
                self.alarm = True
        self.alarm_mode = not self.alarm_mode
        self.alarm_counter = 0

    def update_frame(self,client_socket,client_data):
        ret, frame = self.vid.read()
        socket_thread = threading.Thread(target=self.send_frame, args=(frame,client_socket))
        socket_thread.start()
        alarm_thread = threading.Thread(target=self.alarm_data, args=(client_data,))
        alarm_thread.start()
        if self.text2 == "STOP":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            self.videoframe.img = img_tk
            self.videoframe.create_image(0, 0, anchor=ck.NW, image=img_tk)
        frame_rate_interval = int(1000 / 30)
        self.window.after(frame_rate_interval, lambda: self.update_frame(client_socket,client_data))


    def moves(self, client_data):
        client_data.send(str(5).encode())

    def not_moving(self, client_data):
        client_data.send(str(0).encode())

    def send_frame(self,frame,client_socket):
        a = pickle.dumps(frame)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)

    def __del__(self):
        self.vid.release()

ck.set_appearance_mode('dark')
ck.set_default_color_theme('dark-blue')

root = ck.CTk()
root.geometry("1100x1000")
app=App(root,"Angelus")