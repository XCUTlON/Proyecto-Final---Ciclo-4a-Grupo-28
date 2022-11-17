from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

##########################################
#   Cargar el archivo de configuración   #
##########################################
def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

###################################
#       Función de conexión       #
###################################
def dbConnection():
    dataConfig = loadConfigFile()
    try:
        # Conexión MongoDB Atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca)
        # Conexión localhost
        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["database_votacion"]
    except ConnectionError:
        print("Error de conexión con la database")
    return db