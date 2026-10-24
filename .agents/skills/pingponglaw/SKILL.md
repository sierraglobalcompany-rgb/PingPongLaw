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
