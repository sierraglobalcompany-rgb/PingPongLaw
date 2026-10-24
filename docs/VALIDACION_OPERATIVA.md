# Validación operativa PingPongLaw — F2, F3 y F4

Esta prueba no sustituye las seis leyes ni la Ley 5; distingue **presencia documental** de **comportamiento observado**. Ejecutarla una vez por cambio material en el canon o al instalarlo, no en cada prompt.

## F2 — ChatGPT (3 casos, verificables sin Codex)

**Preparación:** leer realmente `AGENTS.md`, `docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md` y la guía `docs/CHATGPT_START.md` desde el SHA concreto de PingPongLaw. Registrar el SHA consultado, archivos/segmentos leídos, objetivo del usuario y restricciones reales del proyecto elegido. No afirmar que se cargó por memoria.

| Caso | Entrada mínima | Qué demuestra PASS | Bloqueo legítimo |
|---|---|---|---|
| **T1 — prompt** | «Revisa esta orden repetitiva; ¿necesita auditoría o basta corrección focal?» | La orden se mejora o se conserva con evidencia; no se dispara automáticamente otro maestro ni Codex; L1–L6 consultadas | No se recibió orden concreta |
| **T2 — ejecución directa** | Un cambio pequeño y autorizado en un repo con acceso real | ChatGPT lee el archivo, decide y aplica diff/test donde su herramienta lo permite; Codex solo por una limitación demostrable | Sin permiso o sin herramienta de escritura/test; documentar realmente |
| **T3 — verificación Ley 5** | Informe de Codex + SHA/diff/resultado de prueba | Identifica evidencia suficiente, ausente y falsa equivalencia CI=función; emite dictamen acotado sin repetir QA innecesario | No hay entrega o SHA verificable |

**Resultado obligatorio:** `T1=PASS/FAIL/BLOCKED/NOT_RUN`, `T2=...`, `T3=...`, qué herramienta/archivo se consultó, L1–L6 aplicables, errores encontrados y `NEXT`. Un solo ejemplo T1 **no certifica toda F2**.

## F3 — Codex oficial Ponytail

Leer `docs/CODEX_INSTALL.md`, comprobar Codex/Node/marketplace local, versión descargada y procedencia. Inspeccionar antes de habilitar hooks. En sesión nueva, invocar `pingponglaw` desde la ubicación adecuada y comprobar que se leyó el canon; después prueba inocua de presencia de la skill `ponytail`.

**Observaciones separadas**: `CANON_READ`, `PONYTAIL_SKILL_AVAILABLE`, `PLUGIN_INSTALLED`, `HOOKS_REVIEWED`, `HOOKS_TRUSTED`, `SESSION_INJECTED`. Un `codex plugin list` hipotético no es prueba si el comando no existe. Nunca instalar Node, elevar privilegios o aceptar hooks silenciosamente.

**Evidencias locales:** informe Markdown + ZIP cuando existan capturas/logs útiles, juntos en una carpeta externa autorizada. Redactar secretos, tokens y paths sensibles. Si no hay PC accesible: `F3=BLOCKED_LOCAL`, no `FAIL` del canon.

## F4 — piloto en proyecto de aplicación

Seleccionar un repositorio/branch con permisos explícitos y SPEC real. Leer sus `AGENTS.md` y detectar reglas incompatibles antes de escribir. Una adaptación mínima del enlace a PingPongLaw, versión/SHA del canon fijados y **sin sobrescribir el contrato del proyecto**.

Probar:
1. `PRE`: Codex/ChatGPT identifica las seis leyes y las restricciones específicas.
2. `EJECUCIÓN`: un cambio real autorizado usa KISS Ponytail, revisa callers, no genera capas innecesarias.
3. `POST`: tests focales/seguridad pertinentes y reporte Ley 5 del mismo SHA/build.
4. `L6`: si Codex intervino, una única transferencia de lote coherente y ningún ping-pong por errores mecánicos recuperables.

## Evidencia que NO se debe confundir

- `python scripts/check_canon.py` PASS → estructura sana, **no** plugin activo.
- Workflow GitHub SUCCESS → script corrió, **no** UX real/funcionalidad aprobada.
- `AGENTS.md` presente → instrucción almacenada, **no** leído automáticamente por ChatGPT.
- Hook marcado como confiable → autorización, **no** que se ejecutó o que su salida fue aplicada.
- Benchmark Ponytail upstream → cifras del autor, **no** resultado en nuestras aplicaciones.
- Captura visual de maqueta → referencia, **no** producto funcionando.
