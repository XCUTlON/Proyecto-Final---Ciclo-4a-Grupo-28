from Repositorios.PartidoRepositorio import PartidoRepositorio
from Modelos.Partido import Partido

class PartidoControlador():

    # Constructor
    def __init__(self):
        self.repositorioPartido = PartidoRepositorio()

    # Get
    def index(self):
        return self.repositorioPartido.findAll()

    # Create
    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    # Get x _id
    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    # Update
    def update(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)

    # Delete
    def delete(self, id):
        return self.repositorioPartido.delete(id)