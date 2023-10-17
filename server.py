import grpc
import pandas as pd  # Import Pandas library for reading Excel files
from concurrent import futures
from inventory_pb2_grpc import InventoryServiceServicer, add_InventoryServiceServicer_to_server
from inventory_pb2 import InventoryRequest, InventoryRecord, InventorySearchRequest, InventoryRangeRequest, DistributionRequest, UpdateRequest, UpdateResponse

# Load inventory data from Excel file
inventory_data = pd.read_excel('inventoryData.xlsx')

class InventoryServiceServicer(InventoryServiceServicer):
    def searchByID(self, request, context):
        inventory_id = request.id
        record = inventory_data[inventory_data['Inventory ID'] == inventory_id]
        if not record.empty:
            record_dict = record.to_dict(orient='records')[0]
            return InventoryRecord(**record_dict)
        return InventoryRecord()  # Return an empty record if not found

    def search(self, request, context):
        key_name = request.key_name
        key_value = request.key_value
        record = inventory_data[inventory_data[key_name] == key_value]
        if not record.empty:
            record_dict = record.to_dict(orient='records')[0]
            return InventoryRecord(**record_dict)
        return InventoryRecord()  # Return an empty record if not found

    def searchRange(self, request, context):
        key_name = request.key_name
        key_value_start = request.key_value_start
        key_value_end = request.key_value_end
        records = inventory_data[
            (inventory_data[key_name] >= key_value_start) & (inventory_data[key_name] <= key_value_end)
        ]
        records_dict = records.to_dict(orient='records')
        return [InventoryRecord(**record_dict) for record_dict in records_dict]

    def getDistribution(self, request, context):
        key_name = request.key_name
        values = inventory_data[key_name].tolist()
        values.sort()
        total_records = len(values)
        if total_records == 0:
            return None  # Key not found

        # Calculate the percentile value
        index = int((request.percentile / 100) * total_records)
        return float(values[index])

    def update(self, request, context):
        key_name = request.key_name
        key_value = request.key_value
        val_name = request.val_name
        val_val_new = request.val_val_new

        record = inventory_data[inventory_data[key_name] == key_value]

        if not record.empty:
            inventory_data.at[record.index, val_name] = val_val_new
            return UpdateResponse(success=True)
        return UpdateResponse(success=False)  # Return false if record not found

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_servicer = InventoryServiceServicer()
    add_InventoryServiceServicer_to_server(my_servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
