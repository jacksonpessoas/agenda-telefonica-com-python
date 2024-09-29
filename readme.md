## Conversor de Planilha Excel para vCard (.vcf)

Este projeto converte uma planilha Excel contendo uma agenda telefônica em um arquivo de vCard (.vcf). O vCard é um formato padrão utilizado para armazenar informações de contatos, como nome, sobrenome (bairro) e número de telefone.

## Pré-requisitos

Certifique-se de ter o Python instalado e as seguintes bibliotecas:

- **pandas**: Para manipulação de dados em planilhas Excel.
- **vobject**: Para criação e manipulação de arquivos vCard (.vcf).

Para instalar as bibliotecas necessárias, execute:

```bash
pip install pandas vobject

```

## Funcionamento do Código

1. Carregamento da Planilha: O arquivo agenda_telefonica.xlsx é carregado, contendo os dados da agenda.

2. Filtragem de Dados: As colunas Nome, Bairro (usado como sobrenome), e Contato são filtradas.
3. Criação do vCard: Para cada linha da planilha, um vCard é criado e salvo no arquivo agenda_telefonica.vcf.
4. Campos Adicionados:
- Nome Completo
- Sobrenome (substituído pelo bairro da planilha)
- Telefone


## Exemplo da Planilha Excel

A planilha deve ter o seguinte formato, com as colunas `Nome`, `Bairro` e `Contato`:

| Nome       | Bairro            | Contato    |
|------------|-------------------|------------|
| João Silva | Centro            | 999999999  |
| Ana Souza  | Jardim das Flores  | 888888888  |
| Carlos Dias| Vila Nova         | 777777777  |



## Como Executar
1. Coloque a planilha agenda_telefonica.xlsx na mesma pasta que o script.

2. Execute o script Python:

```
python agenda.py
```

### Melhorias Futuras
- Suporte a múltiplos números de telefone por contato.
- Adição de mais campos no vCard, como endereço e email.

#### Observação: 
O campo Bairro na planilha foi utilizado como Sobrenome no vCard. Caso prefira separar esses campos, basta ajustar o código conforme sua necessidade.



#### TÓPICOS
["Funcionamento do Código"](##funcionamento-do-codigo), ["Exemplo da Planilha Excel"](##exemplo-da-planilha-excel), ["Como Executar"](##como-executar), ["Resultado"](##resultado), ["Código"](##código), e ["Melhorias Futuras"](##melhorias-futuras)


## Criado por

JacksonPessoaS 

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jacksonpessoas)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jackson-pessoa-soares)


Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato!