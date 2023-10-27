package utn.tienda_libros.servicio;

import utn.tienda_libros.modelo.Libro;

public interface ILibroServicio {

    public list<Libro> listarLibros();

    public Libro buscarLibroPorId(Integer idLibro);

    public void guardarLibro(Libro libro);

    public void eliminarLibro(Libro libro);
}
