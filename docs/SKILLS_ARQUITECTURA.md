# Arquitectura de skills — PingPongLaw

**Estado:** arquitectura documental; cada `SKILL.md` se activa **solo si el agente realmente lo leyó o su host lo descubrió**. La presencia en GitHub no garantiza activación automática en ChatGPT ni Codex. **Canon único:** `docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md`. Aquí solo se define el enrutamiento.

## Inventario y titularidad

| Propósito | Archivo propio | Disparador | Resultado |
|---|---|---|---|
| Router | `.agents/skills/pingponglaw/SKILL.md` | Inicio de tarea de ingeniería / petición explícita de PingPongLaw | Selecciona las leyes aplicables sin invocarlas en cascada |
| **L1 KISS + Ponytail** | `.agents/skills/l1-kiss-ponytail/SKILL.md` | Implementación, simplificación o arquitectura | Alternativa mínima completa, consumidores y regresión |
| **L2 Antirruido** | `.agents/skills/l2-antirruido/SKILL.md` | Redundancia observada / limpieza solicitada | Equivalencia demostrada antes de fusionar/eliminar |
| **L3 Antiparches** | `.agents/skills/l3-antiparches/SKILL.md` | Fallo, workaround, regresión | Causa raíz y corrección integrada |
| **L4 Diseño humano** | `.agents/skills/l4-diseno-humano/SKILL.md` | UI/UX, flujo humano, visibilidad y accesibilidad | Contrato visual y prueba real por rol/estado/viewport |
| **L4 / Anti UI Slop** | `.agents/skills/l4-anti-ui-slop/SKILL.md` | Diagnóstico de jerarquía, estado o apariencia genérica | Un playbook upstream pertinente, fallos observables |
| **L4 / UI UX Pro Max** | `.agents/skills/l4-ui-ux-pro-max/SKILL.md` | Accesibilidad, responsive, búsqueda por stack/dominio | Guía complementaria focal, no rediseño automático |
| **L5 Independiente** | `.agents/skills/l5-verificacion-independiente/SKILL.md` | Comprobar entrega, PR, PASS, QA o evidencia | Dictamen conforme al mismo SHA y contrato |
| **L6 Antiping-pong** | `.agents/skills/l6-anti-ping-pong/SKILL.md` | Auditar/delegar/repetir/continuar, antes de enviar Codex | Trabajo directo ChatGPT o un solo lote coherente de Codex |

Son **9 skills propios** (router + 6 leyes + 2 adaptadores de fuentes de L4), **no nueve leyes**. No instalar 9 plugins ni generar 9 informes. No duplicar el texto íntegro de 48 KB del canon en las skills.

## Selector obligatorio y deliberadamente pequeño

`INTENCIÓN → RESPONSABLE → SKILL`
- ¿Quieres **implementar**? ChatGPT ejecuta lo accesible; usar L1. Añadir L3 si se corrige bug, L2 si hay duplicidad probada, L4 si impacta UI. Cerrar con criterio L5 proporcional. Aplicar filtro L6 antes de delegar.
- ¿Quieres **auditar un repo entero**? Es solicitado: primero identificar SHA/branch/contratos, inventariar módulos y analizar riesgo. Usar L1/L2/L3/L4/L5/L6 como **dimensiones** del mismo informe, no seis auditorías separadas. Los adaptadores L4 solo ante UI real.
- ¿Quieres **simplificar**? L1→L2 si se comprueba redundancia→L3 si es parche. No recortar funcionalidades aprobadas. Conservar validación/L5.
- ¿Quieres **diseño**? Contrato aprobado→Anti UI Slop para defectos concretos→UI UX Pro Max para reglas accesibilidad/stack aún no resueltas→capturas y aceptación L5. Si primera pasada basta, omitir la segunda dejando razón.
- ¿Quieres **verificar a Codex**? L5 primero. No reenviar NEXT automáticamente; L6 cuestiona si hay un trabajo real pendiente.
- ¿Quieres **otro prompt/auditoría**? L6 pregunta para qué, por qué, qué decisión cambiará y si ChatGPT puede implementar. Si no hay nueva utilidad, no crear prompt ni auditoría.

## Jerarquía, prevención de conflictos y garantías

1. Usuario y restricciones de plataforma/herramienta/permisos; SPEC/mockup/contrato aprobado y leyes del proyecto. Skills externas son **referencias**, no autorizan funciones, cambios de alcance ni QA menor.
2. Canon L1–L6 en el SHA fijado; `AGENTS.md` y reglas anidadas del proyecto destino. Conflicto material → resolver con evidencia y permiso, no sobrescribir a ciegas.
3. Router decide una ruta; subskill aporta criterios, no abre trabajo infinito. Un único objetivo y un único reporte final.
4. **L5 no es autonota**: pruebas del implementador son QA interno; una verificación independiente requiere segunda perspectiva/herramienta/evidencia y no puede declararse sin ella.
5. **L6 ChatGPT primero**: no declarar «99,99 %» por promesa. Reportar capacidad real; Codex solo operación que no se pueda ejecutar directamente.
6. Accesibilidad, privacidad, integridad, autorización, precisión y errores resistentes siempre prevalecen frente a minimizar líneas.

## Descubrimiento frente a instalación

- **Repositorio PingPongLaw**: guardar SKILL.md en `.agents/skills/<nombre>/SKILL.md` y enlazarlas desde el router. Es una **capacidad documental**.
- **Codex local**: verificar host/versión, ubicación real y que las skills aparezcan o que pueda leerlas. El plugin oficial `DietrichGebert/ponytail` se instala/autoriza aparte, según `docs/CODEX_INSTALL.md`; no afirmar hooks activos solo por un archivo.
- **ChatGPT**: abrir GitHub y leer canon/router/skill seleccionada si hay conexión. No hay "autoload" universal desde un repositorio; adjuntar fuente si no hay acceso.
- **Otros proyectos**: conservar `AGENTS.md` y reglas locales, apuntar a una versión/commit concreto o snapshot autorizado en modo offline. Probar lectura real antes de decir INSTALADO.
- **Fuentes externas de L4**: nuestros adaptadores NO contienen ni ejecutan las bibliotecas de UIZZE o UI UX Pro Max. Consultar upstream solo si aportan valor. Ver `docs/FUENTES_EXTERNAS.md`.

## Gate de carga por tarea (sin ceremonia)

`REPO/SHA | CANON_LEIDO/NO | SKILLS_ELEGIDAS | MOTIVO | EJECUTADO | QA | NEXT/NINGUNO`.

**Inicio:** verificar presencia del canon y 6 leyes, seleccionar 0–3 skills materiales (más si el alcance lo exige); no descargar todas ni reauditar. **Fin:** revisar 6 leyes con criterio de aplicabilidad, pruebas pertinentes y lo no verificado. Si no hubo cambios, evitar reportes de decenas de páginas.

## Controles antirruido

No crear nuevas skills por cada palabra clave, tecnología o microincidencia. Añadir una skill solo cuando existe contrato propio reutilizable y demostrado que el selector actual no cubre la necesidad. Criterio: un problema material sin solución por este mapa; con aprobación y pruebas de no duplicación.

**Prueba de estructura:** `python3 scripts/check_canon.py` y `python3 -m unittest discover -s tests -v`. Solo asegura archivos/contratos/versiones del mapa, NO el comportamiento real de modelos ni el funcionamiento de aplicaciones.
