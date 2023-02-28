import streamlit as st
import pandas as pd
import numpy as np

#
st.write("<h1>Scribe</h1>", unsafe_allow_html=True)

#
df = pd.DataFrame(
   columns=["automated step", "expected result", "actual result"]
)

#
tb = st.table(df)
data = ["open chrome", "success", "success"]
row = pd.DataFrame(index=1, data=data)
tb.add_rows(row)

# st.write("hello world")
# st.slider("sadadsdasd")

# st.button("edit", type="primary")
# st.button("d", type="secondary")

# mytable = st.table()
# columns = {"sdas""0"}
# mytable.columns(columns)

# data = {"open chrome", "success"}
# mytable.add_rows(data)


# st.code("""
#     import streamlit as st
#     st.write("hello world")
#     st.slider("sadadsdasd")
#     st.code("")
#     container = st.container()
#     container.success("success")
#     container.warning("warning")
#     container.error("error")
#     print("finished")
# """)

# container = st.container()
# container.success("success")
# container.warning("warning")
# container.error("error")

print("finished")