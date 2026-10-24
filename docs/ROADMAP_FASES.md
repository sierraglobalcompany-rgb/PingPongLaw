# PingPongLaw — Plan maestro de implementación por fases (V2)

**Fuente del estado:** repositorio real, no este texto por sí solo. **BASE_AUDITADA:** `main@9fefcf72f1629af116c3b759202d930c0ada8840`. La corrección F1.1 fue integrada a `main` y comprobada con CI; **no equivale a una instalación del plugin Codex**.

## Resultado final buscado

Un **canon único, ligero y verificable** de seis leyes, con L1 KISS + Ponytail, que ChatGPT consulte al iniciar una tarea técnica y que Codex pueda leer/aplicar en proyectos autorizados. Debe ahorrar complejidad, revisiones innecesarias y transferencias improductivas **sin recortar seguridad, calidad, diseño humano ni pruebas de aceptación**. No se construirá SaaS, base de datos, dashboard, telemetría ni servicio en segundo plano.

**Detalle de implementación de skills:** [plan avanzado](ROADMAP_SKILLS_AVANZADO.md) — es un desglose operativo de estas mismas fases, no otra fuente normativa ni otra auditoría obligatoria.

## Estado y dependencias

| Fase | Responsable prioritario | Producto verificable | Gate de salida | Estado |
|---|---|---|---|---|
| **F0. Investigación y procedencia** | ChatGPT | Ponytail fuente/licencia/SHA, comparación con leyes, límites de hooks y benchmark | G0: hechos respaldados, riesgos explícitos | **HECHO, revisión selectiva** |
| **F1. Canon central** | ChatGPT | README, AGENTS, seis leyes, skill, guías | G1: en main, seis leyes en orden y referencias correctas | **HECHO EN MAIN** |
| **F1.1. Endurecimiento focal** | ChatGPT | Eliminar referencias obsoletas, corregir CI, pruebas negativas y links, actualizar plan | G1.1: tests focales + CI mismo HEAD; PR revisable | **HECHO EN MAIN** (CI de PR y main aprobado) |
| **F1.2. Skills por ley + dos adaptadores L4** | ChatGPT: 9 skills enrutadas, fuentes externas fijadas y tests | G1.2: metadatos, rutas, router y regresión CI sobre SHA | **INTEGRADO EN MAIN**, pruebas estructurales 13/13; carga en PC no verificada |
| **F2. Piloto ChatGPT real** | ChatGPT | Evidencia de lectura del canon exacto y 3 casos de uso (prompt, implementación focal, entrega) | G2: mostrar consulta real, decisiones técnicas, límites y pruebas sin ciclos extra | **EJECUTADO FOCALMENTE 2026-10-24**: T1/T2 y verificación metodológica T3 documentadas, sin certificar producto/Codex local |
| **F3. Codex Windows / Ponytail oficial** | Codex local; ChatGPT dirige | Inventario CLI/Node; plugin oficial y skills; revisión explícita de hooks; prueba de sesión limpia | G3: versión instalada, lectura de L1–L6, hooks autorizados/NO_CONFIADOS de forma explícita, informe MD/ZIP si procede | **NO VERIFICADO: no hay acceso al PC** |
| **F4. Piloto downstream** | ChatGPT + Codex si hace falta | 1 proyecto con canon y normas específicas reconciliadas; prueba de cambio real acotado | G4: lectura aplicable, cambio funcional probado, Ley 5, sin suprimir AGENTS previos | **PENDIENTE** |
| **F5. Expansión** | ChatGPT/GitHub + Codex local | Matriz de repos, PRs precisos, conflictos resueltos, rollout secuencial | G5: cada repo con estado real y trazabilidad SHA; ningún merge automático | **PENDIENTE** |
| **F6. Evaluación/mantenimiento** | ChatGPT, verificador distinto si procede | 2–3 casos comparables: correctitud, alcance, LOC, tiempo/transferencias y defectos | G6: datos reales sin extrapolar benchmark upstream; decisiones de mantener/revertir | **PENDIENTE** |

**Dependencias:** F2 y F3 pueden avanzar de forma independiente tras G1.1; F4 requiere canon accesible y un agente que demuestre su lectura, pero **no necesita activar hooks** si se valida el modo skill/documental. F5 requiere G4. F6 requiere al menos casos aplicados. Evitar múltiples auditorías previas a un gate ya satisfecho.

## Gates concretos

**G0 — Fuentes:** registrar `DietrichGebert/ponytail@09c434ab73ca43761c5d8b0c5d341926c2fba710`, v5.3.2/MIT, distinguir skill estática de plugin Node y métricas publicadas por su autor. No afirmar cobertura total del código upstream.

**G1/G1.1 — Canon:** `python3 scripts/check_canon.py` y `python3 -m unittest discover -s tests -v` con éxito en HEAD exacto, enlaces locales comprobados, seis leyes presentes, skill actual, workflow GitHub terminado. Esto verifica **estructura**, no carga o semántica completa del agente.

**G2 — ChatGPT:** prueba sobre una tarea real con `REPO/SHA_LEIDO`, aplicación observable de L1–L6, decisiones tomadas/edición directa cuando sea posible, pruebas pertinentes y ningún prompt artificial. Usar `docs/VALIDACION_OPERATIVA.md`. Cuando ChatGPT no pueda consultar GitHub, adjuntar el canon y registrar la limitación.

**G3 — Codex:** instalación oficial `codex plugin marketplace add DietrichGebert/ponytail` y `codex plugin add ponytail@ponytail` **solo en PC autorizado y tras preflight de comandos**. Antes de confiar en hooks, revisarlos junto con Node y permisos; nunca cambiar ajustes globales por inferencia. Cargar canon, probar skill y comprobar estado de hooks por observación. El perfil `full` es preferido; no usar `ultra` para cuestionar contratos aprobados.

**G4 — Piloto:** escoger un repo representativo (AlquilaPro solo como candidato, no autorización automática), leer todas sus reglas y PRs existentes. No crear otra copia del canon ni otro PR si hay uno adecuado; actualizar el existente con evidencia. Medir que el agente realiza trabajo real, no solo explica.

**G5 — Multi-repo:** procesar por prioridad/riesgo, identificar HEAD y ramas reales, conflictos de `AGENTS.md` y políticas de ZIP. Estados por repo: `NO_APLICA`, `EN_PR`, `LEYES_PRESENTES`, `CODEX_READ_VERIFIED`, `CONFLICTO`, `NO_ACCESO`. Un PR abierto **no equivale a reglas instaladas en main**. Ramas con WIP y repos vacíos no se tocan sin decisión específica.

**G6 — Medición:** corrección/seguridad primero; eficiencia segundo. Comparar tareas equivalentes, medir transfers ChatGPT↔Codex, QA ejecutada, defectos reales y diff neto; **no exigir reducción fija de líneas** y no fingir el ahorro de tokens atribuido a Ponytail por su autor.

## Política anti-ping-pong para este plan

- La instalación global es **un lote local**: preflight → fuente → inspección hooks → instalación autorizada → comprobación skills/hook → evidencia → informe. Un error recuperable no termina todo, pero secretos, permisos y escritura destructiva siguen bloqueando acciones riesgosas.
- **Auditoría proporcional**: sin nueva auditoría si ya hay evidencia suficiente; chequeo focal por delta; revisión Ponytail de diff cuando tenga utilidad; auditoría forense completa solo por solicitud/riesgo transversal.
- Antes de enviar Codex: `HECHO_CHATGPT`, `LIMITACION_REAL`, `OBJETIVO_CODEX`, `GATE_CIERRE`. No crear un prompt por un import o por un solo comando.
- Antes de PASS: Ley 5 separa resultados de CI y pruebas locales de la aceptación de funcionamiento, UX y permisos.

## Riesgos y rollback

1. **Carga del canon en ChatGPT no automática:** usar URL/adjunto y demostrar lectura. Ningún cambio en PingPongLaw puede obligar a otros chats a leerlo sin conexión.
2. **Hooks Node:** código de terceros ejecutado en sesión; desactivar/remover por procedimiento upstream, preservar el canon independiente del plugin.
3. **Reglas locales conflictivas:** fusionar solo cláusulas faltantes; evitar reemplazos globales en 17 repos.
4. **Canon demasiado largo:** `AGENTS.md` sigue siendo índice breve; leer la sección relevante y verificar seis IDs en inicio/cierre sin imprimir 48 KB en cada turno. Reducir el documento canónico solo cuando se compruebe equivalencia completa.
5. **CI engañoso:** el comprobador estructural y sus pruebas negativas no afirman que Codex ejecutó la skill o que un ERP pasó sus tests.
6. **Licencia MIT:** código sustancial copiado de Ponytail debería preservar avisos; preferir adaptación y enlaces.
7. **Rollback:** revertir el PR de F1.1 si falla; no altera runtime. No borrar comentarios, bases ni PRs ajenos para simplificar.

## NEXT

**G1.1 documental cerrado** con pruebas y CI en main. **NEXT: F2**, completar los tres casos de uso de ChatGPT según `docs/VALIDACION_OPERATIVA.md`. F3 puede avanzar en paralelo cuando exista Codex local autorizado. No crear otra auditoría forense antes de ese piloto.
