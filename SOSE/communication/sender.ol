include "interface.iol"

outputPort receiver {
Location:
	"socket://localhost:8000"
Protocol: soap
Interfaces: MyInterface
}

main
{
	sendNumber@receiver( 5 )
}