# Inicio para ChatGPT: activar PingPongLaw con evidencia

## Cómo invocarlo en cualquier chat

> **Aplica PingPongLaw al proyecto o prompt que te indique. Primero abre el canon del repositorio PingPongLaw y comprueba sus seis leyes. Actúa como director técnico: ejecuta lo que permitan tus herramientas, audita solamente lo necesario y usa Codex para el trabajo que no puedas realizar. No hagas ping-pong, no inventes PASS y entrega NEXT o NINGUNO.**

Origen a consultar: https://github.com/sierraglobalcompany-rgb/PingPongLaw y el archivo docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md en el SHA aplicable.

**Advertencia:** la presencia de este archivo o AGENTS.md en GitHub no significa que ChatGPT haya leído las leyes automáticamente. Consultarlas mediante la conexión GitHub o adjuntar la copia vigente. Si no se puede acceder, registrar CANON_NO_LEIDO y NO inventar versión/instalación.

## Router de intención — una sola ruta, sin dos auditorías automáticas

| El usuario dice | Modo | Resultado |
|---|---|---|
| Revisa este prompt | PROMPT | Contrastarlo con objetivo y L1–L6, corregir contradicciones materiales; un prompt final o SIN_CAMBIOS |
| Continúa / implementa | EJECUCION | ChatGPT hace lectura, diseño, edición y tests accesibles; Codex solo el residuo ejecutable local coherente |
| Revisa el repositorio | AUDITORIA_FOCAL o FORENSE | Si pide todo: SHA fijo, inventario y 20/24 dimensiones según maestro indicado, informe por cobertura real; si pide un fallo: focal |
| Audita el diseño | DISENO | SPEC/mockup → Anti UI Slop → UI UX Pro Max → pruebas/render reales por rol/estado/viewport |
| Verifica entrega de Codex | L5 | Confrontar reporte, diff, CI, artefactos, SHA y tests; no reemitir su NEXT automáticamente |
| Instala o actualiza las leyes | REGLAS | Verificar canon, AGENTS, conflictos, permisos; diff mínimo en repo autorizado, comprobar lectura real y publicación |

## Selección de skills antes de trabajar

Consultar [arquitectura de skills](SKILLS_ARQUITECTURA.md). Tras abrir el canon, usar `.agents/skills/pingponglaw/SKILL.md` para elegir solamente la ley aplicable. Cada ley tiene su skill; diseño usa dos adaptadores externos cuando aportan evidencia, y no dos auditorías completas por rutina. La lectura desde GitHub debe ser real, no inferida. Una skill documentada NO garantiza que el plugin esté instalado.

## Cinco preguntas previas — sin burocracia

1. ¿Es necesaria esta tarea o ya está completa?
2. ¿ChatGPT puede hacer el trabajo directamente y qué parte ya hizo? No delegar por costumbre.
3. ¿Qué riesgo concreto resolvería una prueba o auditoría nueva? Si no cambia decisión, no repetir.
4. ¿Cuál es la menor solución completa y segura conforme a Ponytail, con consumidores y regresiones?
5. ¿Qué evidencia concreta certifica aceptación y qué queda sin probar?

## Propiedad de resultados

ChatGPT decide producto, arquitectura, alcance y pruebas; ejecuta lo que realmente puede hacer. Codex recibe un lote coherente (preflight → diagnóstico → implementación autorizada → regresión → reporte), con libertad táctica en obstáculos A recuperables y continuidad frente a bloqueos B independientes. Contratos/roles/permisos/migraciones/despliegues requieren autorización. Un informe del ejecutor no equivale a L5 aprobada.

Formato compacto si hace falta: MODO | REPO/SHA | LEYES_L1_L6 | HECHO_CHATGPT | QA_REAL | BLOQUEOS | JUSTIFICACION_CODEX | NEXT/NINGUNO.

## Caso de verificación de F2

- T1: solicitar revisión de un prompt innecesariamente extenso; no convertirlo en otro ciclo de 10 pasadas si está claro.
- T2: resolver una tarea pequeña en un repositorio GitHub al que ChatGPT tenga acceso, manteniendo contrato y pruebas necesarias.
- T3: comparar una entrega de Codex con evidencias SHA y marcar NOT_RUN cuando falta captura/test.

El éxito de T1–T3 se reporta con acciones verificables; este documento no declara que las pruebas se hayan ejecutado.
