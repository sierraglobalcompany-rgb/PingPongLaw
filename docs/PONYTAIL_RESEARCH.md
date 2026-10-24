# Estudio técnico de Ponytail como fuente de Ley 1

## Alcance y procedencia comprobada

- Repositorio: https://github.com/DietrichGebert/ponytail, branch main, commit exacto **09c434ab73ca43761c5d8b0c5d341926c2fba710**, observado al crear PingPongLaw.
- Manifest `.codex-plugin/plugin.json` y `package.json`: versión **5.3.2**; licencia `LICENSE`: **MIT**. Árbol Git obtenido: 270 entradas, no 270 archivos de código revisados.
- Inspeccionados selectivamente: README, INSTALL, AGENTS, skills/ponytail, ponytail-review, ponytail-audit; manifest plugin Codex, hooks y sus dependencias principales; benchmark 2026-10-07. **No** se probó su instalación, ni se inspeccionó línea a línea el 100 % del repositorio, ni se ejecutó su suite de tests.

## Qué sí aporta a nuestras leyes

**L1:** su escalera de decisión no crear → reutilizar del repo → biblioteca estándar/plataforma → dependencia ya instalada → expresión legible → código mínimo completo. Antes de editar recorre callers/tests/fixtures/config. Prefiere menos código por claridad y corrección, no por competir en el contador de líneas.

**L2:** detectar duplicados y opciones especulativas solo tras buscar consumidores, incluidos accesos dinámicos. No borrar por gusto.

**L3:** reparar la causa compartida y contratos completos; tests focales para lógica riesgosa.

**L4:** accesibilidad y diseño aprobado no se sacrifican a la reducción de código. Ponytail no sustituye las dos fuentes UX de Ley 4.

**L5:** el skill pide un test/assert para lógica nueva no trivial; nuestro nivel de QA/independencia puede requerir más pruebas que una sola, especialmente seguridad/dinero/roles.

**L6:** instrucciones concisas y menor trabajo redundante; nuestras reglas de responsabilidad de ChatGPT y autonomía Codex continúan mandando.

## Auditorías de Ponytail — cuándo y límites

- `ponytail-review`: revisar un diff y sus callers, seguridad, carga prevista, pruebas, velocidad y qué sobra. Útil para QA focal después de cambios relevantes.
- `ponytail-audit`: mapear entradas, flujos y cargas previstas y priorizar defectos de corrección, seguridad, datos y escala antes de limpieza; útil para revisión amplia solicitada.
- El skill upstream limita a **20 hallazgos en la salida**. Para nuestras auditorías forenses se exige índice completo y no ocultar P0/P1; Ponytail actúa como perspectiva complementaria, no reemplaza la forense L1–L6.
- `shortcut:` permite documentar una concesión conocida, pero **no exime** de arreglar un defecto si ya afecta carga real, contratos o seguridad.

## Hooks y superficie de confianza

- El plugin Codex declara hooks para eventos de inicio de sesión, subagente y entrada de prompt, mediante `node` y archivos de hooks. Por tanto, su instalación **no se reduce a copiar un Markdown**.
- `ponytail-activate.js` puede ejecutar un mapa del código de la carpeta mediante Node; `ponytail-map.js` usa `git ls-files` o recorrido acotado y lectura de fuentes; `ponytail-mode-tracker.js` gestiona estado de modos y contiene ramas específicas para otros hosts.
- Hooks/estado pueden escribir archivos en directorios de configuración del agente. No es prueba de conducta maliciosa, pero exige revisión de permisos y confianza **antes de activar**. El mapa regex es un índice orientativo y no sustituye inspección de rutas de código.
- Instalar desde fuente oficial y verificar versión real; la referencia pin es para procedencia y auditoría, no garantía de que el marketplace siga igual. No copiar scripts hooks dentro de cada aplicación.

## Evidencia publicada por el autor (no validación nuestra)

El benchmark `benchmarks/results/2026-10-07-agentic.md` declara 39 tareas, 5 corridas por brazo, comparativa Claude Code; mediana/razón geométrica; reducción de líneas, tokens y tiempo reportadas por el autor. En esa evaluación deshabilitaron Bash para los agentes y las comprobaciones de ejecución ocurrieron después. El propio documento dice que en tareas de seguridad todos los brazos pasaron 30/30, no que Ponytail incrementó esa medida. **No extrapolar** ahorro de tokens a Codex Luna ni a proyectos de PHP/Android/PDF sin piloto real.

## Decisiones de adaptación

1. No forkar ni instalar toda la base Ponytail en PingPongLaw; referenciar upstream y conservar licencia/procedencia si se distribuyen copias sustanciales. Nuestra skill es redacción adaptada original.
2. Mantener canon único L1–L6; no sustituirlo por el AGENTS del autor ni crear una séptima ley.
3. Usar full como intensidad ordinaria; ultra no cambia permiso, alcance, contratos, mocks ni responsabilidad L5.
4. No activar automáticamente auditorías por cada commit/tarea ni guardar indicadores/telemetría local sin necesidad.
5. Plugin Codex es opcional respecto de lectura de la skill: si no puede instalarse, existe uso documental, pero declarar hooks NO_VERIFICADOS.

**Estado:** análisis estático de fuentes seleccionadas; instalación global Codex y resultados de adopción downstream NO_VERIFICADOS.
