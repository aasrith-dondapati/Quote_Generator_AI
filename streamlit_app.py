# streamlit_app.py
import streamlit as st
from quote_generator import generate_quote
from pdf_generator import generate_pdf

# Streamlit app
st.title("AI-Powered Quote Generator")

# User input
customer_name = st.text_input("Customer Name:")
customer_phone = st.text_input("Customer Phone:")
customer_address = st.text_input("Customer Address:")
service_request = st.text_input("Describe the service required:")

if st.button("Generate Quote"):
    # Generate the quote
    quote = generate_quote(customer_name, customer_phone, customer_address, service_request)
    
    # Display the quote
    st.write("Generated Quote:")
    st.write(quote)

    # Generate PDF
    total_price = 350  # Replace with dynamic calculation if needed
    generate_pdf(customer_name, customer_phone, customer_address, service_request, total_price)
    
    # Provide download link
    with open("quote.pdf", "rb") as f:
        st.download_button("Download Quote", f, file_name="quote.pdf")