import streamlit as st
import funcoes as fun

#add menu lateral
def itensSidebar():
    st.sidebar.title('Menu')
    select  = st.sidebar.selectbox(
    "Escolha uma opção para navegar",
    ("Leitura dos dados", "Formatando as colunas categoricas", "Train Test Split")   
)
    #LEITURA DOS DADOS
    if(select == 'Leitura dos dados'):
        st.subheader('Leitura dos dados')  
        option = st.selectbox(
        'Selecione o formato de arquivo que deseja realizar o upload',
        ('xls', 'csv',))
        #VERIFICAÇÕES COM ARQUIVOS XLS E CSV
        fun.documentos(option)
        
    #FORMATANDO AS COLUNAS CATEGORICAS   
    if(select == 'Formatando as colunas categoricas'):
        st.subheader('Formatando as colunas categoricas') 
    
    #TRAIN TEST SPLIT    
    if(select == 'Train Test Split'):
        st.subheader('Train Test Split') 
    
         
       
      

