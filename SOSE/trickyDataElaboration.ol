include "console.iol"
include "string_utils.iol"

main
{
	cities[0] = "Bologna";
	i = 0;
	while( i < #cities ) {
		println@Console( cities[i] )();
		i++;
		cities[i] = "Bologna"
	}
}