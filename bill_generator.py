# bill_generator.py
import streamlit as st

st.set_page_config(page_title="Simple Bill Generator", page_icon="🧾")

st.title("🧾 Simple Bill Generator")

# Input section
st.header("Enter Item Details")

items = []
total_amount = 0

# Number of items
num_items = st.number_input("How many items do you want to add?", min_value=1, max_value=20, step=1)

for i in range(int(num_items)):
    st.subheader(f"Item {i+1}")
    name = st.text_input(f"Enter name of item {i+1}", key=f"name_{i}")
    qty = st.number_input(f"Enter quantity of {name if name else 'item'}", min_value=0, step=1, key=f"qty_{i}")
    price = st.number_input(f"Enter price per unit of {name if name else 'item'}", min_value=0.0, step=0.5, key=f"price_{i}")
    
    amount = qty * price
    if name:
        items.append((name, qty, price, amount))
    total_amount += amount

# Bill Display
st.header("Generated Bill")

if items:
    st.write("### Itemized Bill")
    for item in items:
        st.write(f"**{item[0]}** - Qty: {item[1]}, Price: ₹{item[2]}, Amount: ₹{item[3]}")
    
    st.subheader(f"💰 Total Bill Amount: ₹{total_amount}")

    if st.button("Generate Receipt"):
        st.success("Receipt Generated!")
        st.write("### Receipt")
        for item in items:
            st.write(f"{item[0]} ({item[1]} x ₹{item[2]}) = ₹{item[3]}")
        st.write(f"**Total: ₹{total_amount}**")
else:
    st.info("Please enter item details above to generate a bill.")

