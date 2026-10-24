# PingPongLaw — seis leyes de ingeniería, KISS + Ponytail

**Propósito:** un solo canon legible por ChatGPT, Codex y otros agentes para desarrollar software simple, completo, seguro y sin ping-pong. No es un framework de aplicación ni un fork de Ponytail.

## Seis leyes

1. **L1 KISS + Ponytail:** menor solución completa y legible; primero reutilizar, luego biblioteca estándar/nativo y dependencias existentes, por último código nuevo.
2. **L2 Antirruido:** eliminar/fusionar duplicados solo tras verificar usos y dependencias.
3. **L3 Antiparches:** reparar causas raíz y todos los consumidores afectados.
4. **L4 Diseño humano:** UX/UI accesible, responsive, coherente con SPEC y mockups; fuentes de apoyo Anti UI Slop y UI UX Pro Max.
5. **L5 Verificación independiente:** nunca declarar PASS sin pruebas reales atribuibles al mismo SHA/build.
6. **L6 Antiping-pong:** ChatGPT es director técnico y ejecuta lo que sus herramientas permiten; Codex recibe lotes coherentes para las operaciones que requieren su entorno.

**Estado de la instalación:** este repositorio aloja instrucciones y documentación; la presencia de archivos no prueba instalación del plugin ni aceptación de hooks en el PC. No realizar auditorías globales por costumbre.

## Cómo usarlo

- **ChatGPT:** abrir este repositorio, consultar `docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md` y seguir `docs/CHATGPT_START.md` antes de proponer implementación o delegación.
- **Codex:** leer `AGENTS.md` y el canon; para tareas de ingeniería consultar la skill local `.agents/skills/pingponglaw/SKILL.md`. Instalar Ponytail oficial aparte, con revisión explícita de hooks.
- **Proyectos existentes:** integrar el enlace mínimo a este canon y reconciliar con sus normas propias, sin copiar documentos y sin autoactivar auditorías.

## Fuentes

- [Ponytail original](https://github.com/DietrichGebert/ponytail), v5.3.2, revisión fijada `09c434ab73ca43761c5d8b0c5d341926c2fba710`, licencia MIT; las métricas publicadas proceden del autor, no de pruebas en nuestros proyectos.
- [Anti UI Slop](https://github.com/github/awesome-copilot/tree/main/skills/anti-ui-slop) y [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), referencias para L4.

## Seguridad y cambios

Toda actualización importante sigue rama/PR, revisión focal y aceptación L5. Sin merges o despliegues automáticos. Este repositorio **no concede permisos** sobre otras aplicaciones ni sobre el equipo local.
