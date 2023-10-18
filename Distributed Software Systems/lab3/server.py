import grpc
import greet_pb2
import greet_pb2_grpc

class GreetServicer(greet_pb2_grpc.GreetServiceServicer):
    def Greet(self, request, context):
        response = greet_pb2.GreetResponse(message=f"Hello, {request.name}!")
        return response

def run_server():
    server = grpc.server(grpc.InsecureServer())
    greet_pb2_grpc.add_GreetServiceServicer_to_server(GreetServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
