---
name: l4-diseno-humano
description: Ley 4 Diseño humano. Activar solo ante cambios visibles/UX, auditorías visuales o flujos; coordina primero Anti UI Slop y después UI UX Pro Max, sin sustituir el mockup aprobado.
---
# L4 — Diseño UX/UI humano, legible y verificable
**Canon:** `docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md` (L4).
**Primero:** requisito de usuario + SPEC/mockup aprobado + design system y componentes existentes + rol/estado/dispositivo. Estos prevalecen frente a sugerencias externas.

## Dos fuentes, responsabilidades diferentes
1. **Anti UI Slop:** aplicar `l4-anti-ui-slop`. Para auditoría, cargar solo `reference/audit.md` del upstream cuando esté accesible; detectar hallazgos **observables** sobre jerarquía, contenido, estados, clipping, superposición y flujo humano. Su salida breve prioriza hasta tres problemas materiales, no limita el inventario forense principal.
2. **UI UX Pro Max:** aplicar `l4-ui-ux-pro-max` como pasada complementaria: accesibilidad, teclado, labels, contrastes, áreas táctiles, responsive, tipografía, feedback y reglas específicas de stack. Búsqueda focal, no barrido de miles de sugerencias.

## Contrato de producto
- No inventar botones, estados, rutas, textos de negocio o interacciones.
- Revisar portada/estado vacío/carga/error/éxito/permisos y navegación humana según contexto aplicable, no checklist rígida.
- Si existe herramienta render/browser, probar roles/estados/viewport y evidenciar capturas auténticas. Sin render, marcar `DISEÑO_ESTÁTICO_NO_VERIFICADO_VISUALMENTE`.
- No exigir ambas fuentes si la tarea es backend sin efecto visual. Si hay una sola anomalía evidente, comprobarla y corregirla sin abrir dos auditorías completas.
- Ley 5 decide aceptación funcional y visual; ambas fuentes son consulta, no juez final.

**Salida:** vista/rol/estado, defecto concreto, impacto humano, evidencia y solución mínima compatible con mockup, pruebas reales.
