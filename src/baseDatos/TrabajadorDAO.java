/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package baseDatos;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.sql.Date;
import java.sql.ResultSet;
import java.util.logging.Level;
import java.util.logging.Logger;
import aplicacion.TrabajadorEspectaculo;
import aplicacion.TrabajadorMantenimiento;
import aplicacion.TrabajadorAdministracion;
import aplicacion.Trabajador;

/**
 *
 * @author Manuel Estevez, Miguel Leal, Pablo Lobato y Pablo Seijo
 */
public class TrabajadorDAO extends AbstractDAO{

    public TrabajadorDAO (Connection conexion, aplicacion.FachadaAplicacion fa) {
        super.setConexion(conexion);
        super.setFachadaAplicacion(fa);
    }

        // Añadir trabajadore de administracion
        public void anhadirTrabajadorAdministracion(String dni, String nombre, String direccion, float salario, String telefono, Date fechaContratacion,  Date fechaNacimiento, String formacion, String espectaculo, String atraccion) throws SQLException {
            Connection con;
    
            con = super.getConexion();
            
            PreparedStatement stmTrabajador = null;
            stmTrabajador = con.prepareStatement("INSERT INTO TrabajadoresAdministracion (dni,nombre,direccion,telefono,fechainicio,fechanacimiento,nombreatraccion,salario) values(?,?,?,?,now(),?,?,?)");
            stmTrabajador.setString(1, dni);
            stmTrabajador.setString(2, nombre);
            stmTrabajador.setString(3, direccion);
            stmTrabajador.setFloat(4, salario);
            stmTrabajador.setString(5, telefono);
            stmTrabajador.setDate(6, fechaContratacion);
            stmTrabajador.setDate(7, fechaNacimiento);
            stmTrabajador.setString(8, formacion);
            stmTrabajador.setString(9, espectaculo);
            stmTrabajador.setString(10, atraccion);
            stmTrabajador.executeUpdate();
            stmTrabajador.close();
        }

    // Añadir trabajadore de mantenimiento
    public void anhadirTrabajadorMantenimiento(String dni, String nombre, String direccion, float salario, String telefono, Date fechaContratacion,  Date fechaNacimiento, String formacion, String atraccion) throws SQLException {
        Connection con;
        con = super.getConexion();
        
        PreparedStatement stmTrabajador = null;
        stmTrabajador = con.prepareStatement("INSERT INTO TrabajadoresMantenimiento (dni,nombre,direccion,telefono,fechainicio,fechanacimiento,nombreatraccion,salario) values(?,?,?,?,now(),?,?,?)");
        stmTrabajador.setString(1, dni);
        stmTrabajador.setString(2, nombre);
        stmTrabajador.setString(3, direccion);
        stmTrabajador.setFloat(4, salario);
        stmTrabajador.setString(5, telefono);
        stmTrabajador.setDate(6, fechaContratacion);
        stmTrabajador.setDate(7, fechaNacimiento);
        stmTrabajador.setString(8, formacion);
        stmTrabajador.setString(9, atraccion);
        stmTrabajador.executeUpdate();
        stmTrabajador.close();
    }

    // Añadir trabajadores de espectaculos
    public void anhadirTrabajadorEspectaculo(String dni, String nombre, String direccion, float salario, String telefono, Date fechaContratacion,  Date fechaNacimiento, String formacion, String espectaculo) throws SQLException {
        Connection con;

        con = super.getConexion();
        
        PreparedStatement stmTrabajador = null;
        stmTrabajador = con.prepareStatement("INSERT INTO TrabajadoresEspectaculo (dni,nombre,direccion,telefono,fechainicio,fechanacimiento,nombreatraccion,salario) values(?,?,?,?,now(),?,?,?)");
        stmTrabajador.setString(1, dni);
        stmTrabajador.setString(2, nombre);
        stmTrabajador.setString(3, direccion);
        stmTrabajador.setFloat(4, salario);
        stmTrabajador.setString(5, telefono);
        stmTrabajador.setDate(6, fechaContratacion);
        stmTrabajador.setDate(7, fechaNacimiento);
        stmTrabajador.setString(8, formacion);
        stmTrabajador.setString(9, espectaculo);
        stmTrabajador.executeUpdate();
        stmTrabajador.close();
    }

    // Despedir administarcion
    public void despedirTrabajadorAdministracion(String dni) {

        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();
        try {
            stmTrabajadores = con.prepareStatement("DELETE from TrabajadoresAdministracion where DNI = ?");
            stmTrabajadores.setString(1, dni);
            stmTrabajadores.executeUpdate();
        } catch (SQLException ex) {
            Logger.getLogger(HostelerosDAO.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    // Despedir mantenimiento
    public void despedirTrabajadorMantenimiento(String dni) {

        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();
        try {
            stmTrabajadores = con.prepareStatement("DELETE from TrabajadoresMantenimiento where DNI = ?");
            stmTrabajadores.setString(1, dni);
            stmTrabajadores.executeUpdate();
        } catch (SQLException ex) {
            Logger.getLogger(HostelerosDAO.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    // Despedir espectaculo
    public void despedirTrabajadorEspectaculo(String dni) {

        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();
        try {
            stmTrabajadores = con.prepareStatement("DELETE from TrabajadoresEspectaculo where DNI = ?");
            stmTrabajadores.setString(1, dni);
            stmTrabajadores.executeUpdate();
        } catch (SQLException ex) {
            Logger.getLogger(HostelerosDAO.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    // Obtener una lista de todos los trabajadores
    public ArrayList<Trabajador> getTrabajadores() {
        ArrayList<Trabajador> resultado = new ArrayList<>();
        ResultSet rsTrabajadores;
        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();


        // Trabajadores Administracion
        try {
            stmTrabajadores = con.prepareStatement("select * from TrabajadoresAdministracion order by fechaContratacion");
            rsTrabajadores = stmTrabajadores.executeQuery();
            TrabajadorAdministracion trabajador;
            while (rsTrabajadores.next()) {
                trabajador = new TrabajadorAdministracion(rsTrabajadores.getString("DNI"), rsTrabajadores.getString("Nombre"), rsTrabajadores.getString("Direccion"), rsTrabajadores.getFloat("Salario"), rsTrabajadores.getString("Telefono"), rsTrabajadores.getString("fechaContratacion"), rsTrabajadores.getString("fechaNacimiento"), rsTrabajadores.getString("Formacion"), rsTrabajadores.getString("Espectaculo"), rsTrabajadores.getString("Atraccion"));
                resultado.add(trabajador);
            }

        } catch (SQLException ex) {
            Logger.getLogger(TrabajadorDAO.class.getName()).log(Level.SEVERE, null, ex);
        }

        // Trabajadores mantenimiento
        try {
            stmTrabajadores = con.prepareStatement("select * from TrabajadoresMantenimiento order by fechaContratacion");
            rsTrabajadores = stmTrabajadores.executeQuery();
            TrabajadorMantenimiento trabajador;
            while (rsTrabajadores.next()) {
                trabajador = new TrabajadorMantenimiento(rsTrabajadores.getString("DNI"), rsTrabajadores.getString("Nombre"), rsTrabajadores.getString("Direccion"), rsTrabajadores.getFloat("Salario"), rsTrabajadores.getString("Telefono"), rsTrabajadores.getString("fechaContratacion"), rsTrabajadores.getString("fechaNacimiento"), rsTrabajadores.getString("Formacion"), rsTrabajadores.getString("Atraccion"));
                resultado.add(trabajador);
            }

        } catch (SQLException ex) {
            Logger.getLogger(TrabajadorDAO.class.getName()).log(Level.SEVERE, null, ex);
        }

        // Trabajadores Espectaculo
        try {
            stmTrabajadores = con.prepareStatement("select * from TrabajadoresEspectaculo order by fechaContratacion");
            rsTrabajadores = stmTrabajadores.executeQuery();
            TrabajadorEspectaculo trabajador;
            while (rsTrabajadores.next()) {
                trabajador = new TrabajadorEspectaculo(rsTrabajadores.getString("DNI"), rsTrabajadores.getString("Nombre"), rsTrabajadores.getString("Direccion"), rsTrabajadores.getFloat("Salario"), rsTrabajadores.getString("Telefono"), rsTrabajadores.getString("fechaContratacion"), rsTrabajadores.getString("fechaNacimiento"), rsTrabajadores.getString("Formacion"), rsTrabajadores.getString("Espectaculo"));
                resultado.add(trabajador);
            }

        } catch (SQLException ex) {
            Logger.getLogger(TrabajadorDAO.class.getName()).log(Level.SEVERE, null, ex);
        }

        return resultado;
    }

    // Obtener una lista de los trabajadores de Administracion
    public ArrayList<TrabajadorAdministracion> getTrabajadoresAdministracion() {
        ArrayList<TrabajadorAdministracion> resultado = new ArrayList<>();
        ResultSet rsTrabajadores;
        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();

        try {
            stmTrabajadores = con.prepareStatement("select * from TrabajadoresAdministracion order by fechaContratacion");
            rsTrabajadores = stmTrabajadores.executeQuery();
            TrabajadorAdministracion trabajador;
            while (rsTrabajadores.next()) {
                trabajador = new TrabajadorAdministracion(rsTrabajadores.getString("DNI"), rsTrabajadores.getString("Nombre"), rsTrabajadores.getString("Direccion"), rsTrabajadores.getFloat("Salario"), rsTrabajadores.getString("Telefono"), rsTrabajadores.getString("fechaContratacion"), rsTrabajadores.getString("fechaNacimiento"), rsTrabajadores.getString("Formacion"), rsTrabajadores.getString("Espectaculo"), rsTrabajadores.getString("Atraccion"));
                resultado.add(trabajador);
            }

        } catch (SQLException ex) {
            Logger.getLogger(TrabajadorDAO.class.getName()).log(Level.SEVERE, null, ex);
        }

        return resultado;
    }

    // Obtener una lista de los trabajadores de Mantenimiento
    public ArrayList<TrabajadorMantenimiento> getTrabajadoresMantenimiento() {
        ArrayList<TrabajadorMantenimiento> resultado = new ArrayList<>();
        ResultSet rsTrabajadores;
        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();

        try {
            stmTrabajadores = con.prepareStatement("select * from TrabajadoresMantenimiento order by fechaContratacion");
            rsTrabajadores = stmTrabajadores.executeQuery();
            TrabajadorMantenimiento trabajador;
            while (rsTrabajadores.next()) {
                trabajador = new TrabajadorMantenimiento(rsTrabajadores.getString("DNI"), rsTrabajadores.getString("Nombre"), rsTrabajadores.getString("Direccion"), rsTrabajadores.getFloat("Salario"), rsTrabajadores.getString("Telefono"), rsTrabajadores.getString("fechaContratacion"), rsTrabajadores.getString("fechaNacimiento"), rsTrabajadores.getString("Formacion"), rsTrabajadores.getString("Atraccion"));
                resultado.add(trabajador);
            }

        } catch (SQLException ex) {
            Logger.getLogger(TrabajadorDAO.class.getName()).log(Level.SEVERE, null, ex);
        }

        return resultado;
    }

    // Obtener una lista de los trabajadores de Espectaculos
    public ArrayList<TrabajadorEspectaculo> getTrabajadoresEspectaculos() {
        ArrayList<TrabajadorEspectaculo> resultado = new ArrayList<>();
        ResultSet rsTrabajadores;
        PreparedStatement stmTrabajadores = null;
        Connection con;
        con = super.getConexion();

        try {
            stmTrabajadores = con.prepareStatement("select * from TrabajadoresEspectaculo order by fechaContratacion");
            rsTrabajadores = stmTrabajadores.executeQuery();
            TrabajadorEspectaculo trabajador;
            while (rsTrabajadores.next()) {
                trabajador = new TrabajadorEspectaculo(rsTrabajadores.getString("DNI"), rsTrabajadores.getString("Nombre"), rsTrabajadores.getString("Direccion"), rsTrabajadores.getFloat("Salario"), rsTrabajadores.getString("Telefono"), rsTrabajadores.getString("fechaContratacion"), rsTrabajadores.getString("fechaNacimiento"), rsTrabajadores.getString("Formacion"), rsTrabajadores.getString("Espectaculo"));
                resultado.add(trabajador);
            }

        } catch (SQLException ex) {
            Logger.getLogger(TrabajadorDAO.class.getName()).log(Level.SEVERE, null, ex);
        }

        return resultado;
    }
}
