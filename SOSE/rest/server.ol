include "restinterface.iol"
include "console.iol"
include "string_utils.iol"

execution { concurrent }

//service RestServer {

    inputPort WebPort{
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

    init {
        notes[0] << {
                .id = 1, .text = "testnote1"
  		}
	notes[1] << {
                .id = 2, .text = "testnote2"
            }
        }

    main {


        [noteDetail (request) (response) {
            //println@Console(request)()
            for (i=0,i<#notes,i++){
                if (notes[i].id == request.id){
		    println@Console("Trovata")()
                    response << notes[i]
                }
            }
        }]


        [notesList (request) (response) {
            println@Console("test")()
            for(i=0,i<#notes,i++) {
                println@Console(notes[i].text)()
                response.notes[i] = notes[i].text
            }
        }]

    }

//}