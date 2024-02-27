import streamlit as st
#streamlit run test.py
st.title("hi")
st.write("test")

st.markdown("## my markdown")
code = '''def hello():
    print("Hello")''' 
st.code(code, language='python')

show_btn = st.button("Show code!")
if show_btn:
    st.code(code, language='python')

age_inp = st.number_input("Input your age")
st.markdown(f"Your age is {age_inp}")

st.markdown("# NLP Task")
text_inp = st.text_input("Input your text")
word_tokenize = "|".join(text_inp.split())
st.markdown(f"{text_inp}")
