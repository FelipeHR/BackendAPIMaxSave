from pymongo import MongoClient

client = MongoClient('mongodb+srv://Checho:2laSw16x9MUf2rAv@serverlessinstance0.wkk1z.mongodb.net/?retryWrites=true&w=majority')

db = client['MaxSave']

col = db['gastos']

col.insert_one( {

    "monto": 10000,
    "fecha": "2022-07-10",
    "categoria": "Ropa",
    "descripcion": "guantes"
    
})
