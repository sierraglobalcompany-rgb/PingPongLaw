---
name: pingponglaw
description: Aplica las seis leyes de PingPongLaw, KISS Ponytail, QA verdadero, diseño humano y coordinación antiping-pong a tareas de programación y revisión.
---

# Skill PingPongLaw — versión de proyecto

1. Leer AGENTS.md y docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md; verificar SHA/repo y permisos. No inventar lectura.
2. **Escalera L1:** ¿necesita existir? → ¿ya hay implementación del repo? → ¿stdlib o plataforma nativa? → ¿dependencia instalada? → ¿código mínimo completo y legible? Leer contratos, consumidores y regresiones antes de editar.
3. L2: evitar duplicados con prueba de uso. L3: causa raíz sin parches. L4: usar SPEC/mockup y fuentes UX si aportan valor. L5: no aprobar sin ejecución y evidencia. L6: ChatGPT primero; Codex autonomía técnica acotada dentro del lote.
4. Autonomía Codex: recuperar errores mecánicos seguros, aislar QA bloqueada y continuar lo independiente. No modificar negocio, esquema de BD real, permisos, seguridad, diseño aprobado ni remoto sin autorización.
5. Usar revisión focal para cambios focales. Ejecutar audit de Ponytail solo cuando el usuario pida auditoría o un riesgo transversal real la justifique. No encadenar prefiltro → auditoría → otra auditoría automáticamente.
6. Informe final: alcance; HEAD/archivos; pruebas reales y pendientes; estado; riesgos; NEXT o NINGUNO; MD obligatorio y ZIP condicional si hay evidencias.

**Procedencia:** adaptación propia inspirada en Ponytail 5.3.2 de DietrichGebert/ponytail, commit 09c434ab73ca43761c5d8b0c5d341926c2fba710, licencia upstream MIT. Esto NO significa plugin oficial ni hooks instalados.

## Enrutamiento operativo — NO cargar todo por rutina
**Antes:** identificar intención, permiso, archivos afectados, riesgos, SHA y objetivo. Leer una vez el canon y `AGENTS.md`; consultar solo skills aplicables, no ejecutar automáticamente ocho auditorías.
- Implementación/refactor/arquitectura → `l1-kiss-ponytail`; si hay duplicidad demostrable → `l2-antirruido`; si es bug o workaround → `l3-antiparches`.
- Cambio visible, experiencia de usuario, layout o accesibilidad → `l4-diseno-humano`; este dirige `l4-anti-ui-slop` y/o `l4-ui-ux-pro-max` según necesidad. Sin visual no activar L4 externamente.
- Aceptación de entrega/QA/contraste de informe → `l5-verificacion-independiente`, sin fingir auditor independiente.
- Antes de delegar, repetir auditoría o generar un NEXT → `l6-anti-ping-pong`: ejecutar primero lo que ChatGPT pueda y agrupar lo restante.
**Al cerrar:** comprobar aplicabilidad de L1–L6 en una línea cada una cuando sea importante; no releer 48 KB sin cambio del canon. Distinguir `SKILL_DOCUMENTADA`, `SKILL_LEIDA`, `PLUGIN_INSTALADO`, `HOOKS_OBSERVADOS`.
Leer `docs/SKILLS_ARQUITECTURA.md` para selección y provenance; esto es un **índice de navegación**, no nueva norma.
