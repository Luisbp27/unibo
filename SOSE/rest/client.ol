include "restinterface.iol"
include "string_utils.iol"

from console import Console
from console import ConsoleInputInterface


service ClientService{

    embed Console as Console 

    inputPort ConsoleInputPort {
        location: "local"
        interfaces: ConsoleInputInterface
    }

    outputPort server{
        location: "socket://localhost:8000"
        protocol: http{
            format = "json"
            osc << {
                noteDetail << {
                    template = "/api/note/{id}"
                    method = "get"
                }
                notesList << {
                    template = "/api/notes"
                    method = "get"
                }
            }
        }
        interfaces: restInterface
    }
    init{
        registerForInput@Console()()
    }

    main
    {
        
        req.id = 1

        notesList@server()(response)
	valueToPrettyString@StringUtils( response )( res1 );
    	println@Console( res1 )()
	req.id=1
	noteDetail@server(req)(response2)
	valueToPrettyString@StringUtils( response2 )( res2 );
    	println@Console( res2 )()
    }
}
