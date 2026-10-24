---
name: l4-anti-ui-slop
description: Adaptador de Anti UI Slop para diseñar o auditar UI humana con evidencia observable. Activar solo en tareas visuales que requieran revisar jerarquía, estados, flujo o apariencia genérica.
---
# L4A — Anti UI Slop (fuente externa; adaptación, no instalación upstream)
**Origen:** `github/awesome-copilot@d85f762d6e521abf5fe16703946e9b38adc42da7`, `skills/anti-ui-slop/SKILL.md` y `reference/audit.md`.
**Condición:** el repositorio externo mantiene metadatos de licencia heterogéneos (frontmatter SKILL: MIT; archivo de distribución LICENSE y MANIFEST: Apache-2.0). No copiar/republicar contenido upstream hasta aclarar distribución y avisos. Esta skill contiene instrucciones originales de integración.

## Uso
1. Leer objetivos, componentes y tokens aprobados del producto, no elegir un estilo genérico por gusto.
2. Si se puede acceder a fuente upstream, cargar solo `SKILL.md` y el **playbook que corresponde**: `reference/audit.md` para revisión, `reference/operate.md` para trabajo de producto, `reference/polish.md` para detalle, etc. No cargar todos juntos.
3. Evaluar si lo visible es propio del producto, si jerarquía conduce la tarea, si hay clipping/overlap y si estados vacíos, errores, loading o acciones inaccesibles perjudican personas.
4. Solo declarar defecto con caso observable (vista/rol/viewport/estado/captura o código inequívoco). Referir hasta tres prioridades principales del playbook sin ocultar defectos críticos cuando un informe forense pide inventario amplio.
5. Proponer mínima corrección coherente con SPEC/mockup. No inventar pantallas ni reemplazar el sistema de diseño.

**Fallo de fuente:** si no se puede leer la skill oficial, `UPSTREAM_NO_CONSULTADO` y aplicar solo estas heurísticas explícitas; no afirmar ejecución de UIZZE ni MCP de pago.
**Integración:** Ley 4 es propietaria de decisión; Ley 5 verifica en navegador real.
