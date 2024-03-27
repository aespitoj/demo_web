# #Learning-Input Data into the website
import streamlit as st
import pandas as pd
name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
adr = st.text_area("Enter Your Text : ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,6))


button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    address : {adr}
    class : {classdata}""")



# #Learning-show csv file in website
# import streamlit as st
# import pandas as pd
#
# dataset = pd.read_csv("YearWiseRecordCount.csv")
# st.dataframe(dataset)


#Learning-Build Basic Website
# import   streamlit as st
#
# st.title("Welcome to kshh tech")
# st.header("Python")
# st.subheader("Java")
# st.markdown("I love python")
# st.code("""for i in range(1,5,1):
#                 print("Hello")
# """)