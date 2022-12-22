#!/usr/bin/python3

# External Resources

# Internal Resources

from UTILS import function_gerenic_except_handler

def function_description():

    try:

        desc = f"""
        Descrição do Projeto:

        - Tecnologias:

          - Python 3.9.5
          - FastAPI 0.75.1
          - Uvicorn 0.17.6
          - Bootstrap 5.2.3
          - JQuery 3.6.0
          - MySQL 8.0

        - Recursos Disponíveis:

          - Listagem de Colaboradores Registrados em Base de Dados Relacional
          - Criação de Colaboradores e Armazenamento do Registro em Base de Dados Relacional
          - Remoção do Registro de Colaboradores Armazenados em Base de Dados Relacional
          - Atualização Parcial do Registro de Colaboradores Armazenados em Base de Dados Relacional
          
        - Considerações:

          - As funcionalidades relacionadas como Recursos Disponíveis, estão habilitadas via interface web e via API.


        - Template de Dados Utilizados Durante a Fase de Desenvolvimento(Disponibilizado pela Visie):

            CREATE TABLE pessoas(
              `id_pessoa` TINYINT(255) NOT NULL AUTO_INCREMENT,
              `nome` CHAR(100) NOT NULL,
              `rg` CHAR(100) NOT NULL,
              `cpf` CHAR(100) NOT NULL,
              `data_nascimento` DATE NOT NULL,
              `data_admissao` DATE NOT NULL,
              `funcao` CHAR(100) NULL,
            PRIMARY KEY (`id_pessoa`));
                         
            INSERT INTO pessoas(`nome`,`rg`,`cpf`,`data_nascimento`,`data_admissao`) VALUES
            ('Alberto Vieira','25.507.105-2','168.637.122-53','1997-07-01','2020-09-28'),
            ('Alexandre Teixeira','79.474.888-8','877.733.889-89','1982-08-16','2020-05-15'),
            ('Ana Carolina Souza','52.565.667-8','766.370.920-96','1982-03-19','2016-08-19'),
            ('Ana Paula Soares','54.744.331-9','746.917.734-52','1984-09-01','2019-08-25'),
            ('Antônio Siqueira','81.669.888-5','695.991.412-45','1990-07-26','2016-05-18'),
            ('Arthur Silva','43.204.402-9','345.898.157-88','1996-12-30','2016-04-28'),
            ('Bárbara Santos','57.106.623-3','587.914.225-66','2000-09-04','2018-11-17'),
            ('Beatriz Santana','70.855.305-2','093.084.203-04','1994-05-17','2018-03-05'),
            ('Caio Sampaio','14.475.327-9','483.764.953-05','1995-11-18','2020-06-03'),
            ('Carla Rodrigues','62.692.082-5','566.412.961-13','1996-08-04','2015-03-31'),
            ('Carlos Rocha','23.782.125-5','053.166.034-60','1983-07-07','2017-03-08'),
            ('Cauê Ribeiro','33.548.790-1','491.145.149-15','1981-01-27','2020-12-31'),
            ('Cláudia Reis','54.435.082-9','511.020.782-80','1986-08-04','2020-09-25'),
            ('Cláudio Ramos','41.432.308-6','673.452.026-90','1982-08-12','2019-11-01'),
            ('Daiane Pereira','90.815.741-8','704.352.424-58','2002-11-22','2017-06-15'),
            ('Diego Penha','43.099.953-1','329.630.074-00','1983-02-23','2017-12-01'),
            ('Eduardo Oliveira','46.249.609-1','772.220.114-80','2001-02-12','2020-05-10'),
            ('Eliana Nunes','84.269.396-7','130.491.959-59','1994-07-03','2018-01-16'),
            ('Enzo Nascimento','68.986.227-4','356.759.355-25','1989-05-05','2016-08-23'),
            ('Fabiana Moura','69.437.526-9','149.992.262-00','1995-08-21','2019-03-26');

        - Objetivos Atingidos:

          - Págima HTML: Ok
          - Comandos CRUD: Ok
          - Listar Pessoas: Ok
          - Formatação dos Dados: Ok
          - Serialização da Data para Formato Brasileiro: Ok
          - Botões de Edição e Exclusão: Ok
          - Formulário de Criação Abaixo da Lista: Ok
          - paginação da Tabela: Removido(DataTables) por Interferência nas Ações de Edição e Remoção de Assinantes, quando navegado para outras páginas que não fosse a primeira.
          - APIs: Ok.
          - Primeiro Nome: Ok
        """

        return desc

    except Exception as Error:

        return function_gerenic_except_handler(__name__, 'function_description', Error)