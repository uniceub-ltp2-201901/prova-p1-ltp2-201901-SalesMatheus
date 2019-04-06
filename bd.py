# Função listar professor
def get_idprofessor(cursor):
    # Executar o sql
    cursor.execute(f'select  nome, idprofessor from faculdade.professor order by nome')

    # Recuperando o retorno do BD
    idprofessor = cursor.fetchall()

    # Fechar o cursor
    cursor.close()

    return idprofessor

# Função exibir professor
def get_detalhe(cursor, professor):
    # Executar o sql
    cursor.execute(f'select professor.Nome as professor, professor.DataNasc, professor.NomeMae, disciplina.nome, disciplina.curso, disciplina.cargahoraria from faculdade.professor, faculdade.disciplina where professor.idProfessor = disciplina.idprofessor and professor.idprofessor = {professor}')

    # Recuperando o retorno do BD
    detalhes = cursor.fetchall()

    # Fechar o cursor
    cursor.close()
    print(detalhes)
    return detalhes

