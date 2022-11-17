from Repositorios.ResultadoRepositorio import ResultadoRepositorio
from Repositorios.MesaRepositorio import MesaRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa

class ResultadoControlador():

    # Constructor
    def __init__(self):
        self.repositorioResultado = ResultadoRepositorio()
        self.repositorioCandidato = CandidatoRepositorio()
        self.repositorioMesa = MesaRepositorio()

    # Get
    def index(self): 
        return self.repositorioResultado.findAll()

    # Create
    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    # Get x _id
    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    # Update
    def update(self, id, infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    # Delete
    def delete(self, id):
        return self.repositorioResultado.delete(id)

    # Muestra los resultados por candidato
    def getListarCandidatosMesa(self, id_mesa):
        return self.repositorioResultado.getListadoCandidatosInscritosMesa(id_mesa)

    # Muestra los resultados por mesa
    def getListarMesasDeInscritoCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoMesasCandidatoInscrito(id_candidato)

    # Muestra el total de votos por candidato
    def getMayorCedula(self):
        return self.repositorioResultado.getNumeroCedulaMayorCandidato()