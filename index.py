import boto3

# Conecte-se ao serviço DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Crie uma tabela (se ainda não existir)
table = dynamodb.create_table(
    TableName='MinhaTabela',
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Espere a tabela ser criada
table.wait_until_exists()

# Prepare os dados a serem inseridos
dados = {
    'ID': '123',
    'Nome': 'Fulano da Silva',
    'Email': 'fulano@email.com'
}

# Insira os dados na tabela
table.put_item(Item=dados)

# Imprima uma mensagem de sucesso
print('Dados inseridos com sucesso!')
