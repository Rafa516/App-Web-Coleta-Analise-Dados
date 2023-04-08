
import streamlit as st
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

#FUNÇÃO PARA VERIFICAÇÃO DOS ARQUIVOS
def documentos(tipo):     
    arquivos = st.file_uploader('Faça upload do arquivo '+ tipo, accept_multiple_files=True,type = tipo)  
    
    multiSelectKey = 0
    textInputKey = 50
    downloadButtonKey = 100
    
    for arquivo in arquivos: 
         multiSelectKey += 1
         textInputKey +=1
         downloadButtonKey +=1
         df = leitura(tipo,arquivo)           
         st.write('Verificações do arquivo',arquivo.name)
         #VERIFICANDO AS COLUNAS
         
         options = st.multiselect(
        'Escolha as colunas que deseja remover',
         df.columns,key = multiSelectKey)
         #REMOVENDO AS COLUNAS SELECIONADAS
         for col in options:
                if col in options:
                    df = df.drop(columns=[col])
                  
         st.dataframe(df)         
         st.write('Quantidade de dados nulos')
         nulos = df.isnull().sum()
         st.write(nulos)
         
         st.subheader('Realizar Download do arquivo '+arquivo.name +' atualizado') 
         nomeArquivo = st.text_input('Novo nome do Arquivo',key = textInputKey)
         df_xlsx = to_excel(df)       
         st.download_button(label='📥 Download do arquivo xls',
                                data=df_xlsx ,
                                file_name= nomeArquivo+'.xlsx',
                                key = downloadButtonKey )  
      
        
            
#FUNÇÃO PARA LEITURA DOS ARQUIVOS SELECIONADOS PELO TIPO
def leitura(tipo,arquivo):
    if(tipo == 'xls'):
        return pd.read_excel(arquivo)
    else:
        return pd.read_csv(arquivo) 
 
#FUNÇÃO PARA GERAR O BINARIO PARA DOWNLOAD DO ARQUIVO XLS
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data
 