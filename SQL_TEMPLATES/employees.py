#!/usr/bin/python3

# External Resources

# Internal Resources

class Employees(object):

    def function_select_all_from_employees():

        '''
        query = 
        SELECT 
        id_pessoa, 
        nome, 
        rg, 
        cpf, 
        DATE_FORMAT(data_nascimento, '%d/%m/%Y') AS data_nascimento, 
        DATE_FORMAT(data_admissao, '%d/%m/%Y') AS data_admissao, 
        funcao 
        FROM pessoas;
        ''' # Desconsiderado pois as datas serão serializadas em funções posteriores a consulta.

        query = '''
        SELECT 
        *
        FROM pessoas;
        '''

        return query

    def function_update_employee(data_admissao, id_pessoa):

        query = f"""
        UPDATE pessoas
        SET data_admissao=DATE('{data_admissao}')
        WHERE id_pessoa={id_pessoa};
        """

        return query

    def function_delete_employee(id_pessoa):

        query = f"""
        DELETE FROM pessoas
        WHERE 
        id_pessoa={id_pessoa};
        """

        return query

    def function_register_employee(employee):

        cpf = employee.cpf if type(employee) != dict else employee['cpf']
        data_admissao = employee.data_admissao if type(employee) != dict else employee['data_admissao']
        data_nascimento = employee.data_nascimento if type(employee) != dict else employee['data_nascimento']
        funcao = employee.funcao if type(employee) != dict else employee['funcao']
        nome = employee.nome if type(employee) != dict else employee['nome']
        rg = employee.rg if type(employee) != dict else employee['rg']

        query = f"""
            INSERT INTO pessoas (
                cpf,
                data_admissao,
                data_nascimento,
                funcao,
                nome,
                rg
            )

            SELECT
                '{cpf}',
                '{data_admissao}',
                '{data_nascimento}',
                '{funcao}',
                '{nome}',
                '{rg}'
            FROM DUAL
            WHERE NOT EXISTS
            (SELECT 1 from pessoas WHERE cpf='{cpf}' OR rg='{rg}');
        """

        return query

    def function_get_filtered_employee(employee):

        lookingFor = "".join(f"""{key} = '{employee[key]}' AND """ for key in employee)

        query = f'''SELECT * FROM pessoas WHERE {lookingFor};'''

        query = query.replace(" AND ;", ";")

        return query