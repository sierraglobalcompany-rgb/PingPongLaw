# AGENTS.md — PingPongLaw: entrada obligatoria

**Inicio:** leer docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md (las seis leyes completas) y, para código, .agents/skills/pingponglaw/SKILL.md. Comprobar que la lectura ocurrió realmente. Si no está disponible: CANON_NO_LEIDO; no afirmar cumplimiento.

1. **L1 KISS + Ponytail:** comprender flujo y consumidores; no crear lo innecesario; reutilizar código; biblioteca estándar/plataforma; dependencia existente; mínimo código nuevo legible. Nunca recortar seguridad, datos, validaciones, accesibilidad o QA obligatoria.
2. **L2 Antirruido:** no duplicar código, documentación ni pruebas; no retirar lo incierto.
3. **L3 Antiparches:** corregir causa raíz, consumidores, contratos y regresiones.
4. **L4 Diseño:** SPEC/mockup humano aprobado primero; Anti UI Slop y UI UX Pro Max son guías de apoyo; no inventar funciones.
5. **L5 Verificación:** PASS requiere pruebas genuinas sobre SHA/build y revisor apropiado; autor ≠ auditor externo.
6. **L6 Antiping-pong:** ChatGPT dirige y realiza lo posible con sus herramientas; Codex ejecuta lote coherente cuando hace falta entorno local, resuelve impedimentos técnicos seguros y documenta los bloqueos.

**Prohibiciones:** nunca modificar otro proyecto, ramas, producción, secretos, datos reales, permisos o hooks de terceros sin autorización adecuada. No lanzar ponytail-audit ni auditoría forense por ritual.
**Cierre:** L1–L6 aplicables, cambios/artefactos, pruebas PASS/FAIL/BLOCKED/NOT_RUN y NEXT único o NINGUNO. Cada entrega de Codex debe contar con informe Markdown y, cuando haya evidencias físicas, ZIP en la misma carpeta autorizada respetando las políticas específicas.

**Para ChatGPT:** consultar docs/CHATGPT_START.md explícitamente; GitHub no carga estas instrucciones de forma automática en cualquier chat.

## Selección de skills (no ejecución automática)
El índice de skills está en `docs/SKILLS_ARQUITECTURA.md`. Usar `.agents/skills/pingponglaw/SKILL.md` como router; cada ley tiene su skill `l1`–`l6` y L4 dispone de dos adaptadores de referencias externas. Consultar solo las necesarias según tipo de tarea y comprobar sus rutas. Una skill en GitHub es **instrucción versionada**, no prueba de que Codex la cargó ni de que ChatGPT la leyó.
