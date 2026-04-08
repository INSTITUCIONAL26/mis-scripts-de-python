# Validation Utilities

Este proyecto proporciona un conjunto de utilidades para la validación de datos comunes, incluyendo DNI, fechas y correos electrónicos. Las funciones de validación están diseñadas para ser fáciles de usar y se pueden integrar fácilmente en cualquier aplicación TypeScript.

## Estructura del Proyecto

- **src/**: Contiene el código fuente de las utilidades de validación.
  - **index.ts**: Punto de entrada de la aplicación.
  - **validators/**: Contiene las funciones de validación.
    - **dni.ts**: Valida el formato de un DNI.
    - **date.ts**: Valida si una cadena es una fecha válida.
    - **email.ts**: Valida si una cadena es un correo electrónico válido.
    - **index.ts**: Exporta todas las funciones de validación.
  - **utils/**: Contiene utilidades adicionales.
    - **normalize.ts**: Normaliza cadenas de texto.
  - **types/**: Contiene definiciones de tipos e interfaces.
    - **index.ts**: Define la estructura de los resultados de las validaciones.

- **test/**: Contiene pruebas unitarias para las funciones de validación.
  - **validators/**: Pruebas para las funciones de validación.
    - **dni.test.ts**: Pruebas para la función de validación de DNI.
    - **date.test.ts**: Pruebas para la función de validación de fechas.

## Instalación

Para instalar las dependencias del proyecto, ejecute:

```
npm install
```

## Uso

Para utilizar las funciones de validación, importe las funciones necesarias desde el módulo de validadores. Por ejemplo:

```typescript
import { validateDNI, validateDate, validateEmail } from './validators';
```

## Pruebas

Para ejecutar las pruebas, use el siguiente comando:

```
npm test
```

Esto ejecutará todas las pruebas definidas en el directorio `test/`.

## Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir, por favor abra un issue o un pull request en el repositorio.