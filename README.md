# Amethyst Administrator

![Logo](resources/pic/logo/logoNormal.png)

### Install and Run:

1) Create a Python venv: `python3 -m venv ./AmethystAdministratorEnviroment`.
2) Clone the repo: `git clone https://github.com/glob-bruh/AmethystAdministrator`.
3) Install required libraries: `pip3 install -r requirements.txt`. 
4) Run main: `python3 main.py`.

### 

![Screenshot](demo.png)

### Development Checklist:

- [x] Put windows in classes.
- [x] Remove client from main window.
- [x] Edit client. 
- [ ] Find ways (or build a function) to refresh/update both the entire canvas and TreeViews.
- [ ] Finish services/TCP ports manager.
  - [x] Add service/port.
  - [x] Remove service/port.
  - [ ] Edit service/port.
- [x] Smaller images on canvas.
- [ ] Scrollbar for canvas (to see other parts of canvas).
- [x] Art assets.
- [ ] Save/load functionality.
  - [ ] Export/Save to file.
  - [ ] Load file/data.
- [ ] Lines between hosts on canvas. 
- [ ] Subnet calculations/processing.
- [ ] IP address calculations/processing.
  - [x] IPv4 address valid verify.
- [ ] Auto ping clients and show results (https://denizhalil.com/2024/04/06/sending-icmp-packets-with-python-socket-adventure-in-signaling/).
  - [x] Contain in its own classed thread.
  - [ ] Program can send a ping.
  - [ ] Program can receive and read a ping.
  - [ ] Ping statistics are functional and can be displayed.
- [x] TkInter terminal.
- [x] Come up with flashy name.
- [ ] Secure password storage (in memory and on disk).
- [ ] Cloud manager (M365).
  - [x] Connecting to client opens Graph terminal.
  - [ ] Graph API cloud management.
  - [ ] Cloud manager GUI. 
- [ ] Implement the ability to connect to clients over various protocols (in order of importance):
  - [x] Android Debug Bridge.
  - [ ] Terminals - SSH and Telnet.
    - [ ] Local PowerShell session service (with persistence).
  - [ ] File Transfer - FTP, SFTP and SAMBA.
  - [ ] Remote Administration - Remote PowerShell Command Execution, etc.

### Contributors:

<a href="https://github.com/glob-bruh/ArmitageBootleg/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=glob-bruh/ArmitageBootleg" />
</a>

### License:

This project is licensed under [The 3-Clause BSD License](https://opensource.org/license/bsd-3-clause).
