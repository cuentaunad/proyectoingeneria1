import streamlit as st

from reg_usr import reg_usr
from reg_mer import reg_mer
from con_mer import con_mer
from gen_rep import gen_rep

st.title("Sistema de control de mercancias")


module_flag = st.sidebar.selectbox(
    "Selección de modulo",
    ("Registro de usuarios", "Registro de mercancía", "Consulta de mercancía", "Generación de reporte")
)


if module_flag == "Registro de usuarios":
    reg_usr()

elif module_flag == "Registro de mercancía":
    reg_mer()
elif module_flag == "Consulta de mercancía":
    con_mer()
    
elif module_flag == "Generación de reporte":
    gen_rep()
    
else :
    st.subheader("Modulo en progreso")