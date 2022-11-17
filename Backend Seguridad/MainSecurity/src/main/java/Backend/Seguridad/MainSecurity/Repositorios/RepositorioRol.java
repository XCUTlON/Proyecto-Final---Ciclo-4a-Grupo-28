package Backend.Seguridad.MainSecurity.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import Backend.Seguridad.MainSecurity.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}