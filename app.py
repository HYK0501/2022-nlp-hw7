from multiprocessing.sharedctypes import Value
import streamlit as st
import  spell as sp
st.title('spell !')

show_orginal = st.checkbox("show original word")
option = st.selectbox( "pick a sample text : " , [ 'speling' , 'korrectud' , 'bycycle' , 'word' , 'apple' , 'lamon' , 'language' , 'hapy' , 'ridiculous'] )
word = st.text_input( label="your word " , value=option) 
#submit = form.form_submit_button("submit")
#if submit:
correct_word = sp.correction( word )
if show_orginal :
    st.write( f'original word :  {word}')
if word == correct_word:
    st.markdown("""
    <p style = "   background-color: lime;color: white ;height: 30px;opacity: .5;"> this word is correct ! </p>
    """ , unsafe_allow_html=True)
       
else:
    st.markdown("""
    <p style = "   background-color: red;color: white ;height: 30px;opacity: .5;" > """
    + f'this word is wrong , the correct word is {correct_word}' + """ </p>
    """ , unsafe_allow_html=True)