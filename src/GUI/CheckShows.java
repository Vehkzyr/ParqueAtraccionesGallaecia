package GUI;

import aplicacion.Atraccion;
import aplicacion.Espectaculo;
import baseDatos.FachadaBaseDatos;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.ArrayList;

public class CheckShows extends JDialog{
    private JTable table1;
    private JButton VOLVERButton;
    private JButton SALIRButton;
    private JPanel MainPanel;
    private FachadaBaseDatos fachadaBaseDatos;
    private JScrollPane scrollPane1;

    public CheckShows(JFrame parent, FachadaBaseDatos fachadaBaseDatos, String User) {
        super(parent);
        this.fachadaBaseDatos = fachadaBaseDatos;
        //ponemos el titulo de la pestaña
        setTitle("Ver Atracciones");
        //Mostramos el panel del .form
        setContentPane(MainPanel);
        createUIComponents();

        //Ponemos el tamaño de la ventana
        setMinimumSize(new Dimension(700, 500));
        //Centramos la pestaña
        //IMPORTANTE!! La instancia parent se la paso para centrar la pestaña em el centro del ordenador, pero se le pasa null
        setLocationRelativeTo(parent);
        //Esto hace que se cierre al darle a la X
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        setVisible(true);

        //Boton de salir (Cierra la ventana)
        SALIRButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });

        //Boton de volver a la pestaña anterior
        VOLVERButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                UserPage menuEmployee = new UserPage(null, fachadaBaseDatos, User);
            }
        });
    }

    private void createUIComponents() {
        // Crear un modelo de tabla con tres columnas
        DefaultTableModel model = new DefaultTableModel();
        model.addColumn("Nombre");
        model.addColumn("Tematica");
        model.addColumn("Sesion");
        model.addColumn("Ubicacion");

        java.util.List<Espectaculo> listaEspectaculos = null;
        try {
            listaEspectaculos = FachadaBaseDatos.consultarEspectaculos();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        for (int i = 0; i < listaEspectaculos.size(); i++) {
            model.addRow(new Object[]{listaEspectaculos.get(i).getNombre(), listaEspectaculos.get(i).getTematica(),
                    listaEspectaculos.get(i).getSesion(),listaEspectaculos.get(i).getUbicacion()});
        }
        // Crear el JTable y asignarle el modelo
        table1 = new JTable(model);

        // Crear el JScrollPane y asignarle el JTable
        scrollPane1 = new JScrollPane(table1);
    }
}
