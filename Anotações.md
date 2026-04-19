




### Comandos executados
Executando no ambiente virtual
>poetry run fastapi dev .\fast_app\app.py

Para ativar o ambiente virtual
>poetry shell
Habilitar execução de scripts windows:
>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Executar apos habilitar o ambiente virtual
>fastapi dev .\fast_app\app.py

Documentação Swagger
http://localhost:8000/docs

### Formatador de codigo
>ruff check
>ruff format .

### Taskipy
A ideia do Taskipy é ser um executor de tarefas (task runner) complementar em nossa aplicação. No lugar de ter que lembrar comandos como o do fastapi, que vimos na execução da aplicação, que tal substituir ele simplesmente por task run?

```
[tool.taskipy.tasks]
pre_lint = 'typos'
lint = 'ruff check'
pre_format = 'ruff check --fix'
format = 'ruff format'
run = 'fastapi dev fast_zero/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'
```

### Testes
Temos 3 etapas dos testes:

**Fase 1 - Organizar (Arrange)**
Nesta primeira etapa, estamos preparando o ambiente para o teste. No exemplo, a linha com o comentário Arrange não é o teste em si, ela monta o ambiente para o teste poder ser executado. Estamos configurando um client de testes para fazer a requisição ao app.

**Fase 2 - Agir (Act)**
Aqui é a etapa onde acontece a ação principal do teste, que consiste em chamar o Sistema Sob Teste (SUT). No nosso caso, o SUT é a rota /, e a ação é representada pela linha response = client.get('/'). Estamos exercitando a rota e armazenando sua resposta na variável response. É a fase em que o código de testes executa o código de produção que está sendo testado. Agir aqui significa interagir diretamente com a parte do sistema que queremos avaliar, para ver como ela se comporta.

**Fase 3 - Afirmar (Assert)**
Esta é a etapa de verificar se tudo correu como esperado. É fácil notar onde estamos fazendo a verificação, pois essa linha sempre tem a palavra reservada assert. A verificação é booleana, ou está correta, ou não está. Por isso, um teste deve sempre incluir um assert para verificar se o comportamento esperado está correto.


### Serving
Quando executamos esse comando. O FastAPI faz uma chamada ao uvicorn e iniciamos um servidor em loopback, acessível apenas internamente no nosso computador. Por isso, ao acessarmos http://127.0.0.1:8000/ no navegador, estamos fazendo uma requisição ao servidor em 127.0.0.1:8000.

**Usando o fastapi na rede local**
Falando em redes, o Uvicorn no seu PC também pode servir o FastAPI na sua rede local, comando --host:
>fastapi dev fast_app/app.py --host 0.0.0.0

### Http - Verbos
- **GET**: Utilizado para recuperar recursos, quando solicitamos um dado ja existente no servidor.
- **POST**: Permite criar um novo recurso, exemplo registrando um novo usuário.
- **PUT**: Atualiza um recurso existente, exemplo atualizar as informações de um usuário existente.
- **DELETE**: Exclui um recurso, exemplo remover um usuário especifico do sistema.

#### Códigos de resposta
- **1xx:** informativo — utilizada para enviar informações para o cliente de que sua requisição foi recebida e está sendo processada.
- **2xx:** sucesso — Indica que a requisição foi bem-sucedida (por exemplo, 200 OK, 201 Created).
- **3xx:** redirecionamento — Informa que mais ações são necessárias para completar a requisição (por exemplo, 301 Moved Permanently, 302 Found).
- **4xx:** erro no cliente — Significa que houve um erro na requisição feita pelo cliente (por exemplo, 400 Bad Request, 404 Not Found).
- **5xx:** erro no servidor — Indica um erro no servidor ao processar a requisição válida do cliente (por exemplo, 500 Internal Server Error, 503 Service Unavailable).

Todos os códigos:  [iana](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)

## APIs
Quando falamos sobre aplicações web que não envolvem uma camada de visualização, como HTML, geralmente estamos nos referindo a APIs. A sigla API vem de Application Programming Interface (Interface de Programação de Aplicações).

### Endpoint
O termo "endpoint" refere-se a um ponto específico em uma API para onde as requisições são enviadas. Basicamente, é um endereço na web (URL) onde o servidor ou a API está ativo e pronto para responder a requisições dos clientes. Por exemplo, um endpoint para recuperar informações de um usuário pode ter um endereço como https://api.exemplo.com/usuarios/{id}, onde {id} é o identificador único do usuário desejado.

### Documentação
Uma pergunta comum nesse estágio é: "Ok, mas como descobrir ou conhecer os endpoints disponíveis em uma API?". A resposta reside na documentação. Uma documentação eficaz é essencial em APIs, especialmente quando muitos clientes diferentes precisam se comunicar com o servidor.

A documentação de uma API serve como um guia ou um manual, facilitando o entendimento e a utilização por desenvolvedores e usuários finais. Ela desempenha um papel crucial ao:
- Definir claramente os endpoints e suas funcionalidades.
- Especificar os métodos HTTP suportados (GET, POST, PUT, DELETE, etc.).
- Descrever os parâmetros esperados em requisições e respostas.
- Fornecer exemplos de requisições e respostas para facilitar o entendimento.

#### OpenAPI e documentação automática
Uma das soluções mais eficazes para a documentação de APIs é a utilização da especificação OpenAPI, disponível em [OpenAPI Specification](https://swagger.io/specification/) - swagger

No contexto do FastAPI, há suporte automático tanto para Swagger UI quanto para Redoc. **/docs ou /redoc**

### Contratos em APIs JSON
Quando falamos sobre o compartilhamento de JSON entre cliente e servidor, é crucial estabelecer um entendimento mútuo sobre a estrutura dos dados que serão trocados. A este entendimento, denominamos schema, que atua como um contrato definindo a forma e o conteúdo dos dados trafegados.

O schema de uma API desempenha um papel fundamental ao assegurar que ambos, cliente e servidor, estejam alinhados quanto à estrutura dos dados. Este "contrato" especifica:
- Campos de Dados Esperados: quais campos são esperados na mensagem JSON, incluindo nomes de campos e tipos de dados (como strings, números, booleanos).
- Restrições Adicionais: como validações para tamanhos de strings, formatos de números e outros tipos de validação de dados.
- Estrutura de Objetos Aninhados: como os objetos são estruturados dentro do JSON, incluindo arrays e sub-objetos.

### Pydantic
No universo de APIs e contratos de dados, especialmente ao trabalhar com Python, o Pydantic se destaca como uma ferramenta poderosa e versátil. Essa biblioteca, altamente integrada ao ecossistema Python, especializa-se na criação de schemas de dados e na validação de tipos. Com o Pydantic, é possível expressar schemas JSON de maneira elegante e eficiente através de classes Python, proporcionando uma ponte robusta entre a flexibilidade do JSON e a segurança de tipos do Python.