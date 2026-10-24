# PingPongLaw — ROADMAP por fases con compuertas de aceptación

**Meta:** un sistema mínimo, compartido y verificable de seis leyes que ChatGPT lee desde GitHub y Codex utiliza con su skill; Ponytail 5.3.2 fortalece L1. No es una app SaaS, no requiere BD, frontend ni backend propios. Por Ley 2 no se construyen dashboards de gobierno sin necesidad demostrada.

| Fase | Qué se hace y quién | Criterio de cierre | Estado inicial |
|---|---|---|---|
| **F0. Fuente y riesgos** | ChatGPT: comprobar PingPongLaw, Ponytail oficial, SHA, MIT, instalación Codex y límites de hooks | Identidad/fuente/SHA registrados y decisiones sobre integración | HECHO: investigación documental |
| **F1. Canon universal** | ChatGPT: publicar README, AGENTS, L1–L6, skill adaptada, guías y roadmap en rama revisable | Los seis textos están presentes y unidos sin duplicar; diff verificable, sin datos ni scripts ejecutados | EN PREPARACIÓN / rama de trabajo |
| **F2. Uso real desde ChatGPT** | ChatGPT: consultar versión exacta del canon por GitHub y aplicar a casos concretos | 3 pilotos: revisión de prompt sin auditoría extra; cambio técnico focal; evaluación de entrega; evidencias de fuente y salida | PENDIENTE |
| **F3. Instalación global en Codex local** | Codex en PC: preflight CLI/Node, fuente oficial, instalar plugin, revisar y autorizar hooks, reiniciar sesión | Identidad y versión verificadas, skills visibles, hooks aprobados conscientemente, prueba de invocación, informe MD y ZIP si hay anexos | PENDIENTE acceso al PC |
| **F4. Piloto en 1 proyecto** | ChatGPT + Codex: reconciliar AlquilaPro u otro repo representativo y el PR previo de Ley 1 sin duplicar AGENTS | PR/ruta correctos, prueba de lectura y flujo completo, QA focal, sin romper reglas propias | PENDIENTE |
| **F5. Propagación controlada** | ChatGPT en GitHub: comprobar base/branch e instrucciones de cada repositorio; preparar cambios mínimos por repo | Matriz CANON_VERIFICADO / EN_PR / INSTALADO / CONFLICTO / SIN_ACCESO; sin merges automáticos | PENDIENTE |
| **F6. Auditoría de impacto y mantenimiento** | Solo cuando una razón concreta lo justifique: comparar cambios, ahorro real y regresiones; registrar upgrades upstream por SHA | Métricas de 2-3 casos comparables, no benchmarks extrapolados; 0 ciclos de auditoría sin finalidad | PENDIENTE |

## Responsables y autorización

- ChatGPT es dueño del plan, el diagnóstico, la elección técnica y todo lo que sus herramientas puedan ejecutar. Codex solo es necesario para instalación en el PC, herramientas nativas o acciones no accesibles a ChatGPT.
- La instalación del plugin Ponytail oficial puede instalar código ejecutable Node en hooks. **No aceptar hooks por defecto**, revisarlos y autorizarlos por separado en una sesión local consciente.
- Las modificaciones remotas de aplicaciones distintas de PingPongLaw, merge, deploy y cambios de seguridad exigen alcance/permiso específico. Los 14 PRs Ponytail creados previamente en repos de aplicaciones no están fusionados y deben reconciliarse en F4/F5.

## Gates comprobables

**G0**: upstream Ponytail `09c434ab73ca43761c5d8b0c5d341926c2fba710`, versión 5.3.2, MIT, límites del benchmark y del plugin documentados.

**G1**: PingPongLaw contiene 6 leyes canónicas, AGENTS apunta a ruta existente, skill con frontmatter válido, README enlaza documentación, sin otras leyes inventadas. Comprobar SHA/árbol y diff antes del merge. El PR no equivale a instalación local.

**G2**: ChatGPT lee el canon remoto realmente cuando el usuario lo solicita; si no hay acceso, declara NO_LEIDO. No asumir carga automática.

**G3**: un Codex en el equipo usuario comprueba CLI, Node, plugin instalado y prueba invocación. La configuración/trust de hooks ha sido confirmada en esa instancia; si no, HOOKS_NOT_VERIFIED.

**G4**: cada proyecto piloto conserva sus AGENTS/SPEC/datos/pruebas y no recibe scripts globales copiados a su código.

**G5**: para expandir, matriz por repositorio y comparación base/HEAD; no tocar ramas concurrentes ni hacer merges silenciosos.

**G6**: medir simplicidad con diff y contratos intactos, no solo reducción de líneas. Un cambio menor que rompa seguridad, accesibilidad o funcionalidades NO cumple Ley 1.

## Política de selección de auditorías

1. Sin auditoría adicional para tareas pequeñas con contrato claro y QA focal suficiente.
2. Revisar diff con Ponytail Review cuando haya riesgo o solicitud: leer consumidores fuera del diff.
3. Ponytail Audit para diagnóstico amplio cuando se solicita o hay riesgo sistémico. Su límite de presentación de 20 hallazgos **no permite ocultar P0/P1** de una forense más exhaustiva.
4. Auditoría forense L1–L6 solo cuando usuario o riesgo alto lo justifican. Para L4 usar primero Anti UI Slop y después UI UX Pro Max, vinculados con SPEC/mockup del proyecto y evidencia visual real.

## Bloqueos y NEXT

Se puede completar F1 antes de F3. La ausencia del PC NO bloquea documentación y uso ChatGPT. **NEXT tras G1:** realizar el piloto de lectura efectiva en ChatGPT; Codex local será un único lote instalador y de verificación, no una cadena de microtareas.
