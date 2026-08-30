from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import socket
import threading

class ZakiMobileApp(App):
    def build(self):
        self.title = "Zaki Mobile Client"
        
        layout = BoxLayout(orientation='vertical', padding=25, spacing=12)
        
        layout.add_widget(Label(text="Mobile Control Panel", font_size=20, bold=True, color=(0.17, 0.24, 0.31, 1), size_hint_y=None, height=35))
        
        layout.add_widget(Label(text="Password:", font_size=12, color=(0.5, 0.5, 0.5, 1), size_hint_y=None, height=15))
        self.pass_input = TextInput(password=True, multiline=False, font_size=13, size_hint_y=None, height=35)
        layout.add_widget(self.pass_input)
        
        layout.add_widget(Label(text="Server IP / Ngrok URL:", font_size=12, color=(0.5, 0.5, 0.5, 1), size_hint_y=None, height=15))
        self.ip_input = TextInput(multiline=False, font_size=13, size_hint_y=None, height=35)
        layout.add_widget(self.ip_input)
        
        connect_btn = Button(text="Connect to PC", background_color=(0, 0.47, 0.83, 1), font_size=14, size_hint_y=None, height=40)
        connect_btn.bind(on_press=self.start_connection_thread)
        layout.add_widget(connect_btn)
        
        self.status_lbl = Label(text="Status: Disconnected", font_size=11, color=(0.8, 0.2, 0.2, 1), size_hint_y=None, height=25)
        layout.add_widget(self.status_lbl)

        # Control Buttons (PC ko command bhejne ke liye)
        cmd_btn = Button(text="Send Command to PC", background_color=(0.1, 0.6, 0.2, 1), font_size=14, size_hint_y=None, height=40)
        cmd_btn.bind(on_press=self.send_control_command)
        layout.add_widget(cmd_btn)
        
        layout.add_widget(Label(text="Muhammad Zaki Rajput | Snapchat: @ZAK_GATTIG | Mob. +923459657516", font_size=8, color=(0.6, 0.6, 0.6, 1)))
        
        return layout

    def start_connection_thread(self, instance):
        if self.pass_input.text != "ZakiRajput":
            self.status_lbl.text = "Status: Ghalat Password!"
            self.status_lbl.color = (0.8, 0.2, 0.2, 1)
            return
            
        server_address = self.ip_input.text.strip()
        if not server_address:
            self.status_lbl.text = "Status: IP/URL enter karein!"
            self.status_lbl.color = (0.8, 0.2, 0.2, 1)
            return
            
        self.status_lbl.text = "Connecting..."
        self.status_lbl.color = (0.9, 0.6, 0.1, 1)
        
        threading.Thread(target=self.connect_server, args=(server_address,), daemon=True).start()

    def connect_server(self, target_url):
        try:
            if "tcp://" in target_url:
                target_url = target_url.replace("tcp://", "")
            elif "https://" in target_url:
                target_url = target_url.replace("https://", "")
            elif "http://" in target_url:
                target_url = target_url.replace("http://", "")
            
            parts = target_url.split(":")
            host = parts[0]
            port = int(parts[1])

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send("Hello from Zaki Mobile App!".encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            
            self.status_lbl.text = f"Connected! Resp: {response}"
            self.status_lbl.color = (0.1, 0.6, 0.2, 1)
            client.close()
        except Exception as e:
            self.status_lbl.text = f"Failed: {e}"
            self.status_lbl.color = (0.8, 0.2, 0.2, 1)

    def send_control_command(self, instance):
        server_address = self.ip_input.text.strip()
        if not server_address:
            self.status_lbl.text = "Status: Pehle Connect karein!"
            return
        try:
            target_url = server_address.replace("tcp://", "").replace("https://", "").replace("http://", "")
            parts = target_url.split(":")
            host = parts[0]
            port = int(parts[1])

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send("COMMAND: ACTION_CLICK".encode('utf-8'))
            client.close()
            self.status_lbl.text = "Command Sent Successfully!"
            self.status_lbl.color = (0.1, 0.6, 0.2, 1)
        except Exception as e:
            self.status_lbl.text = f"Command Failed: {e}"
            self.status_lbl.color = (0.8, 0.2, 0.2, 1)

if __name__ == '__main__':
    ZakiMobileApp().run()