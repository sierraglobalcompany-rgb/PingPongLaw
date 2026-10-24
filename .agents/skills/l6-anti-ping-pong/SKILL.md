---
name: l6-anti-ping-pong
description: Ley 6. Detectar microdelegaciones y auditorías circulares; prioriza que ChatGPT decida e implemente directamente, y solo después delegue a Codex un lote autónomo y verificable.
---
# L6 — Antiping-pong: dirección ChatGPT, ejecución Codex cuando haga falta
**Canon:** `docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md` (L6).

## Prefiltro de realidad — responder, no formar otra lista infinita
1. ¿La acción todavía hace falta o está completa?
2. ¿Puede ChatGPT realizarla con acceso a GitHub, archivos, código, pruebas o herramientas disponibles? Si sí, **hacerla ahora**.
3. ¿Cuál es el cambio de decisión que traerá una auditoría o prueba? Si ninguno, no repetirla.
4. ¿La prueba es necesaria para continuar implementación, o solo para certificar entrega? Preservar aceptación sin bloquear lo independiente.
5. ¿Qué impide genuinamente ejecutar aquí lo restante? Precisar `LIMITACION_REAL`, no un supuesto.
6. ¿Se puede agrupar el resto en un lote seguro con criterio de cierre y sin nuevas consultas al usuario?

## Delegación mínima
Un contrato a Codex solo cuando lo justifique el entorno local, ejecución que ChatGPT no puede hacer o autorización explícita. Incluir objetivo, scope, no tocar, fuentes/SHAs, decisiones ya tomadas, plan completo, permiso táctico para corregir obstáculos recuperables, pruebas, riesgos y reporte final.
Codex puede resolver bloqueos técnicos recuperables, documentar bloqueos genuinos y continuar acciones independientes. No cambia alcance, negocio, permisos, base real, despliegue, contratos o UX aprobada sin permiso.
Prohibido reenviar automáticamente cada `NEXT` de Codex a ChatGPT y viceversa. Antes de otra delegación exigir nueva capacidad, dato, hipótesis o trabajo material pendiente, **no necesariamente SHA nuevo**.
**Salida:** `HECHO_CHATGPT | LIMITACION_REAL | NECESITA_CODEX | MOTIVO_AUDITORIA | RESULTADO | NEXT/NINGUNO` en formato conciso.
