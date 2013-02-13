SkypeTalking
Versión 0.8
Copyright (c) 2010 Equipo SkypeTalking
Sitio web del proyecto: http://skypetalking.googlecode.com

1. Introducción

SkypeTalking es una utilidad que hace que Skype, un popular programa de telefonía de Internet haga más fácil el acceso a los ciego. Utiliza  la
API de Skype  y utiliza el lectores de pantalla y la salida en braille para obtener información de Skype y enviar esa información a su lector de pantalla. SkypeTalking
anunciará la mayoría de las alertas de Skype, incluyendo cambios de estado del usuario, entrada y salida de mensajes de chat, estados de llamada, y mucho
más! En resumen, SkypeTalking simplemente hará que Skype hable  por usted!
SkypeTalking fue desarrollado principalmente para NVDA, un lector de pantalla libre y abierto, para permitir el acceso  más NVDA a la aplicación de Skype.
Sin embargo, también apoyará JAWS, Window-Eyes, System Access y voces  SAPI5, aunque con SAPI5 no tendrá el soporte de braille.

1.1. Requisitos del sistema

Para utilizar SkypeTalking con éxito, se necesita lo siguiente:
* Windows 2000, XP, Vista o 7
* Cualquier lector de pantalla de apoyo: Actualmente los tipos soportados son los lectores de pantalla NVDA 2010.1 o posterior, JAWS (cualquier versión),
Window-Eyes (cualquier versión) o System Access (cualquier versión), incluyendo 
System Access to Go.
* Si usted no utiliza ninguno de los lectores de pantalla compatibles, una  voz SAPI5 se utilizará en su lugar. En tal caso, usted debe tener las voces
SAPI5 compatible (sistemas de Windows cuentan con al menos una voz SAPI5 instalada)
* Y, por supuesto, la aplicación cliente de Skype (3.x, 4.x o posterior) - es probable que funcione con Skype 2.x y posiblemente con 1.x, aunque no he probado.

2. Cómo utilizar

2.1. Instalación y primera ejecución

Para instalar SkypeTalking, inicie SkypeTalking_setup.exe y siga las instrucciones. La instalación creará un icono en el escritorio, un grupo de programas
en el menú de inicio, y la carpeta de instalación se encuentran en x: \ SkypeTalking donde x es la letra de unidad del sistema.
Para desinstalar SkypeTalking, usted puede hacer esto mediante la apertura de grupo SkypeTalking programa en el menú Inicio y seleccione Desinstalar SkypeTalking.
Para iniciar SkypeTalking, haga clic en el icono SkypeTalking ya sea desde su escritorio o SkypeTalking entrada en un menú de inicio de los programas \
SkypeTalking.
Al iniciar SkypeTalking por primera vez, será probablemente no autorizado a comunicarse con la aplicación Skype. Por razones de seguridad, Skype no permite
la activación de cualquier  tercera parte  de plugins   y extras para comunicarse con él sin permiso del usuario. Esto es para evitar que los virus y troyanos dañen Skype. Para
permitir el acceso SkypeTalking de Skype, haga lo siguiente:
1. Lanzar SkypeTalking, ya sea desde el escritorio o desde el menú de inicio bajo Programas> SkypeTalking. Que aquí deben "conectarse a Skype".
2. Abrir Skype .
3. Ir a la barra de menú, seleccione Herramientas y, a continuación flecha hacia arriba a las opciones y pulse Intro.
4. Flecha hacia abajo para la categoría opciones avanzadas.
5. Pulse Shift + Tabulador varias veces hasta que caes en 
enlace "Administrar el acceso de otros programas a skype."
Presione la barra espaciadora para activarlo.
o Dan enter en ese enlace.
6. debe aparecer un cuadro de edición, que dice skypetalking.exe, en una lista (debe ser por lo general un primer elemento), Tabulan una vez para ir al botón Cambiar y presione la barra espaciadora para activarlo.
7. Presiona tab. Usted debe saber que se le coloca en un botón de radio que dice 
"No permitir el acceso a este programa a Skype". Flecha hacia arriba
hasta que escuche 
"Permitir el acceso a este programa a Skype" y presione Intro.
8. Voila! Usted acaba de permitir a SkypeTalking usar Skype! SkypeTalking ahora debe anunciar el mensaje de bienvenida. Ahora puede pulsar varias veces
Escape para salir de las opciones. Incluso no es necesario salvarlos.
Tenga en cuenta, tendrá que repetir estos pasos cada vez que vuelve a instalar SkypeTalking, pero no te preocupes, tienes que hacerlo sólo una vez por
cada nueva instalación de SkypeTalking . Usted también tendrá que hacerlo si hay un cambio en la ubicación del archivo SkypeTalking.exe.

2.2. Cómo utilizar

Una vez lanzado, SkypeTalking se ejecutará en un fondo y leer en voz alta las alertas hasta que lo cierre.
SkypeTalking tiene varios comandos asociados con los métodos abreviados de teclado que puede utilizar para controlar el comportamiento de SkypeTalking
y obtener alguna información repetida o hablado. Todos los atajos de teclado son SkypeTalking en combinación con Alt, Ctrl y Shift (Alt+Ctrl+SHIFT+Algo).
Por lo tanto podemos decir que Alt Ctrl Shift actua como un modificador SkypeTalking. Así que para ejecutar un comando, se mantiene Alt Ctrl + Shift (modificador SkypeTalking) y pulse cualquier tecla mientras se mantiene pulsado estas trez teclas.
Nota: Puede modificar todos los métodos abreviados de teclado SkypeTalking a su gusto mediante la apertura de SkypeTalking.ini archivo ubicado en el directorio SkypeTalking, sin embargo se recomienda sólo para usuarios avanzados en este momento.
En las secciones siguientes se describen todos los comandos SkypeTalking y cómo usarlos.

3. Los comandos

3.1. Lectura de mensajes de chat de Skype

3.1.1. Habla los últimos 10  mensajes entrantes / salientes de chat (Alt+Ctrl+Shift+Números 1 a 0)

Mediante el uso de Alt+Ctrl+Shift +Números 1 a 0 en un teclado alfanumérico, puede leer última entrada y salida de mensajes de chat (del 1 al 10) que
ha recibido o enviado durante la sesión SkypeTalking. Si se pulsa dos veces, una copia del mensaje asociado a ese número ira al portapapeles. Si se presiona
tres veces, se abrirá una dirección URL en el navegador web por defecto (si el mensaje contiene una dirección URL).

3.1.2. Vigilancia activa chats (Alt+Ctrl+Shift+Teclas de función F1 a F10)

Esta característica le permite monitorear conversaciones activas, es decir, abrir ventanas de chat. Esto es útil si usted desea revisar sólo últimos 10
mensajes de chat que están asociados a un determinado chat, chats, y no todos juntos. Utilice Alt Ctrl + Shift teclas de función F1 a F10 para configurar
monitor a la una de hasta 10 chats activos (o pulse dos veces para concentrar la atención a la ventana de chat), y entonces usted puede usar Alt Ctrl +
Shift Números para la lectura últimos 10 mensajes actualmente de chat supervisadas. Presionando Alt Ctrl + Shift C dará a conocer la actualidad de chat
supervisadas, y pulsando dos veces a concentrar la atención a la ventana de chat.

3.1.3. Repetir el último mensaje de chat (Alt Ctrl+Shift+R)

Este comando repite el último mensaje entrante o saliente de chat. Si se pulsa dos veces, se abrirá una ventana de chat de Skype asociadas con ese mensaje,
y también establecerá monitor de la charla a la misma.

3.2. Repetir el último evento (Alt+Ctrl+Shift+E)

Este comando  es para repitir el último evento Skype incluyendo mensajes de chat. Los acontecimientos que se puede repetir utilizando este comando incluyen cambios
de estado, el último mensaje de chat y los estados de llamada.

3.3. Ignorar los  eventos  de Skype bascular(Alt+Ctrl+Shift+I) 

Este comando cambiará haciendo caso omiso de todos los eventos de Skype. Cuando esté activado, SkypeTalking simplemente ignora los acontecimientos y no
no los hablará o no podra grabarlas.

3.4. Cambia tu estado de Skype al vuelo (Alt+Ctrl+Shift+tecla de Retroceso)

Utilice este comando para cambiar su estado de Skype al vuelo entre conectado, ausente, no disponible, no molestar, etc Su estado se cambi´á después
de un segundo de soltar el comando.

3.5. Decir duración de la llamada (Alt+Ctrl+Shift+D)

Este comando funciona durante una llamada de Skype, y el informa de la duración de la llamada actual en horas, minutos y segundos.

3.6. Decir estado de la transferencia de archivos actual (Alt+Ctrl+Shift+F)

Este comando nos anuncia el estado de la transferencia del  archivos  ya última entrada o salida. Si la transferencia de archivos actual está en curso, también
se escuchará la velocidad de transferencia actual en megabytes por segundo, y el número de megabytes que actualmente se están transfiriendo.

3.7. El informe de su estado actual en línea o saldo acreedor (Alt+Ctrl+Shift+O)

Este comando cuando se pulsa una vez, nos dice  el estado de conexión actual, y si se pulsa dos veces nos dice el saldo actual de nuestro crédito de Skype.

3.8. Informe o cambia tu estado de ánimo de Skype de texto (Alt+Ctrl+Shift+M)

Este comando nos dice el actual estado de ánimo de texto de su Skype enel caso  que se 
establece. Si se pulsa dos veces, se abrirá un cuadro de diálogo que
le permite introducir un nuevo texto del estado de ánimo. A continuación, puede introducir un texto nuevo, y entonces usted puede simplemente pulsar Intro
cuando haya terminado. Su estado de ánimo de texto será cambiado.

3.9. Otros comandos

3.9.1. El cuadro de diálogo Acerca de SkypeTalking (Alt+Ctrl+ Shift+A)

Este cuadro de diálogo muestra la versión actual de SkypeTalking, la información de copyright, la información del sitio web etc, Usted puede cerrar esta ventana pulsando
enter.

3.9.2. Informe de la versión de Skype (Alt+Ctrl+Shift+V)

Este comando nos dice la versión  que está ejecutando de Skype instalado en el ordenador del usuario. Si se pulsa dos veces, nos dice la versión de la API Skype 
(sobre todo útil para los desarrolladores).

3.9.3.  Parar voz SAPI5 (Alt+Ctrl+Shift+Barra espaciadora)

Este comando detendrá la voz cuando habla SkypeTalking, esté se utiliza con la voz SAPI5. Si estás utilizando SkypeTalking con su lector de pantalla, usted
puede parar la voz como de costumbre, presionando la tecla Ctrl.

3.9.4. Salir SkypeTalking (Alt+Ctrl+Shift+Q)

Este comando descarga SkypeTalking de la memoria. De forma predeterminada, se le pedirá confirmación. Si su respuesta es Sí, SkypeTalking se descarga,
y cualquier evento pasado, la transferencia de archivos actuales y mensajes de chat será olvidado desde SkypeTalking los mantiene en la memoria del equipo
y por lo tanto se eliminan de la memoria una vez SkypeTalking se descarga. Si su respuesta es No, SkypeTalking seguirá trabajando en él es actual período
de sesiones.

4. El diálogo de Configuración

el diálogo de configuración SkypeTalking se puede invocar pulsando Alt+Ctrl+Shift+P 
(de preferencias). Se puede utilizar para cambiar el comportamiento de
SkypeTalking, y también su lengua que viene por defecto y la salida de voz.
El diálogo de configuración tiene tres pestañas (General, de salida y alertas) que se puede cambiar mediante el uso de las teclas estándares de Windows es decir,  pulsando las teclas Ctrl+Tab 
o pulsando las teclas Ctrl+Shift+Tab 

4.1. pestaña General

La pestaña General de SkypeTalking que se encuentra en el diálogo  de configuración tiene las siguientes opciones.

4.1.1. El lenguaje

El lenguaje cuadro combinado muestra todos los idiomas disponibles que son compatibles actualmente con SkypeTalking. Aquí usted puede elegir su idioma
preferido, y se aplica inmediatamente después de guardar la configuración. De forma predeterminada, SkypeTalking utiliza el lenguaje utilizado por el sistema
operativo.

4.1.2. Inicio automático de Skype si no se ejecuta

Esta opción en caso que esté la casilla verificada permitirá a SkypeTalking para lanzar automáticamente el programa Skype para usted si se olvida de poner en marcha antes de ejecutar Skypecon SkypeTalking. Esto también es útil si desea ejecutar Skype y tener un acceso instantáneo a los anuncios de Skype. Esta opción está activada de forma predeterminada,
lo que significa que SkypeTalking cargará Skype si detecta que Skype no se está ejecutando.

4.1.3. Confirmar al salir SkypeTalking

Esta opción está activada de forma predeterminada. Si se desactiva, SkypeTalking se descargará inmediatamente tan pronto como se emite el comando Salir
y el mensaje de confirmación se omiten.

4.1.4. Al salir de SkypeTalking, también se sale de Skype

Esta opción esta en  auto-descripción. Está marcada por defecto, lo que significa que al salir de SkypeTalking, también descargara Skype para usted. Sin embargo,
si desea seguir utilizando Skype después de salir de SkypeTalking sin descargar Skype, es probable que desee desactivar esta opción.

4.2. Pestaña Salida

La pestaña de salida contiene los ajustes relacionados con la salida de la voz y la salida en braille. Aquí se pueden establecer las siguientes opciones.

4.2.1. Voz de salida

La caja de salida de voz combo que permite ajustar su salida de voz preferida. Si selecciona Auto Detect, que detecta automáticamente y utilizar el lector
de pantalla en ejecución, o SAPI5 si su lector de pantalla no se está ejecutando o no por SkypeTalking. Si se establece en SAPI5, automáticamente usará
una voz SAPI5 y no hará caso de su lector de pantalla.

4.2.2. Velocidad de voz SAPI5

Los 3 siguientes controles que se encuentran en un cuadro de edición  con las que usted puede controlar el volumen y tipo de voz de su sintetizador SAPI5 en el caso cuando
se utiliza SAPI5. Usted puede utilizar las teclas de flecha para ajustar los valores o escriba un número deseado.

4.2.3. Habilitar salida Braille

Esta casilla de verificación le permite decidir que le gustaría ver SkypeTalking de salida en la pantalla en braille. Esta opción no funciona con SAPI5.

4.3. Pestaña de las alertas

Esta pestaña le permite activar y desactivar los anuncios de varias alertas de Skype en la actualidad con el apoyo de SkypeTalking. Cualquier cosa sin marcar
aquí será ignorado por SkypeTalking. Puede cambiar los anuncios de los chats entrantes, salientes chats, los estados de línea, etc

5. El Administrador de Contactos

El Administrador de Contactos de SkypeTalking le permite ver y gestionar tus contactos de Skype en una manera fácil y accesible. Puede acceder a ella pulsando el atajo de teclado 
Alt+Ctrl+Shift+F11 del teclado. Si se pulsa dos veces este comando, SkypeTalking se centrará en el foco de la ventana original de la lista de los contactos Skype. 

5.1. Navegando Administrador de Contactos

El Administrador de Contactos SkypeTalking muestra los contactos en una lista de selección de caja múltiple , lo que le permite seleccionar uno o más contactos a
realizar algunas acciones en. Utiliza las teclas de flecha para navegar entre tus contactos, y utiliza la barra espaciadora para alternar en contacto con la
actualidad centrada entre seleccionados y no seleccionados. El Administrador de Contactos también muestra el estado de los contactos, el texto del estado
de ánimo, y la última fecha y la hora de ver los contactos en línea.

5.2. Elegir un recurso de contacto seleccionado

¿Qué acciones se muestra en Administrador de Contactos depende del número de contactos seleccionados.
Si no hay contactos se seleccionan, SkypeTalking nos anuncia un mensaje de advertencia.
Si sólo se selecciona un contacto, las siguientes acciones están disponibles:
1. Botón de llamada - realiza una llamada de Skype para el contacto seleccionado - Este es el botón predeterminado, por lo que pulsar Intro cuando se centra
en una lista de contactos, éste se activa
2. Botón Chat  - Abre una ventana de chat con el contacto seleccionado
3. Perfil - Abre un visor de perfiles de Administrador de Contactos
Si los contactos de dos o más están seleccionados, las acciones disponibles son las siguientes:
1. Botón Crear Conferencia - Crea una conferencia con todos los contactos seleccionados - Este es el botón predeterminado, por lo que al pulsar Intro cuando
se centra en una lista de contactos, éste se activa
2.  Botón Crear multi-chat abre una ventana de chat y crea un multichat con todos los contactos seleccionados
Usted puede utilizar el tabulador y las teclas Shift+Tabulador para navegar entre las acciones y una lista de contactos. Pulse la tecla Esc o activar
el botón Cancelar en cualquier momento para cerrar el Administrador de Contactos.

5.3. El Visor de perfil

El Visor de perfil es una parte del Administrador de Contactos que se abrirá cuando se activa el botón Ver perfil de un contacto individual. Se muestra
el perfil de los detalles del contacto seleccionado en un formato accesible y fácil de usar cuadro de diálogo. Utilice Tab y Shift+Tab para mover la ficha
de detalle a detalle, y entonces usted puede usar las teclas de flecha y la selección de todos los comandos de texto estándar de copiar algún detalle en
particular si lo desea. Para cerrar el Visor de perfil, active el botón Cancelar o presione Escape para volver al Administrador de Contactos.

6. Envío y recepción de mensajes SMS con SkypeTalking

SkypeTalking le permite enviar y recibir mensajes SMS en una forma fácil con su asistente integrado SMS.

6.1. El Asistente para SMS

Usted puede tener acceso con el Asistente  SMS pulsando Alt+Ctrl+Shift+S.

Una vez abierto, se le pedirá que introduzca un número de teléfono. Debe introducir un número de teléfono válido aquí, incluyendo un código de país. Por
ejemplo: 11234567. Si el número no es válido, se vuelve de nuevo al campo de número de teléfono para  volver hacer una nueva tentativa entrando de nuevo un número. Pulse Intro
para continuar, o presione Escape para cancelar.
Si el número de teléfono era válido, el asistente continuará y se le colocará en un área de edición donde se debe redactar el mensaje SMS. Mientras que
en este cuadro de diálogo, puede pulsar la tecla de función F2 en cualquier momento para obtener el estado actual de sus mensajes SMS 
que está componiendo. Un pitido de aviso se escuchará en el caso cuando el número de caracteres que quedan en un mensaje llega a 0.
Una vez que haya compuesto el mensaje SMS, puede pulsar Tab para ir al botón Enviar y hacer Intro para enviarlo o el botón Cancelar para cancelar el envío. Si el botón
Enviar se activa, y el saldo de su crédito es bueno, el SMS se envió.

7. la información final y los datos de contacto

7.1. La obtención de un código fuente

SkypeTalking es software libre y de código abierto, escrito en un lenguaje de programación Python disponible en www.python.org. El código abierto significa
que el código fuente del software está disponible para cualquiera que lo desee. SkypeTalking usa GNU Licencia Pública General versión 2.0. Usted puede
leer la licencia completa en el archivo license.txt que viene con SkypeTalking.
Si usted es un programador, o si desea contribuir a un código fuente o se puede ejecutar SkypeTalking directamente desde la fuente, se puede visitar un
repositorio SVN de SkypeTalking que se encuentran en
http://skypetalking.googlecode.com
sitio del proyecto web. Allí también se puede descargar la última versión.

7.2. Contribuir con una traducción

Si usted es un traductor y quieres localizar SkypeTalking y la documentación en su propio idioma, puede ponerse en contacto conmigo vía un e-mail en inglés para recibir
las últimas novedades de archivo de idioma y las instrucciones para que luego me puedá enviar de vuelta sus traducciones. También si usted tiene algún
conocimiento de la subversión usando repositorio, estaré encantado de darle los derechos de acceso para actualizar la traducción de vez en cuando.

7.3. La lista de correo SkypeTalking

Usted puede unirse a  la lista de SkypeTalking escribiendo al correo  que esta alojado en los Grupos de Google utilizando la siguiente dirección: subscribe@googlegroups.com skypetalking.
Para enviar un correo electrónico a la lista de discusión de SkypeTalking utilice la dirección skypetalking@googlegroups.com Tenga en cuenta que esta lista sólo es en  Inglés hablante.

Este es el mejor recurso para obtener apoyo técnico y varios consejos y trucos sobre SkypeTalking. Aquí también recibirá una información diaria sobre
lo que está pasando con SkypeTalking en  desarrollo  de repositorio. Todas las preguntas son bienvenidas, desde las preguntas  de los principiante hasta las preguntas   de los avanzado.

7.4. Créditos

Las siguientes personas han contribuido al desarrollo de SkypeTalking de alguna manera:
- Hrvoje Katiæ, que es el tipo principal del proyecto SkypeTalking .
- Gianluca Casalino, quien ha desarrollado diversas funciones avanzadas de SkypeTalking, y ha contribuido mucho al trabajo para los códigos SkypeTalking. Gracias
a su dedicación y ayuda, SkypeTalking es aún mucho mejor que antes!
- René Linke, que también contribuye a SkypeTalking de alguna manera mediante la creación de parches y dando ideas iniciales.
- Varias gentes relajadas  que han hecho SkypeTalking disponibles en sus propios idiomas, por lo que SkypeTalking ahora habla más de 15 idiomas!
- Y, por supuesto, todos los usuarios de todo el mundo que están utilizando SkypeTalking en una base diaria y hacen su promoción para que la gente más sepa  
acerca de este producto!
Muchas gracias a todos Ustedes!

7.5. Mi información para ponerse en contacto

Mi E-Mail para preguntas, sugerencias, apoyo y anunciar una traducción : hrvojekatic@gmail.com
Me puedes seguir en Twitter en: www.twitter.com / hkatic
Mi página de Facebook: www.facebook.com/jukebox2009
Mi Id Klango en klango.net: DJ_Jukebox
Mi dirección de MSN: hrkatic@hotmail.com
Mi Skype: hrvojekatic

Fin del documento.