from Repositorios.MesaRepositorio import MesaRepositorio
from Modelos.Mesa import Mesa

class MesaControlador():

    # Constructor
    def __init__(self):
        self.repositorioMesa = MesaRepositorio()

    # Get
    def index(self):
        return self.repositorioMesa.findAll()

    # Create
    def create(self, infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    # Get x _id
    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    # Update
    def update(self, id, infoMesa):
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.numero = infoMesa["numero"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)

    # Delete
    def delete(self, id):
        return self.repositorioMesa.delete(id)