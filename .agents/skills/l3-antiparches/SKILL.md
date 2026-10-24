---
name: l3-antiparches
description: Ley 3 Antiparches. Investigar regresiones, workaround sobre workaround y errores persistentes; localizar causa raíz y cerrar todos los consumidores, sin añadir parches acumulativos.
---
# L3 — Antiparches
**Canon:** docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md (L3).
## Secuencia
1. Describir síntoma, entrada, resultado esperado, resultado observado y alcance; no inventar reproducción.
2. Rastrear flujo real `entrada → validación/rol → transformación → persistencia/UI → salida` y revisar callers directos/dinámicos.
3. Obtener hipótesis de causa raíz con evidencia; una observación de CI no prueba por sí sola que se entendió la causa.
4. Diseñar **una corrección coherente** en el punto de autoridad; descartar excepciones dispersas, flags nuevos y reintentos infinitos.
5. Ajustar consumidores, errores, pruebas y documentación realmente afectados. No romper compatibilidad ni contratos aprobados.
6. Reproducir la falla antes y la corrección después cuando sea seguro y el entorno lo permita. Diferenciar `REPRODUCIDO`, `ESTÁTICO`, `NO_REPRODUCIDO`, `BLOQUEADO`.

## Stop
No ocultar problemas de autenticación, integridad, dinero, permisos o seguridad bajo fallback silencioso. No inventar una capa de compatibilidad temporal sin límite verificable.
**Salida:** `SÍNTOMA | CAUSA | EVIDENCIA | CORRECCIÓN ÚNICA | CONSUMIDORES | PRUEBAS | RIESGO` y NEXT/NINGUNO.
