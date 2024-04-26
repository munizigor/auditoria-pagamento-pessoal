def pessoal_query(end):
    """
    Gera uma consulta SQL para obter dados relevantes do sistema de pessoal até a data especificada.

    Parâmetros:
    - end (str): A data de término para a análise. Define a última data de promoção a ser considerada.

    Retorno:
    - str: Uma consulta SQL formatada para recuperar dados específicos do sistema GECOPE.
    """
    return f"""
        SELECT cpf, nome, data_promocao, funcao FROM table WHERE data_promocao <= '{end}' ORDER BY cpf
    """

def dependentes_cols():
    return [
    "tipo_dependencia",
    "data_nascimento_dependente",
    "nome_dependente",
    "cpf_dependente",
    "cpf_titular",
    ]

# Seleção das colunas do sistema GEDEP que serão utilizadas na análise
def serv_voluntario_query(begin, end):
    """
    Gera uma consulta SQL para obter dados relevantes do sistema GSV até as datas especificadas.

    Parâmetros:
    - begin (str): A data de início para a análise.
    - end (str): A data de término para a análise.

    Retorno:
    - str: Uma consulta SQL formatada para recuperar dados específicos do sistema GSV.
    """
    return f"""
SELECT 
    *
FROM 
    table
"""