---
name: l2-antirruido
description: Ley 2 Antirruido. Detectar redundancia real en código, módulos, documentación, pruebas y procesos; fusionar o eliminar solo con evidencia de consumidores y regresiones.
---
# L2 — Antirruido
**Canon:** ../../../../docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md (L2).
## Operar
- Delimitar objeto: duplicaciones de helpers, flujos, consultas, config, documentos, reportes o pruebas. No confundir similitud visual con equivalencia de comportamiento.
- Inventariar definiciones y consumidores: importaciones, rutas, DI, nombres dinámicos, pruebas, fixtures, cron, pipelines, migraciones, versiones y referencias externas.
- Antes de borrar o unir: comparar firmas, permisos, casos borde, efectos secundarios y contratos; buscar uso activo y razones históricas. `NO_VERIFICADO` significa conservar.
- Elegir `KEEP`, `MERGE`, `DELETE` o `DEFER`; cada intervención requiere justificación y plan de reversión.
- Si corresponde, modificar todos los consumidores y ejecutar pruebas focales. No sustituir diez archivos por un framework o generar otra capa solo para "organizar".
- No borrar logs necesarios, controles de seguridad, trazabilidad, evidencias de Ley 5, instrucciones de otras leyes o funcionalidades aprobadas.

## Criterios
Un hallazgo material demuestra costo o riesgo real de mantener duplicidad y que la consolidación es equivalente. Si no es material, no iniciar auditoría repetida.
**Salida:** tabla breve `objeto → usos → equivalencia → acción → pruebas → riesgo`. Un NEXT o NINGUNO.
