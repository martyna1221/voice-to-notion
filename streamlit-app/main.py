import streamlit as st
# from applications.chatgpt import ask_chatgpt
from applications.database import get_user, create_user #create_firestore_document, update_firestore_document
from applications.functions import check_and_update_ip

def login():
    try:
        email = st.query_params.get("email", [None])
        if email is None:
            st.markdown("""
                <meta http-equiv="refresh" content="0; url=http://localhost:3000/signin">""", #TODO: switch this URL out
                unsafe_allow_html=True)
            st.stop()
        else:
            user = get_user(email)
            if user is None:
                create_user(email)
            check_and_update_ip(email)
        return email
    except Exception:
        st.markdown("""
            <meta http-equiv="refresh" content="0; url=http://localhost:3000/signin">""", #TODO: switch this URL out
            unsafe_allow_html=True)
        st.stop()

def main():
    st.set_page_config(layout='wide')
    if 'email' not in st.session_state:
        st.session_state.email = login()

    st.title('Inside main.py!')

    # TODO: uncomment the __init__.py file & the above imports

    # TODO: uncomment the line below, once you've added the ChatGPT API key to the .env file to test
    # quote = ask_chatgpt('Tell me a quote by Albert Camus.')
    # st.write("hi")

    # TODO: uncomment the line below, once you've added the service account JSON to the key.json file to test
    # doc_id = create_firestore_document('test', {'test': 'test'})
    # st.write(f'Created document with ID: {doc_id}')
    # update_firestore_document('test', doc_id, {'test': 'updated test'}) # print statements can be seen in the terminal

if __name__ == '__main__':
    main()
