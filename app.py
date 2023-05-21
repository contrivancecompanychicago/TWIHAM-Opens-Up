# Import dependencies
import gradio as gr


"""class ChatWrapper:

    def __call__(
        self, inp: str, history: str, chain
    ):
        Execute the chat functionality.           
        output = chain({"question": inp, "chat_history": history})["answer"]        
        history.append((inp, output))     
        return history, history


chat = ChatWrapper()"""

chatbot = gr.Chatbot()

block = gr.Blocks(css=".gradio-container {background-color: lightblue}")

with block:
    gr.HTML("<center><h2>Omdena AI Chatbot For Mental Health and Well Being</h2></center>")
    
    gr.HTML("WELCOME<br>"
            "I am an AI ChatBot and I am here to assist you with whatever is bothering you."
            "Our conversation is strictly confidential and I will not remember it when you come back another time."     
        )
        
    with gr.Row():
        message = gr.Textbox(
            label="What would you like to talk about?",
        )

    with gr.Row():
        submit = gr.Button(color="lightblue", value="Send", variant="secondary").style(full_width=False)

    gr.Examples(
        examples=[
            "I am lonely",
            "I'm having problems at home",
            "I am jumpy when I hear a loud noise and I feel scared all the time",
                 ],
        inputs=message,
    )


#   submit.click(chat, inputs=[message], outputs=[chatbot])
   
block.launch(debug=True)