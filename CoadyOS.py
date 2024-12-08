import os
import json
from time import sleep as sp
first_use = True
version = '1.0.0'

def oobe():
    # 定义语言文本
    global languages
    languages = {
        "English": {
            "welcome": "Welcome to CoadyOS " + version,
            "setup_message": "Before you can use CoadyOS, you need to set up your system.",
            "language_choice": "Choose your usable language:",
            "english_option": "1. English",
            "chinese_option": "2. 中文",
            "exit_option": "3. Exit",
            "english_selected": "Yeah! English is the first language.",
            "chinese_selected": "太棒了！你的首选语言是中文。",
            "username_prompt": "Enter your username:",
            "password_prompt": "Enter your password:",
            "setup_complete": "Setup complete!"
        },
        "Chinese": {
            "welcome": "欢迎使用 CoadyOS " + version,
            "setup_message": "在您使用 CoadyOS 之前，您需要设置系统。",
            "language_choice": "请选择您的可用语言：",
            "english_option": "1. 英语",
            "chinese_option": "2. 中文",
            "exit_option": "3. 退出",
            "english_selected": "好的！英语是首选语言。",
            "chinese_selected": "太棒了！您的首选语言是中文。",
            "username_prompt": "请输入您的用户名：",
            "password_prompt": "请输入您的密码：",
            "setup_complete": "设置完成！",
            "ch_user": "你正在登录管理员账户，是否继续？[y/n]"
        }
    }
    
    print(languages["English"]["welcome"])
    print(languages["English"]["setup_message"])
    print(languages["English"]["language_choice"])
    print(languages["English"]["english_option"])
    print(languages["English"]["chinese_option"])
    print(languages["English"]["exit_option"])

    language = input(">>")
    if language == "1":
        lang = "English"
        print(languages[lang]["english_selected"])
    elif language == "2":
        lang = "Chinese"
        print(languages[lang]["chinese_selected"])
    elif language == "3":
        print("Exiting setup.")
        return
    else:
        print("Invalid choice. Exiting setup.")
        return

    # 获取用户名和密码
    username = input(languages[lang]["username_prompt"])
    password = input(languages[lang]["password_prompt"])

    # 初始化或读取 boot_config
    global boot_config
    if os.path.exists("boot.json"):
        with open("boot.json", "r") as f:
            boot_config = json.load(f)
    else:
        boot_config = {}

    # 更新 boot.json 文件
    boot_config["username"] = username
    boot_config["password"] = password

    with open("boot.json", "w") as f:
        json.dump(boot_config, f, indent=4)

    print(languages[lang]["setup_complete"])

def boot():
    print(f"Booting CoadyOS version {version}")
    sp(0.2)
    print("Check Files...")
    sp(0.2)
    sp(0.2)
    sp(0.2)
    if not os.path.exists("boot.json"):
        print("boot.json not found. ")
        sp(0.2)
        sp(0.2)
        print('Error code:0x000001')
    else:
        print("boot.json found.")
    sp(0.2)
    if not os.path.exists("./mnt.json"):
        print("mnt.json not found. ")
        print('Error code:0x000002')
    else:
        print("mnt.json found.")
        print('System will still run with some errors.')
    sp(0.2)
    if first_use:
        oobe()
    else:
        print("Starting...")

def login():
    username = input("Username: ")
    password = input("Password: ")

    # 检查 boot.json 文件是否存在
    if not os.path.exists("boot.json"):
        print("User data not found. Please set up your system first.")
        return "NaN"

    # 读取 boot.json 文件中的用户信息
    with open("boot.json", "r") as f:
        user_data = json.load(f)

    # 验证用户名和密码
    if user_data.get("username") == username and user_data.get("password") == password:
        return "successful"
    else:
        return "failed"
def system():
    gh = login()
    if gh == "successful":
        print("Login Successful 登录成功")
        pass
    else:
        print("Login Failed 登录失败")
        gh = login()
        if gh == "successful":
            print("Login Successful 登录成功")
            pass
        else:
            print("Login Failed 登录失败")
            gh = login()
            if gh == "successful":
                print("Login Successful 登录成功")
                pass
            else:
                print("Login Failed 登录失败")
                gh = login()
                if gh == "successful":
                    print("Login Successful 登录成功")
                    pass
                else:
                   print("Login Failed 登录失败")
                   quit()    
    print(r'''
  ____                _        ___  ____    _   ___  
 / ___|___   __ _  __| |_   _ / _ \/ ___|  / | / _ \
| |   / _ \ / _` |/ _` | | | | | | \___ \  | || | | |
| |__| (_) | (_| | (_| | |_| | |_| |___) | | || |_| |
 \____\___/ \__,_|\__,_|\__, |\___/|____/  |_(_)___/
                        |___/
 ____                 _
|  _ \ _ __ _____   _(_) _____      __
| |_) | '__/ _ \ \ / / |/ _ \ \ /\ / /
|  __/| | |  __/\ V /| |  __/\ V  V /
|_|   |_|  \___| \_/ |_|\___| \_/\_/

          ''')
    while True:
        k = 0
        command1 = input(">>")
        command = command1.split()
        times = len(command)
        for i in range(times):
            if command[k] == "help":
                print('''
                This Terminal is CoadyOS Terminal.
                You can use it to do some things.
                Like:
                    open file
                    remove file
                    ......
                Have a good day.
                    ''')
                k += 1
            if command[k] == "echo":
                print(command[k + 1])

            if command[k] == "chuser":
                try:
                    ch_user = command[k + 1]
                    with open("user.json".r) as userdata:
                        if userdata.get("admin") == ch_user:
                            print(languages.get(Chinese))
                            continue
                except:
                    continue
                finally:
                    print(r'''
 ____            _                   _____
/ ___| _   _ ___| |_ ___ _ __ ___   | ____|_ __ _ __ ___  _ __
\___ \| | | / __| __/ _ \ '_ ` _ \  |  _| | '__| '__/ _ \| '__|
 ___) | |_| \__ \ ||  __/ | | | | | | |___| |  | | | (_) | |
|____/ \__, |___/\__\___|_| |_| |_| |_____|_|  |_|  \___/|_|
       |___/

                          
                          
                          ''')
                    quit()
                    

def main():
    boot()
    system()

class tools:
    @staticmethod
    def calculator():
        pass

    @staticmethod
    def notepad():
        pass

    @staticmethod
    def ballgame():
        pass

if __name__ == "__main__":
    main()