import streamlit as st

def check_credentials(username, password):
    # Hardcoded username and password for demonstration
    valid_username = "admin"
    valid_password = "password123"
    return username == valid_username and password == valid_password
def reset_inputs():
    st.session_state['username'] = ''
    st.session_state['password'] = ''

def main():
    st.title("Simple Login Page")
    
    # Input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if check_credentials(username, password):
            st.success("Login Successful! Welcome " + username + "!")
        else:
            st.error("Invalid Username or Password")
    st.button("Reset", on_click=reset_inputs)

if __name__ == "__main__":
    main()
