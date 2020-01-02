# Define the functions necessary for the script
def login_system_greeting():
    print(
        """
    Thank you for visiting <Application Name>. If you already have an Account, please Log in.

    If you don't have an account, that's okay, you're just a couple steps away. Sign up today!
    """
    )


def user_action_prompt():
    print(
        """
    You have 3 options:
    \t1. Login
    \t2. Create an Account
    \t3. Forgot Password?

    Which will you choose... 1, 2 or 3?!
    """
    )
