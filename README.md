<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Challenge Dev Django</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.5;
            margin: 0;
            padding: 0;
        }

        h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }

        h2 {
            color: #333;
            font-size: 20px;
            margin-bottom: 15px;
        }

        p {
            color: #666;
            font-size: 16px;
            margin-bottom: 10px;
        }

        code {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 4px;
            display: inline-block;
            padding: 2px 6px;
        }

        pre {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            white-space: pre-wrap;
        }

        a {
            color: #007bff;
            text-decoration: none;
        }
    </style>
</head>

<body>
    <h1>Challenge Dev Django</h1>

    <h2>Pré-requisitos</h2>
    <p>Certifique-se de ter os seguintes itens instalados no seu sistema:</p>
    <ul>
        <li>Docker</li>
        <li>Docker Compose</li>
    </ul>

    <h2>Instruções de instalação</h2>

    <ol>
        <li>Crie um arquivo chamado <code>.env</code> seguindo o exemplo do arquivo <code>.env.example</code> no repositório.</li>
        <li>Execute o comando <code>docker-compose up --build</code> para iniciar o projeto.</li>
        <li>Para acessar o painel de administração, utilize as seguintes credenciais:</li>
    </ol>
    <ul>
        <li>Nome de usuário: <code>admin</code></li>
        <li>Senha: <code>admin123</code></li>
    </ul>

    <p>Para acessar a rota de resposta, utilize o seguinte formato de URL:</p>
    <pre><code>http://localhost:8000/response/id_da_proposta/</code></pre>

    <p>O administrador do Django é responsável por montar a proposta.</p>

    <h2>Conclusão</h2>
    <p>Siga as instruções acima para configurar e executar o projeto. Se tudo for feito corretamente, você poderá
        acessar o painel de administração e utilizar a rota para responder à proposta.</p>
</body>

</html>
