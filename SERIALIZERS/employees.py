#!/usr/bin/python3

# External Resources

# Internal Resources

def function_serializer_to_json(fieldnames, response):

    listData = []
    
    for employee in response:

        dictData = {}

        for index, value in enumerate(employee):

            dictData[fieldnames[index]] = value

        listData.append(dictData)

    return listData

def function_serializer_employee_params(employee):

    fieldnames = [
    'cpf',
    'data_admissao',
    'data_nascimento',
    'id_pessoa',
    'nome',
    'rg',
    ]

    dictData = {x: employee[x] for x in fieldnames if x in employee}

    [dictData.pop(key) for key in fieldnames if key in dictData.keys() \
    and dictData[key] == None]

    return dictData