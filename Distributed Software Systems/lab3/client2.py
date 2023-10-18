import grpc
import greet_pb2
import greet_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = greet_pb2_grpc.GreetServiceStub(channel)

    name = input("Enter your name: ")

    request = greet_pb2.GreetRequest(name=name)
    response = stub.Greet(request)

    print(f"Server response (Client 2) {name}: {response.mesage}")

if __name__ == '__main__':
    run_client()
