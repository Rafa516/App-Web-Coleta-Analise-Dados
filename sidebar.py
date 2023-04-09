import streamlit as st
import funcoes as fun

#add menu lateral
def itensSidebar():
    st.sidebar.title('Menu')
    select  = st.sidebar.selectbox(
    "Escolha uma opção para navegar",
    ("Leitura dos dados", "Formatando as colunas categoricas", "Train Test Split")   
)
    option = st.selectbox(
    'Selecione o formato de arquivo que deseja realizar o upload', 
    ('xls', 'csv', 'Link Google Drive (CSV)'))    
    #LEITURA DOS DADOS
    if(select == 'Leitura dos dados'):
        st.subheader('Leitura dos dados')  
        if(option == 'Link Google Drive (CSV)'):
         link = st.text_input('Digite ou cole o link')
         if(link != ''):
          fun.documentoLink(link)
        #VERIFICAÇÕES COM ARQUIVOS XLS E CSV
        else:
          fun.documentosLeitura(option)
        
    #FORMATANDO AS COLUNAS CATEGORICAS   
    if(select == 'Formatando as colunas categoricas'):
        st.subheader('Formatando as colunas categoricas')
        if(option == 'Link Google Drive (CSV)'):
         link = st.text_input('Digite ou cole o link')
         if(link != ''):
          fun.documentoLinkColunasCategoricas(link) 
        else:
          fun.documentosColunastegoricas(option)
    
    #TRAIN TEST SPLIT    
    if(select == 'Train Test Split'):
        st.subheader('Train Test Split') 
    
         
       
      

