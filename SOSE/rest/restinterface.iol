type Note {
    .id: int
    .text: string
}

type Notes:void{
    .notes*: string
}

type noteRequest:void{
    .id: int
}

type empty:void

interface restInterface{

    RequestResponse: noteDetail (noteRequest) (Note)

    RequestResponse: notesList (empty) (Notes)
    
    //RequestResponse: addNote (note) (message) //in id [?] - text

    //RequestResponse: deleteNote (noteRequest) (message) //in id 
}
