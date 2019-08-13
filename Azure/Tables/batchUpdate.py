from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from azure.cosmosdb.table.tablebatch import TableBatch

table_service = TableService(account_name='az532rg1diag572', account_key='coixsNqJU6lbm2w9yCWh+fODv+NqAFjgV+jHRy4zkZX8ywkrJ+nfawSPNCF0tgzOh8FstVAG4tUu/pOeDwfLEQ==')

batch = TableBatch()
task008 = {'PartitionKey': 'tasksTigard', 'RowKey':'008', 'description': 'Go grocery shopping', 'priority': 400}
task009 = {'PartitionKey': 'tasksTigard', 'RowKey':'009', 'description': 'Clean the bathroom', 'priority': 100}
batch.insert_entity(task008)
batch.insert_entity(task009)
table_service.commit_batch('tasktable', batch)

task010 = {'PartitionKey': 'tasksTigard', 'RowKey':'010', 'description': 'Go grocery shopping', 'priority': 400}
task011 = {'PartitionKey': 'tasksTigard', 'RowKey':'011', 'description': 'Clean the bathroom', 'priority': 100}

with table_service.batch('tasktable') as batch:
    batch.insert_entity(task010)
    batch.insert_entity(task011)