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

## Installing / Getting started 
```shell

git clone https://github.com/maxitoska/Library-Service-Project.git -b develop
cd Library-Service-Project
initilize enviroment variables .env (hint in .env.sample file)
For retrive the notifications you must create telegram bot and inicialize his token in .env file
```
## Links
You can test api on the next links:
<li>
Get your jwt token: http://127.0.0.1:7000/api/user/token/
<li>
Book API: http://127.0.0.1:7000/api/
<li>
Borrowing API: http://127.0.0.1:7000/api/borrowings/
<li>
Use key "Authorize" in header for jwt token(use Google Chrome extension ModHeader)
<li>
For change notifications text message add to telegram function your information (borrowings.telegram_notification)
<li>
To test admin functionality use email: max@admin.com password: 123
