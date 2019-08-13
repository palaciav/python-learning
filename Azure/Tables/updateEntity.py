from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

table_service = TableService(account_name='az532rg1diag572', account_key='coixsNqJU6lbm2w9yCWh+fODv+NqAFjgV+jHRy4zkZX8ywkrJ+nfawSPNCF0tgzOh8FstVAG4tUu/pOeDwfLEQ==')

if table_service.exists('tasktable'):
    task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description': 'Take out the garbage.', 'priority': 250}
    table_service.update_entity('tasktable', task)

# Replace the entity created earlier
task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description': 'Take out the garbage again...', 'priority': 250}
table_service.insert_or_replace_entity('tasktable', task)

#Insert a new entity
task = {'PartitionKey': 'tasksTigard', 'RowKey':'001', 'description': 'Buy detergent', 'priority':300}
table_service.insert_or_replace_entity('tasktable',task)