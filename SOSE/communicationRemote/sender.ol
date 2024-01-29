include "interface.iol"

outputPort receiver {
Location:
	"socket://serena.cs.unibo.it:8000"
Protocol: soap
Interfaces: MyInterface
}

main
{
	sendNumber@receiver( 5 )
}