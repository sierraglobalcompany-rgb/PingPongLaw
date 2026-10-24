# Registro de fuentes externas y límites — Ponytail / Ley 4

**Revisión de GitHub:** 2026-10-24. Las fuentes pueden cambiar después de sus SHAs; no presentar una versión mutable de `main` como evidencia de un cambio evaluado. Las skills de PingPongLaw son **adaptaciones propias basadas en conceptos**, no clones ni instalaciones automáticas.

| Fuente | SHA observado | Archivos clave | Uso permitido por esta integración | Pendiente |
|---|---|---|---|---|
| [Ponytail](https://github.com/DietrichGebert/ponytail) | `09c434ab73ca43761c5d8b0c5d341926c2fba710` | `skills/ponytail/SKILL.md`, `skills/ponytail-review/SKILL.md`, `skills/ponytail-audit/SKILL.md`, `skills/ponytail-debt/SKILL.md`, `INSTALL.md`, `hooks/` | L1 escalera mínima, revisión focal, auditoría bajo demanda, deuda `shortcut:` | Test real de versión/plugin/hooks Codex en Windows |
| [Anti UI Slop](https://github.com/github/awesome-copilot/tree/main/skills/anti-ui-slop) | `d85f762d6e521abf5fe16703946e9b38adc42da7` | `SKILL.md`, `reference/audit.md`, `reference/operate.md`, `references/uizze-reference-policy.md`, `MANIFEST.json`, `LICENSE` | L4 primera pasada de producto/flujo y defectos observables; un playbook por tarea | Aclarar discrepancia de licencia antes de redistribuir fuentes |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `d14efff8ed1faa4187f004f79926f428c8074ec7` | `.claude/skills/ui-ux-pro-max/SKILL.md`, `references/quick-reference.md`, `references/pro-rules.md`, `scripts/search.py`, `LICENSE` | L4 segunda pasada por criterio UX/accessibility/stack con búsqueda mínima | Confirmar entorno/instalación real si se desea ejecutar scripts de búsqueda |

## Ponytail: adopción de lo útil, no de todo el runtime

- **La skill principal no es un minificador de código**: pide comprender callers, tests y datos, luego escoger la solución menor que resuelve **todo** el contrato. Seguridad, validación, accesibilidad y manejo de errores no son recortables.
- **`ponytail-review`** analiza cambios/diff y código conectado; útil tras cambios de riesgo. **`ponytail-audit`** mapea repo y flujos, bugs, seguridad, escala y ruido; **su propio formato limita a 20 hallazgos**, lo cual no sirve como límite en una auditoría forense nuestra con más fallos importantes.
- **`ponytail-debt`** recoge marcadores `shortcut:` con límite y condición de revisión: solo cuando se solicita revisar deuda, no un cron ni otro ledger redundante por defecto.
- **`ponytail-gain`** muestra datos de benchmark del autor, **no** permite afirmar que ahorramos tokens en nuestros proyectos. El benchmark de 2026-10-07 usa Claude Code, no valida automáticamente Codex Luna.
- **Hooks oficiales del plugin:** el manifest Codex declara `SessionStart`, `SubagentStart`, `UserPromptSubmit`; script Node puede leer árbol de código/config y generar mapa. Debe auditarse el paquete y autorizarse en el equipo antes de afirmar ejecución.
- **Compatibilidad por capas:** copia de reglas para otros hosts, plugin oficial Codex, y skills locales adaptadas PingPongLaw son distintos. Nunca vender `SKILL_DOCUMENTADA` como `PLUGIN_INSTALADO`.

## Anti UI Slop: hallazgo de procedencia / licencia

En el commit citado, el `skills/anti-ui-slop/SKILL.md` declara `license: MIT`; **pero** la ruta de distribución `skills/anti-ui-slop/LICENSE` contiene Apache License 2.0 y su `MANIFEST.json` también indica `Apache-2.0` para el componente de diseño referenciado. A falta de reconciliación exacta del conjunto de archivos, **no vendorear** el contenido completo ni afirmar una licencia única del paquete. Enlazar fuente y escribir adaptadores propios. Si se necesita copiar material, resolver avisos y términos por archivo, conservar NOTICE y atribuciones pertinentes.

La skill ofrece un servicio externo UIZZE opcional (algunas funciones sujetas a pago); **no se afirma conexión** ni se envían datos privados del proyecto a servicios externos sin base/autorización. Su regla es **cargar un playbook** según contexto y, si se puede renderizar, revisar una vez los fallos observables. El playbook `reference/audit.md` prioriza hasta tres problemas materiales y prohíbe considerar gustos como errores. Cuando nuestro encargo es forense exhaustivo, ese límite se usa solo como resumen priorizado; hallazgos adicionales verificables no se ocultan.

## UI UX Pro Max: búsqueda condicionada al stack

El `SKILL.md` divide guías en accesibilidad, interacción, rendimiento visible, estilos, layout, tipografía, animación, formularios, navegación y gráficos. Incluye herramienta Python de búsqueda y colecciones de datos. **No hay necesidad de copiar decenas de CSV/scripts en PingPongLaw** si solo se requiere una comprobación focal.

Para una anomalía concreta elegir `--domain` y solo si aporta aclaración adicional `--stack`; no ejecutar todas las consultas. El propio skill advierte sobre no asumir stack, no regenerar `MASTER.md` existente sin autorización y no usar `--force` por defecto. Para páginas nuevas sin sistema aprobado puede orientar la propuesta; si existe SPEC/mockup, respetarlo.

## Criterios comunes de L4/L5

1. **Contrato primero:** SPEC, mockup, diseño humano, acciones reales/roles/estados.
2. **Pasada 1 / Anti UI Slop:** producto, jerarquía, clipping, contenido, estados y fluidez de interacción.
3. **Pasada 2 / Pro Max cuando haya riesgo no resuelto:** a11y, teclado, responsive, touch, stack, contraste, navegación y semántica de controles.
4. **Evidencia:** navegador/render auténtico, roles y resoluciones aplicables. Sin ello solo análisis estático.
5. **Convergencia:** corregir por causa raíz, no crear otra ronda de auditoría sin cambio relevante; QA Ley 5 del SHA real.

## Política de actualizaciones upstream

Fijar commit/versión conocido, comprobar cambios en README/SKILL/manifest/licencia, identificar si cambian reglas o seguridad, probar una tarea piloto. No sincronizar automáticamente `main`, scripts, hooks ni bases de datos del proveedor a nuestros repositorios. La revisión de licencias y dependencias es necesaria **antes de copiar código**.

**Auditoría hecha:** rutas, archivos y contenidos clave observados en GitHub; no se ejecutó la suite upstream completa ni se certificó integración real de UIZZE o Pro Max en Codex local.
