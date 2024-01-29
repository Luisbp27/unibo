include "interface.iol"

inputPort Port
{
Location: "socket://localhost:8000"
Protocol: sodep
Interfaces: sayHelloRR
}


main
{
sayHello(x)(y) {y="Hello "+x}
}