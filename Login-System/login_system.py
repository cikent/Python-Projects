import datetime
import sys
import login_page
import forgot_password_page
import create_account_page
import users_profile_page

# variable declarations
time_now = datetime.datetime.now()
valid_users = {}
user_username = ""
user_email = ""
user_password = ""

# session info
print(sys.version)
print(sys.executable)
print(time_now)

# login_system functional code
login_page.login_system_greeting()
login_page.user_action_prompt()

