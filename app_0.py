import streamlit as str

str.title("Hello, Streamlit!")

str.title("_This_ is :blue[a title] text :speech_balloon:")

str.title('$E = mc^2$')

str.header('This is a header')

str.subheader('This is a subheader')

str.text('This is a text element')  

str.markdown('# This is \n a **markdown** \n -element')

str.write('This is a write element')

data = { "Name": "Alice", "age": 30, "Occupation": "Engineer" }

str.write(data)






with str.chat_message("AI"):
    str.write("Hello, how can I help you?")

prompt = str.chat_input("Type your message here...", max_chars=100)
if prompt:
        with str.chat_message("user"):
            str.write(f"User message: {prompt}")





