---
title: Proceso de gestión de respuestas a solicitudes de juzgados
date: septiembre 01 de 2023
author: Javier Sanchez Toledano
---

# Objetivo

El objetivo de la gestión de respuestas es controlar el
flujo de trabajo de las solicitudes de información
realizadas por los juzgados y por particulares, para 
mejorar la velocidad con la que se atienden sin 
menoscabo de la seguridad.

```{.plantuml caption="Diagrama UML del proceso" width=50%}
@startuml
actor "Solicitante" as sol
actor "Junta Local" as jl
participant "Sistema" as sis
control "Conteo\nRegresivo" as cr
database "Bitácora" as log

sol -> jl: Recibe solicitud
jl -> sis: Registra solicitud
sis -> cr: Activa conteo regresivo
sis -> log: Registra eventos
jl -> sis: Registra respuesta
sis -> sis: Encripta respuesta
sis -> sol: Envia UUID
sis -> sol: Enviar contraseña
sis -> cr: Detiene conteo regresivo
sol -> sis: Recibe UUID y entrega\narchivo encriptado
@enduml
```