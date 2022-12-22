#!/usr/bin/python3

# External Resources

from fastapi.responses import HTMLResponse

# Internal Resources

from .head_content import function_head_content
from UTILS import function_gerenic_except_handler
from DATABASES import function_get_all_employees

def modalEditar():
	
	modalData = f'''
	<!-- MODAL EDITAR COLABORADOR -->
    <div id="modalEditEmployee" class="modal fade" role="dialog">
      <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">Editar Colaborador</h4>
            <button type="button" class="close" data-bs-dismiss="modal">&times;</button>
          </div>
          <div class="modal-body">

            <form role="form" id="modalEditEmployeeForm" method="POST"
             accept-charset="utf-8" action="/form/edit/employee" 
             data-form="modalEditEmployeeForm" 
             data-row-id-pessoa="" 
             data-row-data-admissao="" 
             >

            <div class="input_div">
              <div>
                <label for="">Data de Admissão: </label>
                <input type="date" name="data_admissao" id="data_admissao" required>
                <input type="hidden" name="id_pessoa" id="id_pessoa" value="">
              </div>
            </div>

          </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancelar</button>
            <button type="submit" form="modalEditEmployeeForm" class="btn btn-success" id="btnEditEmployee">Alterar</button>
          </div>
        </div>

      </div>
    </div> <!-- FIM DO MODAL MODAL EDITAR COLABORADOR -->
	'''

	return modalData

def modalRemover():
	
	modalData = f'''
	<!-- MODAL REMOVER COLABORADOR -->
    <div id="modalDeleteEmployee" class="modal fade" role="dialog">
      <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">Remover Colaborador</h4>
            <button type="button" class="close" data-bs-dismiss="modal">&times;</button>
          </div>
          <div class="modal-body">

            <form role="form" id="modalDeleteEmployeeForm" method="POST"
             accept-charset="utf-8" action="/form/delete/employee" 
             data-form="modalDeleteEmployeeForm" 
             data-row-id-pessoa="" 
             >

            <div class="input_div">
              <div>
                <input type="hidden" name="id_pessoa" id="id_pessoa" value="">
              </div>
              <div>
                <span> Tem certeza que deseja remover o colaborador?</span>
              </div>
            </div>

          </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancelar</button>
            <button type="submit" form="modalDeleteEmployeeForm" class="btn btn-success" id="btnEditEmployee">Confirmar</button>
          </div>
        </div>

      </div>
    </div> <!-- FIM DO MODAL MODAL REMOVER COLABORADOR -->
	'''

	return modalData

def td(employee):

	id_pessoa = employee['id_pessoa']
	data_admissao = employee['data_admissao']
	nome = employee['nome']

	buttonEditar = f'''
	<button type="button" class="btn-dark btnCallJS" 
	data-bs-toggle="modal" 
	data-bs-target="#modalEditEmployee" 
	data-row-id-pessoa="{id_pessoa}" 	
	>Editar</button>
	'''

	buttonRemover = f'''
	<button type="button" class="btn-dark btnCallJSDelete" 
	data-bs-toggle="modal" 
	data-bs-target="#modalDeleteEmployee" 
	data-row-id-pessoa="{id_pessoa}" 
	>Remover</button>
	'''

	htmlData = f'''<td>{nome}</td>'''
	htmlData += f'''<td>{data_admissao}</td>'''
	htmlData += f'''<td>{buttonEditar}</td>'''
	htmlData += f'''<td>{buttonRemover}</td>'''

	return htmlData

def tr():

	employees = function_get_all_employees()

	if type(employees) == dict and 'state' in employees.keys() and employees['state'] == False:

		htmlData = None

	else:

		htmlData = "".join(f'''<tr>{td(employee)}</tr>''' for employee in employees)

	return htmlData

def thead():

	htmlData = '''
	<thead class="thead-dark">
		<tr>
			<th colspan="" rowspan="" headers="" scope="col">Primeiro Nome</th>
			<th colspan="" rowspan="" headers="" scope="col">Data de Admissão</th>
			<th colspan="" rowspan="" headers="" scope="col"></th>
			<th colspan="" rowspan="" headers="" scope="col"></th>
		</tr>
	</thead>
	'''

	return htmlData

def tbody():

	htmlData = f'''
	<tbody>
		{tr()}
	</tbody>
	'''

	return htmlData

def table():

	htmlData = f'''
	<table class="table table-striped" name="employeeTable" id="employeeTable">
	{thead()}
	{tbody()}
	</table>
	'''

	return htmlData

def function_add_employee():

	cpfPattern = "\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}"
	rgPattern = "\\d{2}\\.\\d{3}\\.\\d{3}-\\d{1}"
	
	htmlData = f'''
	<div>
		<br>
		<br>
		<h2>Formulário Para Registro de um Novo Colaborador</h2>
	    <form name="formEmployee" id="formEmployee" method="post" action="/">
	      <div class="form-group">
	        <label for="cpf">CPF: *</label>
	        <input type="" class="form-control" name="cpf" id="cpf" placeholder="" 
	        pattern="{cpfPattern}" required>
	        <small id="cpf_format" class="form-text text-muted">Formato: xxx.xxx.xxx-xx</small>
	      </div>
	      <div class="form-group">
	        <label for="data_admissao">Data de Admissão: *</label>
	        <input type="date" class="form-control" name="data_admissao" id="data_admissao" placeholder="" required>
	      </div>
	      <div class="form-group">
	        <label for="data_nascimento">Data de Nascimento: *</label>
	        <input type="date" class="form-control" name="data_nascimento" id="data_nascimento" placeholder="" required>
	      </div>
	      <div class="form-group">
	        <label for="funcao">Função: </label>
	        <input type="" class="form-control" name="funcao" id="funcao" placeholder="Suporte, Vendas, Gestor..." >
	      </div>
	      <div class="form-group">
	        <label for="nome">Nome: *</label>
	        <input type="" class="form-control" name="nome" id="nome" placeholder="" required>
	      </div>
	      <div class="form-group">
	        <label for="rg">RG: *</label>
	        <input type="" class="form-control" name="rg" id="rg" placeholder=""
	        pattern="{rgPattern}" required>
	        <small id="rg_format" class="form-text text-muted">Formato: xx.xxx.xxx-x</small>
	      </div>
	      <div class="form-group">
	        <input type="submit" class="btn btn-primary" name="" id="submitButton" placeholder="">
	      </div>
	    </form>
  	</div>
  	<br>
  	<br>
	'''

	return htmlData

def function_script_pagination():

	htmlData = '''
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.js"></script>
	
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
	

	<script>

	$(function() {
    $(".btnCallJSDelete").on("click", function() {
        
        var id_pessoa = $(this).attr('data-row-id-pessoa');

        $("#id_pessoa").val(id_pessoa);

        var form = document.querySelector('form[data-form="modalDeleteEmployeeForm"]');

        form.setAttribute('data-row-id-pessoa', id_pessoa);

        var hiddenPessoa = form.querySelector('input[name="id_pessoa"]')

        hiddenPessoa.setAttribute('value', id_pessoa);

	    });
	});


	</script>

	<script>

	$(function() {
    $(".btnCallJS").on("click", function() {
        
        var id_pessoa = $(this).attr('data-row-id-pessoa');

        $("#id_pessoa").val(id_pessoa);

        var form = document.querySelector('form[data-form="modalEditEmployeeForm"]');

        form.setAttribute('data-row-id-pessoa', id_pessoa);

	    });
	});

	</script>
	'''

	return htmlData

def function_body():

	try:

		messageAlert = "<br><br><span><h2>Nenhum Colaborador registrado. Uma tabela será exibida após a inserção do primeiro registro.</h2></span>"



		htmlData = f'''
		<body>
			{modalEditar()}
			{modalRemover()}
		  <div>
		    {table() if tr() != None else messageAlert}
		  </div>
		  <div>
		    {function_add_employee()}
		  </div>
		  {function_script_pagination()}
		</body>
		'''

		return htmlData

	except Exception as Error:

		return function_gerenic_except_handler(__name__, 'function_body', Error)

def function_index_html_page():

    try:

        htmlData = f'''
        <!DOCTYPE html>
        <html class="no-js" lang="en-US">{function_head_content()}{function_body()}
        </html>
        '''

        return HTMLResponse(content= htmlData, status_code= 200)

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_index_html_page', Error)