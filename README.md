# Audio Texto Scripts

El trabajo acá desarrollado pretende presentar una solución para el proyecto final de Tecnología de Base de Datos, 

El operador utilizando un aplicativo interno de la universidad, guarda el archivo con el siguiente formato:
`dniOperador_dniCliente-dia-mes-año hora`
`206580985_207850699-08-07-2021 20:02:21.550`

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
- [ ] Almacenar en una estructura(dictionary) los audios de cada carpeta para iterar sobre ellos
- [ ] Depende el folder en el que este(cobro, informacion, matricula), va a llevar associado un id de catalogoInteraccion
- [ ] Depende el folder padre va a tener un id de medio de interacion asociado(llamada, chat)
- [ ] Para Llamada: Procesar el audio a texto y aplicar el analisis de sentimiento
- [ ] Para Chat: Aplicar analisis de sentimiento a los chats
- [ ] Dado el nombre de el archivo(audio, chat) consultar la base de datos, para obtener el id de el operador y el cliente
- [ ] Realizar el insert en tbInteracciones y retornar el id de la interacción
- [ ] Con el id de la interaccion realizar el insert en tbSentimientsInteracciones
- [ ] Refactor
- [ ] Tests