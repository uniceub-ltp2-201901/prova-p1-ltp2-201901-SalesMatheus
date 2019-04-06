# Função validar login
def get_idprofessor(cursor):
    # Executar o sql
    cursor.execute(f'select  nome from faculdade.professor')

    # Recuperando o retorno do BD
    idprofessor = cursor.fetchall()

    # Fechar o cursor
    cursor.close()

    print(idprofessor)
    # Retornar o idlogin
    return idprofessor


