import inventory_pb2_grpc
from time import time
import inventory_pb2
import grpc
import pandas as pd

def requestResponseData(stub, method, *args):
    start_time = time()
    response = method(*args)
    end_time = time()
    response_time = end_time - start_time
    return response, response_time

def search_in_excel(file_path):
    df = pd.read_excel(file_path)
    result = df.to_dict(orient='records')
    return result

def run():
    with grpc.insecure_channel('54.160.226.4:50051') as channel:
        stub = inventory_pb2_grpc.InventoryServiceStub(channel)
        excel_file_path = r'InventoryData.xlsx'

        inventory_data = search_in_excel(excel_file_path)

        if not inventory_data:
            print("No Inventory data found in the Excel file.")
            return

        while True:
            print("1. Search by ID")
            print("2. Search by Key Value pair")
            print("3. Search within a range")
            print("4. Calculate percentile")
            print("5. Update a value")
            print("6. Exit")
            choice = input("Which gRPC operation would you like to perform (1/2/3/4/5/6): ")

            if choice == '1':
                inventory_id = input("Enter the Inventory ID to search: ")

                # Search for the Inventory ID in the local data
                found_inventory = next((item for item in inventory_data if item['Inventory_ID'] == inventory_id), None)

                # ...

                if found_inventory:
                    print("\nFound in local data:")
                    print("Local data details:")
                    for key, value in found_inventory.items():
                        print(f"{key}: {value}")

                    # Search for the Inventory ID on the gRPC server
                    try:
                        response = stub.searchByID(inventory_pb2.InventoryRequest(id=inventory_id))
                        if response.Inventory_ID:
                            print("\nResult from gRPC server:")
                            print("gRPC server response details:")
                            print(f"Inventory_ID: {response.Inventory_ID}")
                            print(f"Name: {response.Name}")
                            print(f"Description: {response.Description}")
                            print(f"Price: {response.Price}")
                            print(f"Quantity_in_Stock: {response.Quantity_in_Stock}")
                            print(f"Quantity_in_Reorder: {response.Quantity_in_Reorder}")
                            print(f"Discontinued: {response.Discontinued}")
                        else:
                            print(f"Error: {response}")
                    except grpc.RpcError as e:
                        # Handle NOT_FOUND error
                        if e.code() == grpc.StatusCode.NOT_FOUND:
                            print("Inventory ID", inventory_id, "not found on the gRPC server.")
                        else:
                            print(f"Error: {e}")
                else:
                    print("Inventory ID", inventory_id, "not found in the local data.")


            elif choice == '2':
                key_name = input("Enter the key name: ")
                key_value = input("Enter the key value: ")
                try:
                    response = stub.search(inventory_pb2.InventorySearchRequest(key_name=key_name, key_value=key_value))
                    if response.Inventory_ID:
                        print("\nResult from gRPC server:")
                        print("gRPC server response details:")
                        print(f"Inventory_ID: {response.Inventory_ID}")
                        print(f"Name: {response.Name}")
                        print(f"Description: {response.Description}")
                        print(f"Price: {response.Price}")
                        print(f"Quantity_in_Stock: {response.Quantity_in_Stock}")
                        print(f"Quantity_in_Reorder: {response.Quantity_in_Reorder}")
                        print(f"Discontinued: {response.Discontinued}")
                    else:
                        print(f"Error: {response}")
                except grpc.RpcError as e:
                    # Handle NOT_FOUND error
                    if e.code() == grpc.StatusCode.NOT_FOUND:
                        print(f"Key '{key_name}' with value '{key_value}' not found on the gRPC server.")
                    else:
                        print(f"Error: {e}")

            elif choice == '3':
                key_name = input("Enter the key name: ")
                key_value_start = input("Enter the start value: ")
                key_value_end = input("Enter the end value: ")

                try:
                    response_iterator = stub.searchRange(
                        inventory_pb2.InventoryRangeRequest(
                            key_name=key_name,
                            key_value_start=key_value_start,
                            key_value_end=key_value_end
                        )
                    )

                    print("\nResult from gRPC server:")
                    print("gRPC server response details:")
                    for response in response_iterator:
                        print(f"Inventory_ID: {response.Inventory_ID}")
                        print(f"Name: {response.Name}")
                        print(f"Description: {response.Description}")
                        print(f"Price: {response.Price}")
                        print(f"Quantity_in_Stock: {response.Quantity_in_Stock}")
                        print(f"Quantity_in_Reorder: {response.Quantity_in_Reorder}")
                        print(f"Discontinued: {response.Discontinued}")

                except grpc.RpcError as e:
                    print(f"Error: {e}")

            elif choice == '4':
                key_name = input("Enter the key name: ")
                percentile = float(input("Enter the percentile: "))
                try:
                    response = stub.getDistribution(inventory_pb2.DistributionRequest(key_name=key_name, percentile=percentile))
                    print("\nResult from gRPC server:")
                    print("gRPC server response details:")
                    print(f"Percentile Value: {response.value}")
                except grpc.RpcError as e:
                    print(f"Error: {e}")

            elif choice == '5':
                key_name = input("Enter the key name: ")
                key_value = input("Enter the key value: ")
                val_name = input("Enter the attribute name to update: ")
                val_val_new = input("Enter the new value: ")

                try:
                    response = stub.update(inventory_pb2.UpdateRequest(
                        key_name=key_name,
                        key_value=key_value,
                        val_name=val_name,
                        val_val_new=val_val_new
                    ))

                    if response.success:
                        print("\nUpdate successful.")
                    else:
                        print("Update failed. Record not found on the gRPC server.")
                except grpc.RpcError as e:
                    print(f"Error: {e}")

            elif choice =='6':
                print("Exiting Program")
                break  # Exit the loop

            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.")

if __name__ == "__main__":
    run()