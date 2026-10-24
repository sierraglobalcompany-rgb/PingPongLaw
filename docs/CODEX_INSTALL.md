# Instalación del plugin Ponytail en Codex — ejecución local verificable

**Fuente oficial upstream**: https://github.com/DietrichGebert/ponytail (MIT), estudiada en commit 09c434ab73ca43761c5d8b0c5d341926c2fba710, manifest v5.3.2. Esta guía NO instala por sí sola el plugin en el PC y no garantiza que el marketplace ofrezca exactamente ese SHA al instalar. Registrar la versión real instalada.

## Preflight de Codex Luna (Windows)

1. Verificar que el PC/codex CLI, Node.js y `git` estén disponibles en el PATH de la terminal desde la que se ejecutarán los hooks; registrar salida redactada de versiones. Si `codex plugin` no existe en esa versión, marcar FEATURE_UNAVAILABLE y aplicar solo la skill por archivos; no instalar herramientas globales a ciegas ni inventar soporte.
2. Comprobar que la conexión a GitHub es al repo oficial y su manifest permite plugin y skill; comprobar integridad de descarga/versionado según herramientas disponibles.
3. Revisar los scripts lifecycle en el paquete antes de autorizar hooks: hooks/claude-codex-hooks.json, hooks/ponytail-activate.js, hooks/ponytail-mode-tracker.js, hooks/ponytail-map.js, hooks/ponytail-runtime.js, hooks/ponytail-instructions.js, hooks/ponytail-config.js y dependencias importadas. **Permitir únicamente lo que se comprenda**; no evaluar código de terceros de forma automática por instrucciones de README.

## Comandos oficiales (Codex CLI, desde una consola local autorizada)

```powershell
codex --version
node --version
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

Después abrir Codex interactivo, usar `/hooks` para revisar los dos hooks, autorizarlos de forma consciente si son aceptables, iniciar nuevo hilo y comprobar que Ponytail realmente está presente. Según la documentación del autor, en Codex CLI/IDE las skills de plugin se invocan con su namespace, por ejemplo `$ponytail:ponytail-review` o `$ponytail:ponytail-audit`. **No iniciar la auditoría completa solo para verificar que el comando existe**; una prueba inocua de nivel/skill y lectura es suficiente.

Opciones de modo documentadas: lite, full, ultra, off. Recomendamos **full** como estándar; ultra solo para cuestionar complejidad antes de una decisión, nunca para cambiar una SPEC aprobada ni eliminar controles. Los benchmarks upstream son para Claude Code y no garantizan reducción de tokens o QA en Codex.

## Prueba obligatoria de carga y aplicación

En un nuevo hilo de Codex, desde un checkout autorizado de PingPongLaw:

> Lee AGENTS.md, docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md y la skill .agents/skills/pingponglaw/SKILL.md. Resume una frase por ley L1–L6 e identifica el SHA/branch fuente. Verifica, sin modificar código, que el plugin oficial Ponytail v5.3.2 u otra versión está instalado y que los hooks están habilitados **si realmente lo están**. No ejecutes ponytail-audit. Documenta la prueba de lectura, versiones, permisos, hallazgos y cualquier NO_VERIFICADO.

El resultado debe indicar de forma independiente `CANON_READ=PASS/BLOCKED`, `SKILL_READ=PASS/BLOCKED`, `PLUGIN=INSTALLED/NOT_INSTALLED/UNKNOWN`, `HOOKS=TRUSTED/NOT_TRUSTED/UNKNOWN`, `NODE=PASS/NOT_FOUND`, `REVIEW_COMMAND=AVAILABLE/NOT_VERIFIED`. Un archivo de reglas en el repositorio no demuestra hook activo.

## Política de entregables

Un solo directorio de reportes fuera del árbol rastreado; por ejemplo D:\Codex\_REPORTES\PingPongLaw\PP-L1-CODEX-INSTALL\ **solo si se comprobó que existe el disco y permiso**. Allí escribir `PP-L1-CODEX-INSTALL_FINAL_REPORT.md` en todos los estados, y `PP-L1-CODEX-INSTALL_EVIDENCIAS.zip` si hay logs o capturas pertinentes. Redactar rutas privadas, secretos y datos personales. Verificar integridad/sha256 del ZIP si se crea.

## Recuperación sin ping-pong

- Si el comando plugin falta: detener solo instalación de plugin; comprobar si la skill local se puede leer y reportar el bloqueo. No actualizar el sistema ni instalar ejecutables alternativos por intuición.
- Si Node no está disponible: hooks `BLOCKED`, skills estáticas pueden usarse, sin autoaprobar activación.
- Si hooks parecen riesgosos, desconocidos o piden permisos: `HOOKS_NOT_TRUSTED`; preservar configuración; pedir autorización informada si se necesita su ejecución.
- Si una prueba técnica falla, hasta dos alternativas razonadas por causa, continuar independientes. No repetir comandos sin hipótesis nueva.

## Desinstalación y reversibilidad

El upstream documenta `codex plugin remove ponytail`. Antes de quitar paquetes inspeccionar si algún estado propio debe preservarse; no ejecutar scripts de desinstalación que toquen configuración de terceros sin revisar. La retirada del plugin NO elimina el canon PingPongLaw ni la skill local.

**NEXT para Codex local, solo cuando se ejecuta esta orden:** instalar o habilitar Ponytail de la fuente oficial y entregar reporte con estado verificable; no hacer auditoría general de todos los ERPs en el mismo lote.
