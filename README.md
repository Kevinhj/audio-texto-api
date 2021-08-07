# Audio Texto Scripts

El trabajo acá desarrollado pretende presentar una solución para el proyecto final de Tecnología de Base de Datos, 

El operador utilizando un aplicativo interno de la universidad, guarda el archivo con el siguiente formato:
`dniOperador_dniCliente-dia-mes-año hora`
`206580985_207850699-08-07-2021 20:02:21.550`

Tambien, el operador con el aplicativo interno cuando recibe la llamada, selecciona el motivo de la llamada o chat, 
informacion(horario de cursos, oficinals), matriculas, cobros(letras de cambio pendientes de pago), etc con base en eso; dicho audio o chat es almacenado en una carpeta de unprocessed_audio/subcarpeta_tipo_interaccion

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

Tareas pendientes por desarrollar:
- [ ] Almacenar en una estructura los audios para iterar sobre ellos
- [ ] Depende el folder en el que este, va a llevar associado un id de catalogoInteraccion