import streamlit as st

def is_authenticated():
    
    if 'is_logged_in' in st.session_state:
        return st.session_state.is_logged_in
    else:
        return False
    # 如果已登录，返回True；否则返回False

# 如果用户已登录，显示页面
if is_authenticated():
    # st.write(f"欢迎登陆！")
    pass

# 如果用户未登录，显示登陆界面
else:
    # 显示登陆表单
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")
    if st.button("登陆"):
        # 在这里编写验证用户名和密码的代码
        # 如果验证通过，将用户标记为已登录
        if username == "abc" and password == "abc":
            st.session_state.is_logged_in = True
            
            st.write("登陆成功！")
            if is_authenticated():
                st.session_state.show_login_form = False  
                st.write(f"欢迎登陆！")
           
        else:
            st.write("用户名或密码错误，请重试。")

