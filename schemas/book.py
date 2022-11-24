def bookEntity(item) -> dict:
    return{
            "id":str(item["_id"]),
            "titulo": item["titulo"], 
            "autor": item["autor"],
            "editorial": item["editorial"],
            "idioma" : item["idioma"],
            "precio" : item["precio"]
    }

def booksEntity(entity) ->list:
    return [bookEntity(item) for item in entity] 
