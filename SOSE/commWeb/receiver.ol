include "console.iol"
include "interface.iol"

inputPort MyInput {
Location:
	"socket://localhost:8000"
Protocol: http {format = "json"}
Interfaces: MyInterface
}

main
{
	inc( x )( y )
	{
		y.term=x.term+1	
	};
	println@Console( x )() 
	
}