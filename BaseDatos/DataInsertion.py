'''
@author Miguel Leal, Pablo Lobato, Manuel Estévez, Pablo Seijo
@date 12/abr/2023
@description script de creacion de una base de datos
'''

# Importamos la libreria para la gestion de la base de datos
import sqlite3


# Nos conectamos a la base de datos del gimnasio de la USC
miConexion = sqlite3.connect("ParqueAtraccionesGallaecia")

# Con la conexión, crea un objeto cursor
miCursor = miConexion.cursor()


#Hacemos una lista con tuplas para los espectaculos
espectaculos = [
    ("La Bella y la Bestia", "Tarde", '15:00', '17:30', "Musical", "Una historia clásica de amor y aceptación", "Teatro Occidental"),
    ("El Rey León", "Noche", '20:00', '22:30', "Musical", "Un relato épico sobre la vida y la muerte en la sabana africana", "Teatro Principal"),
    ("Mamma Mia!", "Tarde", '14:30', '17:00', "Musical", "Una divertida historia de amor y música al ritmo de ABBA", "Teatro Oriental"),
    ("Cats", "Noche", '19:30', '22:00', "Musical", "Un viaje al mundo de los gatos callejeros de Londres",
     "Teatro Occidental"),
    ("El Fantasma de la Ópera", "Noche", '21:00', '23:30', "Musical",
     "Una historia de amor y obsesión en el mundo de la ópera parisina del siglo XIX", "Teatro Principal"),
    ("Wicked", "Tarde", '16:00', '18:30', "Musical", "La historia detrás de la malvada bruja del oeste de Oz",
     "Teatro Oriental"),
    ("Les Misérables", "Noche", '20:30', '23:00', "Musical",
     "Una emocionante epopeya sobre la lucha por la libertad y la redención en la Francia del siglo XIX",
     "Teatro Occidental"),
    ("Chicago", "Tarde", '15:30', '18:00', "Musical",
     "Un retrato satírico y crítico de la justicia y la corrupción en la Chicago de los años 20", "Teatro Principal"),
    ("Phantom", "Noche", '19:00', '21:30', "Drama",
     "Una mirada profunda al mundo de los enfermos mentales y su lucha por la recuperación", "Teatro Oriental"),
    ("The Book of Mormon", "Tarde", '17:00', '19:30', "Musical",
     "Una irreverente comedia musical sobre dos misioneros mormones en África", "Teatro Principal"),
]

miCursor.executemany("INSERT INTO Espectaculos VALUES (NULL,?,?,?,?,?,?,?)", espectaculos) #Como el primer campo es auto increment le paso null

#Hacemos una lista con tuplas para los Visitantes
visitantes =  [
('34589123A', "Juan Pérez Gómez", "juanpgomez@gmail.com", "1980-05-12"),
('26347819B', "María Rodríguez Martínez", "mariarodriguezm@gmail.com", "1975-12-28"),
('16749235C', "Pedro Gómez Sánchez", "pedrogomezs@gmail.com", "1992-03-05"),
('39984560D', "Lucía Fernández López", "luciaflopez@gmail.com", "1987-11-02"),
('18563247E', "Diego Sánchez García", "diegosangarcia@gmail.com", "2001-08-20"),
('24789153F', "Ana Martínez Pérez", "anamperez@gmail.com", "1998-06-05"),
('43890261G', "Jorge Hernández Gutiérrez", "jorgehgutierrez@gmail.com", "1983-09-15"),
('31875492H', "Sofía González Ruiz", "sofiagr@gmail.com", "1995-02-12"),
('50263489I', "Manuel García Castro", "manuelgarcia@gmail.com", "1990-07-23"),
('12345678J', "Laura Pérez Torres", "lauraperez@gmail.com", "1988-04-17"),
('54673821K', "Carlos Rodríguez Díaz", "carlosrodriguezd@gmail.com", "1997-11-08"),
('78902345L', "Marina Sánchez Gómez", "marinasgomez@gmail.com", "1982-02-24"),
('23456789M', "Andrés Fernández García", "andresfgarcia@gmail.com", "1993-09-07"),
('98765432N', "Cristina López Pérez", "cristinalopezp@gmail.com", "1996-06-18"),
('67438902O', "Rafael González Sánchez", "rafaelgsanchez@gmail.com", "1985-03-30"),
('34567289P', "Isabel Martínez Ruiz", "isabelmr@gmail.com", "1999-10-10"),
('90871234Q', "Mario Hernández Castro", "mariohernandezc@gmail.com", "1991-05-02"),
('56789012R', "Luciana García Torres", "lucianagarcia@gmail.com", "1994-08-13"),
('45678901S', "David Pérez Sánchez", "davidpsanchez@gmail.com", "1989-01-28"),
('34567890T', "Verónica Rodríguez Fernández", "veronicarf@gmail.com", "2000-12-03"),
('65432109U', "Gabriel Sánchez Pérez", "gabrielsanchezp@gmail.com", "1996-07-20")
]

miCursor.executemany("INSERT INTO Visitantes VALUES (?,?,?,?)", visitantes) #Como el primer campo es auto increment le paso null

#Hacemos una lista con la hosteleria
hosteleria = [
    ('La Mar de Sabores', 50, 'sur', '09:00', '22:00', 1200.50),
    ('El Rincón del Sabor', 35, 'norte', '10:30', '23:00', 980.25),
    ('La Casa de las Carnes', 80, 'este', '12:00', '23:30', 2450.75),
    ('El Bodegón del Abuelo', 60, 'oeste', '11:30', '22:30', 1785.50),
    ('La Tasca del Puerto', 45, 'sur', '13:00', '23:45', 1432.00),
    ('El Sabor de la Huerta', 30, 'oeste', '11:00', '21:30', 675.00),
    ('La Taberna del Buen Vino', 55, 'norte', '10:00', '22:00', 1905.00)
]

miCursor.executemany("INSERT INTO Hosteleria VALUES (NULL,?,?,?,?,?,?)", hosteleria)


#Atracciones

atracciones = [
  ("Montaña rusa del dragón", 30, 120, 10000, False, "norte", "Una emocionante montaña rusa con giros y caídas vertiginosas"),
  ("La torre del terror", 20, 140, 8000, False, "sur", "Una atracción que simula una caída libre desde una gran altura"),
  ("La noria gigante", 40, 80, 5000, False, "este", "Una noria con vistas panorámicas de todo el parque"),
  ("La casa embrujada", 15, 110, 12000, False, "oeste", "Un oscuro y espeluznante recorrido por una casa encantada"),
  ("La rueda de la fortuna", 35, 70, 7000, False, "norte", "Una gran rueda con vistas al parque y sus alrededores"),
  ("La montaña rusa de la serpiente", 25, 130, 9000, False, "sur", "Una montaña rusa con loops y giros intensos"),
  ("El carrusel de los caballos", 30, 90, 4000, False, "este", "Un clásico carrusel con caballos decorativos"),
  ("El tiovivo de las mariposas", 20, 100, 4500, False, "oeste", "Un tiovivo con asientos con forma de mariposas"),
  ("El laberinto del minotauro", 10, 150, 15000, False, "norte", "Un laberinto lleno de sorpresas y peligros"),
  ("La atracción acuática del pulpo", 30, 110, 10000, False, "sur", "Una atracción que simula un paseo en bote por aguas turbulentas"),
  ("La torre de la emoción", 15, 160, 12000, False, "este", "Una torre que sube y baja a gran velocidad"),
  ("El castillo encantado", 20, 120, 8000, False, "oeste", "Un castillo lleno de trampas y sorpresas"),
  ("El tren fantasma", 25, 100, 7000, False, "norte", "Un recorrido en un tren a través de un túnel de terror"),
  ("La montaña rusa de la cobra", 30, 135, 9000, False, "sur", "Una montaña rusa con caídas y curvas vertiginosas"),
  ("El carrusel de los aviones", 25, 80, 4500, False, "este", "Un carrusel con asientos con forma de aviones"),
  ("La atracción acuática del calamar", 20, 115, 10000, False, "oeste", "Una atracción que simula un paseo en bote por aguas oscuras"),
  ("El laberinto del dragón", 10, 155, 15000, False, "norte", "Un laberinto lleno de dragones y tesoros")
]

miCursor.executemany("INSERT INTO Atracciones VALUES (NULL,?,?,?,?,?,?,?)", atracciones)

#ir

ir = [
('2023-04-01', '34589123A', 4),
('2023-04-02', '26347819B', 12),
('2023-04-02', '16749235C', 9),
('2023-04-03', '39984560D', 2),
('2023-04-04', '18563247E', 14),
('2023-04-04', '24789153F', 7),
('2023-04-05', '43890261G', 1),
('2023-04-06', '31875492H', 16),
('2023-04-06', '50263489I', 5),
('2023-04-07', '12345678J', 8),
('2023-04-08', '54673821K', 15),
('2023-04-08', '78902345L', 3)
]

miCursor.executemany("INSERT INTO Ir VALUES (?,?,?)", ir)

#comer
comer = [
('1980-05-12', '34589123A', 1),
('1975-12-28', '26347819B', 2),
('1992-03-05', '16749235C', 3),
('1987-11-02', '39984560D', 4),
('2001-08-20', '18563247E', 5),
('1998-06-05', '24789153F', 6),
('1983-09-15', '43890261G', 7),
('1995-02-12', '31875492H', 1),
('1990-07-23', '50263489I', 2),
('1988-04-17', '12345678J', 3),
('1997-11-08', '54673821K', 4),
('1982-02-24', '78902345L', 5),
('1993-09-07', '23456789M', 6),
('1996-06-18', '98765432N', 7),
('1985-03-30', '67438902O', 1),
('1999-10-10', '34567289P', 2),
('1991-05-02', '90871234Q', 3),
('1994-08-13', '56789012R', 4),
('1989-01-28', '45678901S', 5),
('2000-12-03', '34567890T', 6),
('1996-07-20', '65432109U', 7)
]

miCursor.executemany("INSERT INTO Comer VALUES (?,?,?)", comer)

#asistir
asistir = [
    ('2022-05-01', '34589123A', 5),
    ('2022-05-01', '26347819B', 8),
    ('2022-05-02', '16749235C', 2),
    ('2022-05-02', '39984560D', 10),
    ('2022-05-03', '18563247E', 4),
    ('2022-05-03', '24789153F', 6),
    ('2022-05-04', '43890261G', 1),
    ('2022-05-04', '31875492H', 9),
    ('2022-05-05', '50263489I', 3),
    ('2022-05-05', '12345678J', 7),
    ('2022-05-06', '54673821K', 5),
    ('2022-05-06', '78902345L', 8),
    ('2022-05-07', '23456789M', 2),
    ('2022-05-07', '98765432N', 10),
    ('2022-05-08', '67438902O', 4),
    ('2022-05-08', '34567289P', 6)
]

miCursor.executemany("INSERT INTO Asistir VALUES (?,?,?)", asistir)

#TrabajadorAdministracion

trabajadorAdministracion = [
('123456789S', 'Juan Pérez', 'Calle Mayor 1 28001 Madrid', 2500.0, 910000000, '2021-01-01', '1995-05-15', 'Ingeniero Informático', 1, 3),
('234567890C', 'María Rodríguez', 'Calle Ancha 10 28002 Madrid', 2200.0, 910000001, '2020-02-01', '1998-11-20', 'Licenciada en ADE', 2, 5),
('345678901V', 'Pedro Gómez', 'Calle Estrecha 5 28003 Madrid', 1800.0, 910000002, '2019-03-01', '1990-07-01', 'Diplomado en Empresariales', 3, 2),
('456789012S', 'Lucía Fernández', 'Calle Pequeña 3 28004 Madrid', 3000.0, 910000003, '2018-04-01', '1985-12-10', 'Licenciada en Derecho', 4, 8),
('567890123H', 'Diego Sánchez', 'Calle Grande 20 28005 Madrid', 2400.0, 910000004, '2017-05-01', '1992-03-25', 'Ingeniero Industrial', 5, 11),
('678901234J', 'Ana Martínez', 'Calle Peatonal 7 28006 Madrid', 2800.0, 910000005, '2016-06-01', '1996-09-05', 'Licenciada en Historia del Arte', 6, 10),
('789012345R', 'Jorge Hernández', 'Calle Comercial 8 28007 Madrid', 2000.0, 910000006, '2015-07-01', '1991-01-30', 'Diplomado en Turismo', 7, 9),
('890123456Q', 'Sofía González', 'Calle Principal 15 28008 Madrid', 2600.0, 910000007, '2014-08-01', '1988-05-12', 'Ingeniera de Caminos', 8, 14),
('901234567A', 'Manuel García', 'Calle Larga 12 28009 Madrid', 2300.0, 910000008, '2013-09-01', '1997-10-18', 'Licenciado en Derecho', 9, 17),
('012345678E', 'Laura Pérez', 'Calle Corta 2 28010 Madrid', 2800.0, 910000009, '2012-10-01', '1994-08-05', 'Ingeniera de Telecomunicaciones', 10, 6),
('345678901P', 'Luisa Pérez', 'Calle Mayor 10 28001 Madrid', 2500.50, 910123456, '2010-05-15', '1985-07-20', 'Licenciatura en Economía', 2, 4),
('234567890P', 'Carlos López', 'Avenida de la Luz 15 46005 Valencia', 2200.00, 960654321, '2008-11-01', '1982-01-10', 'Ingeniería Informática', 5, 8),
('123456789O', 'María Sánchez', 'Plaza Mayor 3 41001 Sevilla', 1800.75, 955987654, '2013-03-20', '1990-11-27', 'Grado en Derecho', 1, 3),
('987654321U', 'Javier García', 'Calle Alcalá 20 28009 Madrid', 2800.25, 912345678, '2006-06-10', '1980-04-05', 'Licenciatura en ADE', 1, 7),
('876543210Y', 'Ana Martínez', 'Calle Mayor 5 50001 Zaragoza', 2100.50, 976543210, '2015-09-01', '1995-08-17', 'Grado en Marketing', 2, 6),
('765432109M', 'David Rodríguez', 'Calle de la Estrella 8 28004 Madrid', 1900.00, 911234567, '2017-01-15', '1992-03-25', 'Ingeniería Industrial', 2, 9),
('654321098N', 'Marta Jiménez', 'Calle de la Rosa 12 29005 Málaga', 2300.75, 952345678, '2009-10-10', '1987-06-12', 'Grado en Psicología', 3, 2),
('543210987T', 'Pedro Gómez', 'Calle de la Paloma 6 41003 Sevilla', 1950.25, 955432109, '2014-07-01', '1991-12-08', 'Grado en Historia', 6, 5),

]

miCursor.executemany("INSERT INTO TrabajadoresAdministracion VALUES (?,?,?,?,?,?,?,?,?,?)", trabajadorAdministracion)

trabajadoresMantenimiento = [
('12345678A', 'Juan Pérez Gómez', 'Calle Mayor 1 28001 Madrid', 2000.00, 912345678, '2018-01-01', '1990-02-03', 'Licenciado en Administración de Empresas', 1, 5),
('23456789B', 'María Sánchez Martínez', 'Avenida de la Constitución 20 41001 Sevilla', 1500.50, 677889900, '2019-02-01', '1995-11-10', 'Diplomado en Relaciones Laborales', 2, 6),
('34567890C', 'Antonio García González', 'Calle Real 5 29001 Málaga', 1800.25, 655443322, '2015-04-01', '1985-06-15', 'Graduado en Marketing', 3, 14),
('45678901D', 'Ana Martínez Sánchez', 'Calle Mayor 10 30001 Murcia', 1900.75, 644332211, '2016-06-01', '1988-09-20', 'Licenciada en Derecho', 5, 4),
('56789012E', 'David González García', 'Calle de las Flores 2 28002 Madrid', 2100.00, 911223344, '2020-03-01', '1993-08-05', 'Ingeniero en Informática', 4, 16),
('67890123F', 'Marina López Hernández', 'Calle de la Libertad 15 46001 Valencia', 1700.50, 677889900, '2017-08-01', '1991-12-25', 'Técnica Superior en Administración y Finanzas', 1, 2),
('78901234G', 'Javier Sánchez Martínez', 'Calle Mayor 8 28001 Madrid', 2200.00, 912345678, '2014-01-01', '1980-07-30', 'Doctor en Economía', 5, 1),
('89012345H', 'Lucía Rodríguez Ruiz', 'Calle del Sol 4 41002 Sevilla', 1600.25, 655443322, '2013-09-01', '1983-05-08', 'Técnica en Recursos Humanos', 7, 3),
('90123456I', 'Miguel Torres Jiménez', 'Calle Real 10 29002 Málaga', 1950.75, 644332211, '2012-05-01', '1982-11-18', 'Ingeniero Industrial', 6, 5),

]

miCursor.executemany("INSERT INTO TrabajadoresMantenimiento VALUES (?,?,?,?,?,?,?,?,?)", trabajadorMantenimiento)

trabajadorEspectaculo = [
('12345678A', 'Ana García', 'Calle Mayor 23 28001 Madrid', 1500.0, 912345678, '2021-01-01', '1990-05-15', 'Licenciatura en Bellas Artes', 1),
('34567890C', 'María López', 'Calle San Miguel 5 41001 Sevilla', 1000.0, 955678901, '2018-03-30', '1995-07-20', 'Grado en Comunicación Audiovisual', 3),
('45678901D', 'Javier Rodríguez', 'Calle Valencia 8 46001 Valencia', 1300.0, 960123456, '2019-11-10', '1992-02-01', 'Grado en Bellas Artes', 4),
('56789012E', 'Marta Sánchez', 'Calle del Prado 34 28001 Madrid', 1500.0, 912345678, '2021-01-01', '1990-05-15', 'Licenciatura en Bellas Artes', 5),
('67890123F', 'Carlos Ruiz', 'Calle de la Feria 2 41001 Sevilla', 1100.0, 955678901, '2020-03-01', '1996-11-03', 'Diplomatura en Arte Dramático', 6),
('89012345H', 'Pedro Martínez', 'Calle de las Huertas 10 28001 Madrid', 1700.0, 912345678, '2018-09-23', '1988-01-10', 'Grado en Bellas Artes', 8),
('90123456I', 'Ana Belén García', 'Calle Sierpes 45 41001 Sevilla', 1200.0, 955678901, '2021-02-10', '1994-06-02', 'Licenciatura en Bellas Artes', 9),
('01234567J', 'Pablo Hernández', 'Calle del Arenal 8 28001 Madrid', 1300.0, 912345678, '2020-05-01', '1985-11-20', 'Diplomatura en Arte Dramático', 10)
]

miCursor.executemany("INSERT INTO TrabajadoresEspectaculo VALUES (?,?,?,?,?,?,?,?,?,?,?)", trabajadorEspectaculo)

hosteleros = [
('12345678A', 'Juan Perez', 'Calle Mayor 5 28001 Madrid', 1500.0, 912345678, '2020-01-01', '1990-05-10', 'Bachillerato', 1),
('23456789B', 'Maria Garcia', 'Calle Ancha 10 29002 Malaga', 1300.0, 623456789, '2019-05-12', '1992-03-22', 'FP Grado Medio', 2),
('34567890C', 'Pedro Rodriguez', 'Calle Estrecha 2 46001 Valencia', 1400.0, 634567890, '2018-11-15', '1995-09-05', 'FP Grado Superior', 3),
('45678901D', 'Ana Martinez', 'Calle Larga 20 41001 Sevilla', 1200.0, 745678901, '2017-09-22', '1993-12-31', 'Bachillerato', 1),
('56789012E', 'Jose Lopez', 'Calle Redonda 15 50001 Zaragoza', 1600.0, 856789012, '2016-07-07', '1989-07-18', 'Bachillerato', 4),
('67890123F', 'Lucia Fernandez', 'Calle Corta 7 15001 A Coruna', 1250.0, 967890123, '2015-06-04', '1991-10-15', 'FP Grado Medio', 2),
('78901234G', 'Hector Gomez', 'Calle Alta 3 48001 Bilbao', 1350.0, 178901234, '2014-04-03', '1988-02-27', 'FP Grado Superior', 5),
('89012345H', 'Sara Sanchez', 'Calle Baja 8 18001 Granada', 1100.0, 289012345, '2013-03-02', '1994-06-20', 'Bachillerato', 3)
]

miCursor.executemany("INSERT INTO Hosteleros VALUES (?,?,?,?,?,?,?,?,?)", hosteleros)

miConexion.commit()

miConexion.close()
