import streamlit as st
from backend import generate

# creating session state variables

if "API_KEY" not in st.session_state:
    st.session_state["API_KEY"] = ""

st.markdown(
    """
    <style>
    /* Target the button using attribute selector */
    button[kind="secondary"] {
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 12px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    button[kind="secondary"]:hover {
        background-color: white;
        color: red;
        
    }
    </style>
""",
    unsafe_allow_html=True,
)

# UI here
st.title("🎬 YouTube Script Writing Tool ")
st.write(
    "Welcome to the YouTube Script Writing Tool! This tool will help you generate a script for your YouTube video based on your input.")

topic = st.text_input("please provide your video's topic.", placeholder = 'e.g. LangChain')
video_length = st.text_input("Epected video length in minutes.", placeholder = 'e.g. 1 ')
creativity = st.slider("creativity and word limit", 0.0, 1.0, 0.5)

# sidebar
st.sidebar.header("YouTube")
st.sidebar.subheader("🔐 API Key")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if api_key:
    st.session_state["API_KEY"] = api_key

st.sidebar.image("youtube-logo-png-31812.png", width=200, use_container_width=True)
submit = st.button(
    "✨ Generate Script", key="generate_script", help="Click to generate the script"
)

if submit:
    if st.session_state["API_KEY"]:
        video_length = int(video_length)
        with st.spinner("Brewing your script like a chai pro... ☕"):
            search_result, title, script = generate(
                topic=topic,
                video_length=video_length,
                creativity=creativity,
                api_key=st.session_state["API_KEY"]
            )

        st.success("Script generated successfully! 🎉")
        st.subheader("🎬Title")
        st.write(title["text"])
        st.subheader("📝Script")
        st.write(script)

        # Display search engine results
        st.subheader("Check Out - DuckDuckGo search:")
        with st.expander("show me"):
            st.info(search_result) 
    else:
        st.warning("Please provide API key first.")
