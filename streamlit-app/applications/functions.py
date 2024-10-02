import streamlit as st
from applications import db
import requests

def client_ip():
    """
    Get the client's IP address.
    """
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip = response.json().get('ip')
            return ip
        else:
            return None
    except Exception:
        return None

def check_and_update_ip(email):
    """
    Check if the client's IP is in the user's document.
    """
    ip = client_ip()
    if not ip:
        return False
    try:
        user_ref = db.collection('users').document(email)
        user_doc = user_ref.get()
        user_data = user_doc.to_dict()
        if user_data is not None:
            ip_list = user_data.get('ips', [])
            if ip not in ip_list:
                ip_list.append(ip)
                user_ref.update({'ips': ip_list})
        else:
            st.error("User not found. Redirecting to sign-in.")
            st.markdown("""
                <meta http-equiv="refresh" content="0; url=http://localhost:3000/signin/">""", #TODO: switch this URL out
                unsafe_allow_html=True)
            st.stop()
    except Exception:
        return False
    return True
