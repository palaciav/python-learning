from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

table_service = TableService(account_name='az532rg1diag572', account_key='coixsNqJU6lbm2w9yCWh+fODv+NqAFjgV+jHRy4zkZX8ywkrJ+nfawSPNCF0tgzOh8FstVAG4tUu/pOeDwfLEQ==')

table_service.create_table('tasktable')
task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description': 'Take out the trash', 'priority': 200}
table_service.insert_entity('tasktable',task)

task = Entity()
task.PartitionKey = 'tasksSeattle'
task.RowKey = '002'
task.description = 'Wash the car'
task.priority = 100
table_service.insert_entity('tasktable', task)

