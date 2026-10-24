# Integración de PingPongLaw en repositorios de aplicaciones

## Principio: un canon, adaptadores mínimos por proyecto

El documento principal vive en PingPongLaw; cada aplicación conserva sus propias reglas, SPEC, CI y bloqueos. No copiar el repositorio completo de Ponytail ni sus hooks al árbol de la app.

### Preflight por repo

1. Confirmar owner/repo, branch, SHA, permisos y cambios preexistentes; localizar AGENTS.md raíz y anidados, reglas override, README/continuidad, contratos y políticas de reportes.
2. Comparar leyes L1–L6 semánticamente, no por coincidencia de nombres: estado PRESENTE / INCOMPLETO / CONFLICTO / AUSENTE / NO_VERIFICADO.
3. Si existe canon local equivalente, actualizarlo por diff mínimo. Si necesita operar offline, mantener un **snapshot versionado y verificable** de PingPongLaw con fuente/commit, NO una segunda norma divergente.
4. AGENTS puede enlazar la URL del canon con SHA fijo y una instrucción expresa de lectura; se debe comprobar que Codex dispone de acceso. Si Codex no tiene red, instalar snapshot local autorizado.
5. No reemplazar AGENTS existente por el AGENTS de Ponytail ni por el de este repo. Conservar restricciones específicas: permisos, multiempresa, seguridad, proceso de fabricación, políticas de ZIP y branches.
6. Probar un prompt de inicio y fin de tarea; el agente debe decir qué leyes realmente leyó y qué ejecutó, sin falsos PASS.

## Ejemplo mínimo para AGENTS del proyecto

```markdown
## PingPongLaw / seis leyes
Antes de desarrollar o revisar, consultar el canon PingPongLaw
en https://github.com/sierraglobalcompany-rgb/PingPongLaw
(commit de versión aprobado, no main móvil), y la copia local si existe.
Aplicar L1 KISS + Ponytail, L2 Antirruido, L3 Antiparches,
L4 Diseño humano, L5 Verificación independiente y L6 Antiping-pong.
No ignorar reglas específicas ni afirmar lectura no comprobada.
No iniciar auditorías globales automáticamente; conservar tests y seguridad.
```

**Importante:** una URL de canon en AGENTS no garantiza lectura automática: prueba con el agente real y registra `CANON_READ=PASS/NOT_VERIFIED`.

## PRs previos de adaptación Ponytail

Existen 14 PRs borrador creados previamente en repositorios asociados, con una skill local y referencia a AGENTS; al ejecutar F4/F5 **no duplicar esos PRs ni fusionarlos por costumbre**. Revisar HEAD/diff/CI de cada uno, reconciliar su ruta `.agents/skills/kiss-ponytail` con este canon y aplicar solo diferencias justificadas. Los repositorios vacíos o con default branch de trabajo requieren decisión de destino antes de instalar.

## Conflictos típicos

- Si una app prohíbe ZIP salvo solicitud: una orden explícita del usuario y las políticas de esa app definen si se puede generar; documentar conflicto si no se puede cumplir. No eliminar esa regla sin revisión.
- Si una app exige tests extensos: Ponytail no autoriza saltarlos aunque prefiera una prueba pequeña por lógica nueva.
- Si una app tiene mockup aprobado: Ponytail no autoriza rediseño o botones inventados.
- Si ChatGPT no tiene acceso local: puede hacer análisis/edición GitHub autorizados; delegar una sola prueba local razonada, sin pedir al usuario copias de archivos que ya son accesibles por herramienta.

## Rollout seguro

Elegir piloto con alta representación, comparar base/HEAD, crear PR focal si hace falta, probar instrucciones y un cambio pequeño de código, y aprobar por Ley 5. Solo después extender a otros proyectos, uno por repo y sin merge automático.
