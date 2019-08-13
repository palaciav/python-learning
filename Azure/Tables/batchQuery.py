from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

table_service = TableService(account_name='az532rg1diag572', account_key='coixsNqJU6lbm2w9yCWh+fODv+NqAFjgV+jHRy4zkZX8ywkrJ+nfawSPNCF0tgzOh8FstVAG4tUu/pOeDwfLEQ==')

tasks = table_service.query_entities('tasktable',filter="PartitionKey eq 'tasksTigard'")
print("Tasks to do in Tigard:")
for task in tasks:
    print(task.description)
    print(task.priority)