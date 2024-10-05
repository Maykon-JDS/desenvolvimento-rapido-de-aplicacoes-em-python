import streamlit as st
from Model.UserModel import User

class UserController:

    @staticmethod
    def signUp():

        try:

            user = User(st.session_state.name, st.session_state.username, st.session_state.password, st.session_state.email)

            valid = user.validateUser(["all"], {"confirmPassword": st.session_state.confirmPassword})

            if (valid):

                response = user.create()

                if (response):

                    st.session_state.respose.update(status="ok", messages="User created successfully!")

        except Exception as errors:

            st.session_state.respose.update(status="error", messages= errors.args[0])
