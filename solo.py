import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("Expense tracker")
st.write("You can track your expenses here")
st.set_page_config(  layout="wide" )
FILE="expenses.csv"
def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    else:
        return pd.DataFrame(columns=["Data","Category","Amount"])  
df=load_data()
st.subheader("Add your expenses")   
tab1,tab2,tab3,tab4=st.tabs(["💰Add Expenses"," 🔘Category"," 📝Note"," 📅Date"])
with tab1:
    amount=st.number_input("Enter the amount",min_value=0.0,step=10.0)

with tab2:
    category=st.selectbox("select the category",["Food","Travel","Entertainment","Health","Shopping","Education","Electricity bills","Others"])

with tab3:
    note=st.text_area("Add a note",max_chars=100)

with tab4:
     data=st.date_input("Select a date")
if st.button("➕Add Expenses",use_container_width=True):

    new_data=pd.DataFrame({"Data":[data],"Category":[category],"Amount":[amount],"Note":[note]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE, index=False)


    st.success("✅Expense added successfully")
    st.rerun()

st.divider()
st.header("Expense History")
total_expenses=df["Amount"].sum()
col1,col2=st.columns(2)

with col1:
    st.metric("💰TotalExpenses",f"₹{total_expenses:,.2f}")

    with col2:
        st.metric("🧾Number of Expenses",len(df))

st.subheader("Expenses by Catagory")
if not df.empty:
    st.write(df.columns.tolist())
    Category_data=df.groupby("Category")["Amount"].sum()
    st.bar_chart(Category_data)
else:
    st.info("No expenses added yet.")

st.subheader("📋Expenses by Data")
st.dataframe(df,use_container_width=True)



                                         









    

  
