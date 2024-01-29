include "interface.iol"
include "console.iol"

outputPort Server
{
Location: "socket://localhost:8000"
Protocol: sodep
Interfaces: sayHelloRR
}


main
{
sayHello@Server("John")(x);
println@Console(x)()
}