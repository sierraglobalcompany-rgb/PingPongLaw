---
name: l1-kiss-ponytail
description: Ley 1 KISS + Ponytail. Usar al implementar, refactorizar, elegir dependencias o simplificar arquitectura; solo auditar un repositorio entero ante solicitud explícita o riesgo sistémico.
---
# L1 — KISS + Ponytail
**Fuente vinculante:** ../../../../docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md (sección L1). Esta skill aplica la ley, no la duplica.

## Preguntas previas
1. ¿Esto necesita existir o está fuera del contrato aprobado?
2. ¿Hay una función/componente del proyecto que ya lo haga? Leer llamadas, contratos, tests, fixtures, configuraciones y accesos dinámicos antes de cambiar.
3. ¿Lo cubre la biblioteca estándar o una función nativa compatible con el sistema existente?
4. ¿Lo cubre una dependencia ya instalada, sin sumar una nueva?
5. ¿Cuál es la solución mínima **completa, legible y mantenible**? No hacer *code golf* ni reestructurar el sistema sin causa.

## Diagnóstico y acción
- Buscar complejidad real: wrappers vacíos, capas especulativas, alternativas no usadas, duplicación demostrada, dependencia injustificada, queries/IO extra.
- Cada hallazgo requiere archivo/función, escenario concreto, consumidores, impacto y alternativa menor. No llamar "muerto" al código no investigado.
- Si el usuario pidió implementar, corregir el problema en el alcance autorizado; si pidió únicamente auditar, solo diagnosticar.
- Mantener: permisos, aislamiento por empresa, seguridad, integridad de datos, comportamiento aprobado, accesibilidad, errores y pruebas necesarias. La menor solución que rompe alguna de estas NO es KISS.
- Si hay lógica riesgosa, dejar prueba que capture el fallo; Ley 5 puede exigir más que una sola prueba.
- Ponytail oficial `ponytail-review` para diff con riesgo y `ponytail-audit` solo para auditoría global justificada. No invocar automáticamente por cada tarea.

## Salida
Decisión: `NO_CAMBIAR/REUTILIZAR/REDUCIR/IMPLEMENTAR`; razón, rutas/callers, diff o propuesta mínima, QA auténtica, riesgos y NEXT/NINGUNO.
**Procedencia:** adaptación original inspirada en https://github.com/DietrichGebert/ponytail, commit 09c434ab73ca43761c5d8b0c5d341926c2fba710, MIT. No equivale a instalación de su plugin ni hooks.
