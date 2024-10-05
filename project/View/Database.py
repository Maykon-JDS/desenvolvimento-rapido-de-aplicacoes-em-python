import streamlit as st
from Database.Database import Database

database = Database()

database.cursor.execute("SELECT * FROM User")
# database.cursor.execute("DELETE FROM User WHERE 1 = 1")

# database.connection.commit()

rows = database.cursor.fetchall()

print(rows)

for row in rows:
    st.write(dict(row))
