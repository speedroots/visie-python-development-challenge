#!/usr/bin/python3

# External Resources

# Internal Resources

from .listar_todos_colaboradores import listar_todos_colaboradores
#from .localizar_um_colaborador import localizar_um_colaborador
from .atualizar_colaborador import atualizar_colaborador
from .deletar_colaborador import deletar_colaborador
from .registrar_colaborador import adicionar_colaborador

from UTILS import function_init_alert_loaded_status

function_init_alert_loaded_status(__name__)