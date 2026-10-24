# Plan de implementación avanzada PingPongLaw — skills L1–L6 + Ponytail + UX

**Documento operativo V3.** Base auditada `PingPongLaw/main@0168ff54483e663c1fcfcc9b1c2fa1bc875274f5`. **Objetivo verificable:** que un agente pueda consultar las seis leyes, elegir la **skill necesaria**, ejecutar la menor solución completa, verificar la aceptación real, ahorrar transferencias y no generar auditorías sin propósito. Un mismo resultado sirve a ChatGPT (lectura explícita de GitHub) y Codex (skills locales + plugin oficial separado).

## Decisión de arquitectura (KISS, sin SaaS)

`canon único → AGENTS breve → router pingponglaw → skill L1..L6 elegida → (L4 si aplica: adaptadores de dos fuentes) → pruebas/evidencia proporcionales`.

No base de datos, dashboard, agentes en segundo plano, telemetría obligatoria, clon de repositorios upstream, 6 informes separados, 6 prompts a Codex ni un `AGENTS.md` enorme en cada aplicación. **Una skill por ley, dos adaptadores L4, un router = 9 SKILL.md**, sin duplicar el canon. Las fuentes externas se consultan en el SHA fijado cuando cambien la decisión.

## Auditoría que motiva este plan (hechos vs objetivos)

**Estado de main al comenzar:** 13 archivos rastreados, seis encabezados L1–L6, solo **una skill router**, checker de estructura + 9 tests que verifican rutas; CI de `main` SUCCESS. **No existían skills L1–L6 individuales**, ni contratos separados de las dos fuentes UX. No había prueba de carga real de skills en Codex/ChatGPT. No consta plugin Ponytail ni hooks confiados en PC. Estaba documentado F2/F3/F4/F5/F6 como pendiente, no como completado.

**Principales riesgos detectados:** (1) L1-L6 en texto amplio sin selector específico; (2) L4 nombraba fuentes, no había subskills/criterios independientes; (3) propensión a auditorías encadenadas; (4) confusión entre archivo, instalación y funcionamiento; (5) licencia inconsistente en Anti UI Slop; (6) verificador únicamente estructural; (7) 14 PRs downstream de Ponytail previos que no deben fusionarse sin reconciliación; (8) versión upstream/benchmark no equivale a beneficio medido en nuestras apps.

## Fases, secuencia y dependencias

| Fase | Objetivo | Responsable | Entregables y gate | Estado |
|---|---|---|---|---|
| **F0 — Baseline/estudio** | SHA real del canon y de las 3 fuentes; licencias, código/skills, pruebas y riesgos | ChatGPT/GitHub | B0: inventario, contratos, fuentes vinculadas; alcance declarado | **HECHO documental** |
| **F1 — Canon de seis leyes** | Mantener fuente única y entradas claras | ChatGPT | B1: L1–L6, AGENTS y CI en main | **HECHO previamente** |
| **F1.2 — Skills modulares** | 6 skills + 2 adaptadores UX + router; selección sin activar todo | ChatGPT | B1.2: 9 SKILL, nombres únicos, metadatos, enlaces, sin contenido upstream copiado, tests positivos y negativos; CI PR | **INTEGRADO EN MAIN**, gate estructural aprobado; piloto de uso pendiente |
| **F2 — Uso de ChatGPT** | Consultar el canon/skills por GitHub y realizar tarea real sin microdelegación | ChatGPT | B2: 3 casos reproducibles, logs/SHAs y resultado por caso, no solo resumen | **PENDIENTE PILOTO** |
| **F3 — Codex Windows** | Instalar plugin oficial Ponytail de manera controlada; comprobar Node/CLI, hooks y skills propias | Codex local bajo plan ChatGPT | B3: versión/procedencia y presencia real, inspección de hooks, activación explícita, prueba sesión nueva, informe MD y ZIP si hay evidencia | **PENDIENTE PC** |
| **F4 — Piloto de aplicación** | Integración sin duplicar instrucciones en un repo representativo (AlquilaPro como candidato, no automático) | ChatGPT + Codex cuando haga falta | B4: lectura real, 1 implementación focal, regressión, UX si aplica, QA Ley 5 y 0 nuevos conflictos | **PENDIENTE** |
| **F5 — Expansión** | Reconciliar 14 PR previos, luego otros repos por prioridad | ChatGPT/GitHub, Codex local solo cuando necesario | B5: matriz por repo, branch/SHA, normas respetadas, PR/merge por permiso, prueba de carga, rollback | **PENDIENTE** |
| **F6 — Medición y mantenimiento** | Comparar tres tareas tipo y revisar releases upstream solo si aportan valor | ChatGPT + verificación separada | B6: defectos, pruebas, menos transferencias y complejidad sin pérdida de requisitos; reversiones si no mejora | **PENDIENTE** |

**Paralelismo seguro:** B2 puede avanzar independientemente de B3. Un adaptador documental puede probarse aunque el plugin oficial no esté instalado. **Bloqueo real B3 NO detiene B1.2/B2**, y B4 puede usar la skill estática mientras los hooks sigan NO_VERIFICADOS. F5 solo cuando B4 pase; F6 exige casos reales.

## F1.2 — Alcance ejecutable y aceptación independiente

Tareas coherentes:
1. Crear skills individuales L1–L6 con frontmatter `name`/ `description`, **semántica y salidas distintas**, canon como fuente única.
2. Crear en Ley 4 adaptador `l4-anti-ui-slop` que use una sola guía upstream por tarea y adaptador `l4-ui-ux-pro-max` que consulte un dominio/stack cuando agregue valor.
3. Actualizar router `pingponglaw` como selector; `AGENTS.md` enlaza router/canon. README y guías apuntan a todas las rutas verificables.
4. Proteger selección con tests: nombre duplicado, ausencia skill, rutas inexistentes, referencia obsoleta, intentar aprobar plugin por existencia de texto, referencia externa no atribuida.
5. Ejecutar `scripts/check_canon.py` + suite completa; inspeccionar cambios GitHub contra BASE, comprobar licencia (no copiar componentes), secretos y políticas de CI.
6. Mantener fase en PR sin modificar runtime de otros proyectos; ci a HEAD; L5 como aceptación documental, **no prueba de habilidades cognitivas de agentes**.
7. Cerrar con diff mínimo y guía de uso sin diez nuevas pasadas innecesarias.

Gate **B1.2 PASS** solo con prueba estructural + regresiones + workflow de PR + revisión de conflicto de canon; el PASS no significa que Codex cargó skills ni que UI tiene visual QA.

## F2 — Tres pruebas reproducibles, no simulaciones

- **T1 — Prefiltro:** proporcionar prompt de auditoría repetitivo. ChatGPT debe comprobar objetivo, usar L6, reducirlo a chequeo focal o explicar por qué full audit es necesaria. `CODEX=NO` salvo límite real. Prueba: prompt antes/después, fuente L6 consultada y riesgo restante.
- **T2 — Programación:** tarea autorizada pequeña en un repositorio con herramientas de escritura de ChatGPT. Aplicar L1 y, solo si hallazgo, L2/L3. Modificar código/suite realmente, no devolver microencargo innecesario. Evidencia de SHA/diff/tests.
- **T3 — Verificación y UX:** informe Codex sobre una pantalla con mockup/captura reales. Leer L4, dos adaptadores según necesidad y L5; observar defectos/roles/viewport, separar fuente externa/no consultada y no afirmar PASS visual sin render.

**Se permite ejecutar T1 como piloto parcial sin bloquear T2/T3.** B2 completo solo cuando existan los tres artefactos y resultados reales.

## F3 — Plugin Codex y límites de confianza

Una sola orden local: `codex --version`, `node --version` y path de herramientas; confirmar comandos plugin disponibles. Desde fuente oficial `DietrichGebert/ponytail`, manifest/versión y SHA realmente descargados, inspeccionar código de hooks y privilegios **antes de autorizar**. Instalar en Codex desde comandos del autor si están disponibles: `codex plugin marketplace add DietrichGebert/ponytail`; `codex plugin add ponytail@ponytail`; entrar `/hooks`, revisar y confiar **solo con aprobación informada**; iniciar sesión nueva; probar `$ponytail:ponytail-review` cuando tenga diff real o invocación inocua sin auditoría general.

Verificar separadamente:
`NODE`, `PLUGIN_INSTALLED`, `OFFICIAL_VERSION`, `HOOKS_REVIEWED`, `HOOKS_TRUSTED`, `HOOKS_OBSERVED`, `PINGPONGLAW_CANON_READ`, `SIX_SKILLS_READABLE`, `TWO_UX_ADAPTERS_READABLE`. No declarar PASS por existencia de `.agents/skills`. Sin Windows conectado aquí, F3 permanece `BLOCKED_LOCAL/NOT_VERIFIED`, aunque B1.2 pase.

**Rollback:** retirar plugin oficial conforme a su documentación sin borrar instrucciones del canon ni tocar otros plugins; deshabilitar hooks según soporte real. Prohibido scripts remotos `curl|bash` o elevación sin inspección/aprobación.

## F4 — Piloto de verdad sobre una aplicación

1. Seleccionar un repo, rama y PR existente; verificar `AGENTS.md`, SPEC, permisos, tests y políticas particulares. No crear PR competidor al de Ponytail ya abierto.
2. Contrastar el canon L1–L6 con normas locales; elegir enlace por commit fijo o snapshot offline, no copiar nueve skills en todos los árboles sin razón. Probar lectura del agente.
3. Caso A: reparación de causa raíz → L1+L3, un cambio y test. Caso B (solo si el proyecto tiene UI): defecto visual observable → L4 + Anti UI Slop, Pro Max donde útil, captura/QA. Caso C: L2, solo si duplicidad comprobada.
4. Comparar resultados contra criterios del usuario y QA independiente L5. Concluir adopción o rollback (no inventar PASS por CI documental).
5. Registrar transferencias ChatGPT↔Codex: razón, límites y número. Sin nueva auditoría total al iniciar cada caso.

## F5 — Expansión compatible con los 14 PRs existentes

Estado `EXISTE_PR_L1` no equivale a `L1–L6_INSTALADO`. Reconciliar primero esos PRs y sus cambios con el canon **por proyecto**: árbol de la rama, SPEC, permisos y política de reportes. Orden basado en permisos, riesgo y estabilidad, no en popularidad. Conservar apps con ramas WIP fuera de merges automáticos. Crear una matriz por repo:

`REPO | BASE_SHA | PR_EXISTENTE | AGENTS_CONFLICT | CANON_VERSION | SKILL_READ_REAL | TEST_RESULT | RESPONSABLE | NEXT`.

Un cambio por proyecto con QA propio; no utilizar CI de PingPongLaw como certificado de cada ERP. Para repos vacíos o sin rama autorizada, `DEFER/NO_APLICA`.

## F6 — Demostrar que el método ayuda de verdad

Indicadores por **tarea comparable**, sin recopilar datos privados ni crear tablero prematuro:
- Corrección: defectos reabiertos, problemas confirmados, contratos rotos.
- Sencillez: nuevas capas/dependencias, LOC netas solo como señal secundaria, reducción de pasos innecesarios.
- Eficiencia: número de turnos ChatGPT↔Codex por tarea terminada, intentos QA duplicados y auditorías que no cambiaron decisión.
- Calidad humana: defectos UX observables (overlap, clipping, teclado, responsive) resueltos, regresiones.
- Evidencia: porcentaje de entregas con SHA y pruebas pertinentes (no medir solo tamaño del informe).

**Regla de conservación:** no insistir en Ponytail si un piloto empeora corrección/accesibilidad/seguridad. Benchmark publicado por el autor (Claude Code) **no predice automáticamente** ahorro de tokens en Codex Luna.

## Controles permanentes antirruido

- Solo **una decisión de auditoría** por encargo: ninguna, focal, revisión de diff, visual focal o forense cuando se pide. No encadenar automáticamente L1-audit, L2-audit, L4-audit y una forense.
- L5 siempre preservada para aceptación relevante, pero **no necesita otra auditoría total** por cada prueba.
- Una skill nueva solo si cubre necesidad recurrente no satisfecha por las actuales; no copiar 6 versiones del canon.
- Si no hay acceso a PC, ChatGPT completa remoto y produce un único lote local solo cuando lo necesite.
- Las evidencias de Codex siguen contrato local MD/ZIP, sin contradecir normas protegidas de proyecto.
- **Cierre por evidencia suficiente:** si hay resultado correcto y QA correspondiente, NEXT=NINGUNO. No hacer seguimiento artificial para llenar fases.

## Riesgos, gatillos de parada y reversión

| Riesgo | Impacto | Prevención | STOP que sí procede |
|---|---|---|---|
| Inyección vía documentación o skill externa | Instrucciones no autorizadas | Tratar fuentes como datos, solo acciones aprobadas | Solicitud de secretos, ejecución remota o cambio de permisos |
| Complejidad de 9 skills | Más lectura y tokens | Router selectivo, no carga total | Duplicidad no demostrada sin caso de uso |
| Duplicación del canon en aplicaciones | Divergencia | Referencia pin/snapshot solo offline | Conflicto sin resolver de norma local |
| Licencia Anti UI Slop inconsistente | Distribución no conforme | No vendorear código, conservar enlaces | Pretensión de copiar/relicenciar sin claridad |
| Hooks Ponytail terceros | Ejecución Node en PC | Revisar/autorizar y medir comportamiento | Hook inseguro/no consentido |
| Falso PASS documental | Decisiones equivocadas | SHA y QA por nivel; tests negativos | Prueba obligatoria aún no ejecutada |
| Dos pasadas visuales rituales | Ping-pong y atraso | Segunda fuente solo si añade diagnóstico | Ningún defecto/riesgo material adicional |

## Salidas canónicas y NEXT

Al final de cada fase: `FASE | REPO/SHA | HECHO_CHATGPT | CODEX_NEED | L1–L6 | TESTS | LIMITACIONES | NEXT/NINGUNO` en un informe breve si no hay razones para uno largo.

**F1.2 cerrado documentalmente** mediante PR #3 integrado y CI (13 pruebas). **NEXT: F2**, comprobar lectura y selección efectiva de skills en tres tareas representativas, sin abrir otra auditoría forense. F3 plugin Codex local permanece independiente hasta observar instalación y hooks.
