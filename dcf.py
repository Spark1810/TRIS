import streamlit as st

st.title("TRIS")
st.subheader("Your Virtual Ally in Every Endeavor")

def translate_text():
    # You can add your translation logic here
    translated_text = "Translated text goes here"
    st.warning(f"Translated Text: {translated_text}")

def translate_text2():
    # You can add your translation logic here
    translated_text = "Your Summarized text goes here"
    st.warning(f"Summarized Text: {translated_text}")

def translate_text3():
    # You can add your translation logic here
    translated_text = "Elaborated text goes here"
    st.warning(f"Elaborated Text: {translated_text}")


def svb():
    from annotated_text import annotated_text
    st.subheader("Proof Reading - Your Gramatical Synthesiser")
    annotated_text(
        "This ",
        ("is", "verb"),
        " some ",
        ("annotated", "adj"),
        ("text", "noun"),
        " for those of ",
        ("you", "pronoun"),
        " who ",
        ("like", "verb"),
        " this sort of ",
        ("thing", "noun"),
        "."
    )

activities = ["Introduction", "Chat"]
choice = st.sidebar.selectbox("Select Activities", activities)
st.markdown(
        "")

if choice == 'Introduction':
    st.markdown(
        "")
    st.subheader("Facilitating Offline text enhancer with AI-precised Summarizer and Grammar Corrector ")
    st.info("This idea initially focus on creating a standalone LLM application which summarizes text, science and tech documents in network not connected to internet. The system also concise newspaper articles and performs reformatting and grammar checks. ")

elif choice=='Chat':
    user_input = st.text_input("Enter your text :")
    st.markdown("")
    if st.sidebar.button("Translate"):
        translate_text()
    
    if st.sidebar.button("Summarize"):
        translate_text2()
    if st.sidebar.button("Proof Reader"):
        svb()
    if st.sidebar.button("Expander"):
        translate_text3()
