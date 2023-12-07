import streamlit as st
import extra_streamlit_components as stx
import streamlit_nested_layout
import os 
import datetime
import shutil
from pathlib2 import Path 

st.set_page_config(layout="wide")

order_list = []
msg = ""
parent_dir = "D:/SI_Dashboard/Saved/"

img_dict = {'Blue': 'can_color\Blue.png','Gray': 'can_color\Gray.png','Green': 'can_color\Green.png','Red': 'can_color\Red.png','Yellow': 'can_color\Yellow.png'}
key_dict = {'can_color\Blue.png': 'Blue','can_color\Gray.png': 'Gray','can_color\Green.png': 'Green','can_color\Red.png': 'Red','can_color\Yellow.png': 'Yellow'}

key_list = list(img_dict.keys())
val_list = list(img_dict.values())

c1, c2, c3 = st.columns((8.2, 0.4, 0.4))
Home = '<p style="font-family:sans-serif; font-size: 50px; font-weight: bold;">Home</p>'
c1.markdown(Home, unsafe_allow_html=True)
# c2.button("Back")
c3.button("Back")

col1, col2 = st.columns((7,3))
with col1:
    # st.code("import extra_streamlit_components as stx")
    chosen_id = stx.tab_bar(data=[
        stx.TabBarItemData(id="tab1", title="4️⃣ 4 pcs.", description="minimal choice, full of yummy."),
        stx.TabBarItemData(id="tab2", title="6️⃣ 6 pcs.", description="extra pack, extra delicious.")])

    placeholder = st.container()

with col2:
   st.header("Select your Option 🎯")
   if chosen_id == "tab1":
        option4p1 = st.selectbox(
            'First Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='4pcs_1')
        option4p2 = st.selectbox(
            'Second Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='4pcs_2')
        option4p3 = st.selectbox(
            'Third Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='4pcs_3')
        option4p4 = st.selectbox(
            'Fourth Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='4pcs_4')
        
   if chosen_id == "tab2":
        option6p1 = st.selectbox(
            'First Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='6pcs_1')
        option6p2 = st.selectbox(
            'Second Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='6pcs_2')
        option6p3 = st.selectbox(
            'Third Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='6pcs_3')
        option6p4 = st.selectbox(
            'Fourth Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='6pcs_4')
        option6p5 = st.selectbox(
            'Fifth Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='6pcs_5')
        option6p6 = st.selectbox(
            'Sixth Item',
            ('Red', 'Green', 'Blue', 'Yellow', 'Gray'),
            key='6pcs_6')

with col1:
    if chosen_id == "tab1":
        placeholder.markdown(f"## Welcome to `{chosen_id}`")
        colL, colM, colR = st.columns((3.25,3.5,3.25))
        with colM:
            colA, colB = st.columns((5,5))
            colC, colD = st.columns((5,5))
            with colA:
                st.image(img_dict[option4p1])
            with colB:
                st.image(img_dict[option4p2])
            with colC:
                st.image(img_dict[option4p3])
            with colD:
                st.image(img_dict[option4p4])
            order_list = [f"\tVac1_{key_dict[img_dict[option4p3]]}\n", f"\t\tVac2_{key_dict[img_dict[option4p1]]}\n", "\t\tGo_Position_1\n",
                          f"\t\tVac1_{key_dict[img_dict[option4p2]]}\n", f"\t\tVac1_{key_dict[img_dict[option4p4]]}\n", "\t\tGo_Position_2"]


    elif chosen_id == "tab2":
        placeholder.markdown(f"## Hello, this is `{chosen_id}`")
        colL, colM, colR = st.columns((2.5,5,2.5))
        with colM:
            colA, colB, colC = st.columns(3)
            colD, colE, colF = st.columns(3)
            with colA:
                st.image(img_dict[option6p1])
            with colB:
                st.image(img_dict[option6p2])
            with colC:
                st.image(img_dict[option6p3])
            with colD:
                st.image(img_dict[option6p4])
            with colE:
                st.image(img_dict[option6p5])
            with colF:
                st.image(img_dict[option6p6])
            order_list = [f"\tVac1_{key_dict[img_dict[option6p4]]}\n", f"\t\tVac2_{key_dict[img_dict[option6p1]]}\n", "\t\tGo_Position_1\n",
                          f"\t\tVac1_{key_dict[img_dict[option6p5]]}\n", f"\t\tVac1_{key_dict[img_dict[option6p2]]}\n", "\t\tGo_Position_2\n",
                          f"\t\tVac1_{key_dict[img_dict[option6p6]]}\n", f"\t\tVac1_{key_dict[img_dict[option6p3]]}\n", "\t\tGo_Position_3"]
    else:
        placeholder.markdown("## Choose one of our product choices")

cF1, cF2, cF3 = st.columns((8.2, 0.4, 0.4))
order_cmd = cF3.button("Order")
st.code(order_list)


if order_cmd:
    target_dir = parent_dir+'{date:%Y-%m-%d_%H-%M-%S%z}'.format( date=datetime.datetime.now())
    os.mkdir(target_dir)
    shutil.copyfile("template.txt", "message.txt")
    msg = msg.join(order_list)
    st.code(msg)
    file = Path(r"message.txt")
    data = file.read_text()
    data = data.replace("$REPLACE HERE$", msg)
    file.write_text(data)
    shutil.copyfile("message.txt", target_dir+'/'+"message.txt")
