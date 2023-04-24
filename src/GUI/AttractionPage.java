package GUI;

import baseDatos.FachadaBaseDatos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AttractionPage extends JDialog {

    private FachadaBaseDatos fachadaBaseDatos;
    private JButton añadirAtraccionButton;
    private JButton eliminarAtraccionButton;
    private JButton SALIRButton;
    private JButton VOLVERButton;
    private JPanel MainPanel;

    public AttractionPage(JFrame parent, FachadaBaseDatos fachadaBaseDatos) {
        super(parent);
        this.fachadaBaseDatos = fachadaBaseDatos;
        //ponemos el titulo de la pestaña
        setTitle("Atracciones");
        //Mostramos el panel del .form
        setContentPane(MainPanel);
        //Ponemos el tamaño de la ventana
        setMinimumSize(new Dimension(700, 500));
        //Centramos la pestaña
        //IMPORTANTE!! La instancia parent se la paso para centrar la pestaña em el centro del ordenador, pero se le pasa null
        setLocationRelativeTo(parent);
        //Esto hace que se cierre al darle a la X
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);

        //Cierra la plataforma
        SALIRButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });

        //Vuelve a la ventana anterior
        VOLVERButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                AdminPage menuAdmin = new AdminPage(null,fachadaBaseDatos);
            }
        });

        //Lanza la pestaña de eliminar atraccion
        eliminarAtraccionButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                DeleteAttraction DeleteAttraction = new DeleteAttraction(null,fachadaBaseDatos);
                dispose();
            }
        });

        //Ponemos que se visualice la ventana
        setVisible(true);
        añadirAtraccionButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                AddAttraction AddAttraction = new AddAttraction(null,fachadaBaseDatos);
                dispose();
            }
        });
    }
}