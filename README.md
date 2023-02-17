# Library-Service-Project

API for library with next futures:
<li>
Added and manage books
<li>
Added borrowing
<li>
Added payments for borrowing
<li>
Notifications for borrowing in telegram chat

## Installing/Getting started 

Fork the repo (GitHub repository)
Clone the forked repo
```shell
git clone https://github.com/maxitoska/Library-Service-Project.git -b develop
```
You can get the link by clicking the Clone or download button in your repo
Open the project folder in your IDE
Open a terminal in the project folder
Create a branch for the solution and switch on it
```shell
git checkout -b master
```
You can use any other name instead of master
If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
initilize enviroment variables .env (hint in .env.sample file)
For retrive the notifications you can create telegram bot and inicialize his token in .env file or Use my test Token in .env.sample
Easy way to find your Telegram chat_id is:

Tap to open the Telegram app.
In the top-right corner, tap on the small magnifying glass icon.
Type @RawDataBot in the search dialog box and then tap the search icon
open conversation with Telegram Bot Raw
write /start
your chat_id is "chat" : {"id": your_id_here}


## Links
You can test api on the next links:
<li>
Get your jwt token: http://127.0.0.1:8000/api/user/token/
<li>
Book API: http://127.0.0.1:8000/api/
<li>
Borrowing API: http://127.0.0.1:8000/api/borrowings/
<li>
Payment API: http://127.0.0.1:8000/api/payments/
<li>
Use key "Authorize" in header for jwt token(use Google Chrome extension ModHeader)
<li>
For change notifications text message add to telegram function your information (borrowings.telegram_notification)
<li>
To test admin functionality use email: max@admin.com password: 123
