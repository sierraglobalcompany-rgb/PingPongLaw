---
name: l4-ui-ux-pro-max
description: Adaptador de UI UX Pro Max. Usar solo para necesidades visuales sobre accesibilidad, interacción, responsive, tipografía, formularios, gráficos o implementación dependiente del stack.
---
# L4B — UI UX Pro Max (fuente externa; guía complementaria)
**Origen:** `nextlevelbuilder/ui-ux-pro-max-skill@d14efff8ed1faa4187f004f79926f428c8074ec7`, `.claude/skills/ui-ux-pro-max/SKILL.md` y `references/quick-reference.md`. Licencia del repo MIT. Esta adaptación **no instala** las tablas, búsquedas ni ejecutables del upstream.

## Consulta proporcional
- Ante fallo visual concreto, primero describir resultado humano observable (ej. botón tapado en móvil, texto ilegible, foco oculto), el stack real detectado y el viewport/rol. No asumir React/Tailwind si el proyecto es PHP, Flutter o WinForms.
- Consultar **una sola categoría** necesaria (accesibilidad, layout/responsive, touch, tipografía, navegación, estados, performance visible) antes de buscar otras. Si existe skill instalada, usar su búsqueda de dominio o stack documentada; no ejecutar scripts desde repos externos sin inspección.
- Para un diseño nuevo sin referencias aprobadas puede orientar un sistema consistente; **si existe mockup/MASTER del producto, respetarlo** y no regenerarlo ni usar `--force`.
- Aceptar solo recomendaciones pertinentes al stack y UX del proyecto. No imponer un umbral o patrón sin verificar aplicabilidad y norma de accesibilidad/tecnología del caso.
- Contrastar con UI renderizada y pruebas de teclado/touch cuando existan herramientas; sin evidencia, `RECOMENDACIÓN_ESTÁTICA`, no `VISUAL_PASS`.

**Fallo de fuente:** `UPSTREAM_NO_CONSULTADO` si no se pudo acceder a referencias actuales; jamás afirmar que se ejecutó su buscador o persistió diseño si no ocurrió.
**Integración:** la ruta Anti UI Slop precede a esta solo cuando el encargo requiere ambas; evitar dos auditorías completas repetidas.
