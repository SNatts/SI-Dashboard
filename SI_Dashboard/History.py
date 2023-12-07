import streamlit as st

c1, c2, c3 = st.columns((6, 1, 1))
History = '<p style="font-family:sans-serif; font-size: 30px; font-weight: bold;">History</p>'
c1.markdown(History, unsafe_allow_html=True)
c2.button("Back", use_container_width=True)


cols   = st.columns((2, 2, 3, 1))
fields = ["Date", "Order ID", "User", "Status"]

for col, field in zip(cols, fields):
	col.write("**"+field+"**")
data1 = ['05-12-2024', '2024000001', 'Marry', ":green[Success]"]
for col, data in zip(cols, data1):
	col.write(data)
data2 = ['05-12-2024', '2024000002', 'John', ":red[Cancel]"]
for col, data in zip(cols, data2):
	col.write(data)
data3 = ['05-12-2024', '2024000003', 'John', ":green[Success]"]
for col, data in zip(cols, data3):
	col.write(data)
data4 = ['06-12-2024', '2024000004', 'Edwin', ":green[Success]"]
for col, data in zip(cols, data4):
	col.write(data)
data5 = ['06-12-2024', '2024000005', 'Ann', ":green[Success]"]
for col, data in zip(cols, data5):
	col.write(data)
data6 = ['06-12-2024', '2024000006', 'James', ":orange[Sending]"]
for col, data in zip(cols, data6):
	col.write(data)
data7 = ['07-12-2024', '2024000007', 'Miko', ":orange[Sending]"]
for col, data in zip(cols, data7):
	col.write(data)
data8 = ['07-12-2024', '2024000008', 'Adam', ":orange[Sending]"]
for col, data in zip(cols, data8):
	col.write(data)
data9 = ['08-12-2024', '2024000009', 'Wong', ":blue[Packing]"]
for col, data in zip(cols, data9):
	col.write(data)
data10 = ['08-12-2024', '2024000010', 'Pearl', ":blue[Packing]"]
for col, data in zip(cols, data10):
	col.write(data)