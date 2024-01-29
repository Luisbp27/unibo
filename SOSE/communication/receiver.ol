include "console.iol"
include "interface.iol"

inputPort MyInput {
Location:
	"socket://localhost:8000"
Protocol: soap
Interfaces: MyInterface
}

main
{
	sendNumber( x );
	println@Console( x )()
}