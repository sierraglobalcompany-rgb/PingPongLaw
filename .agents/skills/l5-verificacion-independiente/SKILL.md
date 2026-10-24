---
name: l5-verificacion-independiente
description: Ley 5. Validar entregas de ChatGPT/Codex, PRs, código, UI, tests y evidencias sin aceptar PASS autoproducido; separar verificación de implementación.
---
# L5 — Verificación independiente de entregas
**Canon:** `docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md` (L5).
## Método
1. Fijar `REPO, BASE_SHA, HEAD_SHA, BUILD_ID` pertinentes y contrato aprobado (SPEC/mockup/permiso).
2. Separar **afirmación**, **evidencia del ejecutor** y **comprobación independiente**. CI de otra revisión o pruebas antes del último cambio no certifican el HEAD.
3. Contrastar diff y consumidores, resultados de tests, logs pertinentes y, si aplica, navegador/render reales; no inventar capturas, pruebas o logs. No reejecutar suites caras sin razón si evidencia válida del SHA actual ya cubre criterio.
4. Buscar falsos positivos y negativos: defectos no reportados, pruebas omitidas, permisos/roles y regresiones. Resultado por hallazgo `CONFIRMADO/REFUTADO/PARCIAL/NO_VERIFICABLE`.
5. Si el agente que implementa también revisa, su QA es autocontrol **no independiente**. Pedir agente/revisor distinto o contraste externo cuando el riesgo lo exige; no fingir independencia.

## Gate
`APROBADO_FOCAL` solo cuando criterios del alcance fueron observados; de lo contrario `PARCIAL/FAIL/BLOCKED/NOT_RUN` con razones concretas. No detener implementación independiente por una prueba que únicamente bloquea aceptación.
**Entregables:** informe Markdown siempre que el ejecutor pueda escribir; ZIP de evidencias si hay ficheros y la política del proyecto lo permite, misma carpeta. No copiar secretos. Un NEXT o NINGUNO.
