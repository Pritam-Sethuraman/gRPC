import grpc
from inventory_pb2_grpc import InventoryServiceStub
from inventory_pb2 import InventoryRequest, InventorySearchRequest, InventoryRangeRequest, DistributionRequest, UpdateRequest

def run():
    channel = grpc.insecure_channel('localhost:50051')
    client = InventoryServiceStub(channel)

    # Search by ID
    request = InventoryRequest(id='IN0002')
    response = client.searchByID(request)
    print("Search by ID:")
    print(response)

    # Search by Key and Key Value
    search_request = InventorySearchRequest(key_name='Inventory ID', key_value='IN0003')
    response = client.search(search_request)
    print("Search by Key and Key Value:")
    print(response)

    # Search by Key and Range
    range_request = InventoryRangeRequest(key_name='Quantity in Reorder', key_value_start=50, key_value_end=150)
    response = client.searchRange(range_request)
    print("Search by Key and Range:")
    for record in response:
        print(record)

    # Get Distribution
    dist_request = DistributionRequest(key_name='Quantity in Stock', percentile=50)
    response = client.getDistribution(dist_request)
    print("Get Distribution (50th percentile):")
    print(response)

    # Update Record
    update_request = UpdateRequest(key_name='Inventory ID', key_value='IN0004', val_name='Quantity in Stock', val_val_new=60)
    response = client.update(update_request)
    print("Update Record:")
    print(response)

if __name__ == '__main__':
    run()
