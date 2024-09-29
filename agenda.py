import pandas as pd
import vobject

# Carregar a planilha Excel
arquivo_excel = 'agenda_telefonica.xlsx'
planilha = pd.read_excel(arquivo_excel)

# Filtrar as colunas de Nome, Sobrenome e Contato
agenda = planilha[['Nome', 'Sobrenome', 'Contato']]  

# Criar um arquivo vCard (.vcf)
with open('agenda_telefonica.vcf', 'w') as vcf_file:
    for _, row in agenda.iterrows():
        vcard = vobject.vCard()
        
        # Nome completo e sobrenome
        nome_completo = row['Nome']
        sobrenome = row['Sobrenome']  # Substituindo 'Bairro' por 'Sobrenome'
        vcard.add('n').value = vobject.vcard.Name(family=sobrenome, given=nome_completo)
        
        # Campo 'FN' (nome completo obrigatório)
        vcard.add('fn').value = f"{nome_completo} {sobrenome}"

        # Telefone
        vcard.add('tel').value = str(row['Contato'])

        vcf_file.write(vcard.serialize())

print("Arquivo VCF criado com sucesso!")
