import random
import gradio as gr
def FriendshipCal(name1,name2):
    fs=random.randint(0,100)
    if (fs > 80):
        status = 'Best Friends Forever'
    elif (fs < 40):
        status = 'Just Friends'
    else:
        status = 'Friends Forever'
    return f'The Friendship Score is {fs}%', status

iface=gr.Interface(
    fn=FriendshipCal,
    inputs=[gr.Text(label='Enter 1st Name'), gr.Text(label='Enter 2nd Name')],
    outputs=[gr.Text(label='Friendship Score'), gr.Text(label='Friendship Status')],
    title='Friendship Calculator'
)

iface.launch()
