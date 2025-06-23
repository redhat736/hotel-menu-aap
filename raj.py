import streamlit as st
import os

# ------------------ USERS ------------------
users = {
    "admin": "admin123",
    "rahul": "1234",
    "chef": "cookme"
}

# ------------------ FOOD MENU ------------------
menu_items = [
    {"name": "Pizza", "price": 299, "image": "menu_images/pizza.jpg"},
    {"name": "Burger", "price": 149, "image": "menu_images/burger.jpg"},
    {"name": "Pasta", "price": 199, "image": "menu_images/pasta.jpg"},
    {"name": "Biryani", "price": 249, "image": "menu_images/biryani.jpg"},
    {"name": "Ice Cream", "price": 99, "image": "menu_images/icecream.jpg"},
    {"name": "Cold Drink", "price": 49, "image": "menu_images/colddrink.jpg"}
]

# ------------------ SESSION ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.cart = []
    st.session_state.address = ""

# ------------------ LOGIN PAGE ------------------
def login():
    st.title("🔐 Login to Hotel Menu")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

# ------------------ LOGOUT ------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.cart = []
    st.session_state.address = ""
    st.experimental_rerun()

# ------------------ MAIN MENU ------------------
def main_menu():
    st.set_page_config(page_title="🍽️ Hotel Menu", layout="wide")
    st.sidebar.title("👤 Welcome")
    st.sidebar.write(f"Logged in as: `{st.session_state.username}`")
    if st.sidebar.button("Logout"):
        logout()

    st.markdown("<h1 style='text-align: center;'>🍴 Our Menu</h1>", unsafe_allow_html=True)
    search = st.text_input("🔍 Search food items")

    filtered = [item for item in menu_items if search.lower() in item["name"].lower()]
    cols = st.columns(3)

    for i, item in enumerate(filtered):
        with cols[i % 3]:
            if os.path.exists(item["image"]):
                st.image(item["image"], use_column_width=True)
            st.subheader(item["name"])
            st.write(f"💰 ₹{item['price']}")
            if st.button(f"Add to Cart - ₹{item['price']}", key=f"add_{i}"):
                st.session_state.cart.append(item)
                st.success(f"✅ Added {item['name']} to cart")

    st.markdown("---")
    st.markdown("### 🛒 Your Cart")

    if not st.session_state.cart:
        st.info("Cart is empty.")
    else:
        total = 0
        for item in st.session_state.cart:
            st.write(f"- {item['name']} — ₹{item['price']}")
            total += item["price"]
        st.success(f"🧾 Total: ₹{total}")

        st.markdown("### 📬 Delivery Details")
        address = st.text_area("Enter your delivery address")
        if st.button("Place Order"):
            if address.strip() == "":
                st.warning("⚠️ Please enter your delivery address before placing the order.")
            else:
                st.session_state.address = address
                show_order_summary(total)

# ------------------ ORDER SUMMARY ------------------
def show_order_summary(total):
    st.markdown("## ✅ Order Confirmed!")
    st.balloons()
    st.markdown("Thank you for your order. Here are your order details:")
    
    for item in st.session_state.cart:
        st.write(f"- {item['name']} — ₹{item['price']}")
    
    st.success(f"🧾 Total Amount Paid: ₹{total}")
    st.markdown(f"📦 Your order will be delivered to:\n\n**{st.session_state.address}**")

    # Clear cart after order
    st.session_state.cart = []
    st.session_state.address = ""

# ------------------ RUN APP ------------------
if not st.session_state.logged_in:
    login()
else:
    main_menu()
