# Discord-Group-Call

This is a simple Python project that collects HTML data from a Discord group to create a database of calls that happened in the group (or DM conversation).

<br>

# How it works?

The program uses [selenium](https://github.com/SeleniumHQ/selenium/tree/trunk) to control a browser, which will analyze the Discord HTML for collecting call data.

1. When the program is launched, the user can login to Discord and will then be automatically redirected to the link of the group chat (entered in `main.py`) that they wish to log.

3. After that, the user can simply press enter in the console, and the program will simulate pressing the `Page Up` key on the keyboard to go through the entire group chat.

4. Every time the program finds an HTML `<div>` with the call class (`content__235ca`), it will be analyzed, extracting the **user who started the call**, **the length of the call**, and the **time of the call**. All of this will be saved to an SQLite database.

5. Once the program is done going through the chat, the user can press `Ctrl + C` in the console to end the program.

⚠ All the browser data and login token for Discord ect. are saved in `data/selenium_browser_profile` be careful with this folder! (For dev its not tracked by Git)

**Console extracting calls:**

<img src="https://github.com/user-attachments/assets/e8259974-a5d5-4521-97f4-e1fda5cbcdad" width="500">

<br>

# What to do with the data?

The data collected can be used for making stats and analyze the call habbits of you and your friends, like how long you all spend on calls, average call length, who starts calls the most ect

There is a couple data analyzing programs in the `tools` directory but nothing too advanced.

**Data analyzing examples:**

<img src="https://github.com/user-attachments/assets/de9579f5-0d2f-464a-b222-1246e7c20352" width="400">
<img src="https://github.com/user-attachments/assets/a3b0a148-8a22-4cd3-a154-2d26073f68b9" width="400">

