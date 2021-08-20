# Audio Texto Scripts

El trabajo acá desarrollado pretende presentar una solución para el proyecto final de Tecnología de Base de Datos, 

El operador utilizando un aplicativo interno de la universidad, guarda el archivo con el siguiente formato:
`dniOperador_dniCliente_año-mes-dia hora-minutos-segundos`
`303090138_303250244_2021-07-27 07-55-25.wav`

Ademas, el operador con el aplicativo interno cuando recibe la llamada, selecciona el motivo de la llamada o chat, 
informacion(horario de cursos, oficinals), matriculas, cobros(letras de cambio pendientes de pago), etc con base en eso; 
dicho audio o chat es almacenado en una carpeta de unprocessed_audio/subcarpeta_tipo_interaccion

```
├───unprocessed_interactions
│   ├───audio
│   │   ├───cobro
│   │   ├───informacion
│   │   └───matricula
│   └───chat
│       ├───cobro
│       ├───informacion
│       └───matricula
```

Tareas necesarias para realizar la implementación:
- [x] Almacenar en un list los audios de cada carpeta para iterar sobre ellos
- [x] Depende de el folder en el que este(cobro, informacion, matricula), va a llevar associado un id de catalogoInteraccion
- [x] Depende de el folder padre va a tener un id de medio de interacion asociado(llamada, chat)
- [x] Para Llamada: Procesar el audio a texto y aplicar el analisis de sentimiento
- [ ] Para Chat: Aplicar analisis de sentimiento a los chats
- [x] Crear un procedimiento almacenado que realice el insert en tbInteracciones
- [x] El procedimiento almacenado consulta el id de el cliente y el operador, realizar el insert y retornar el id de la interacción
- [ ] Crear un procedimiento almacenado que realice el insert en tbSentimientoInteracciones
- [ ] Con el id de la interaccion realizar el insert en tbSentimientsInteracciones
- [ ] Refactor
- [ ] Crear el .bat para ejecutar los scripts
- [ ] Tests