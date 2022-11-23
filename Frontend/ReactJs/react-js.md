## React.js
- Se considera una librería
- A medida que cambia el ecosistema se convierte en un framework progresivo

## Flujos de trabajo
### Modelo en cascada
El equipo desarrolla su parate hasta construir la aplicación. Toma bastante tiempo hasta recibir el feedback del usuario.
- Diseño, desarrollo, test

### MVP iterativo
Minimum Viable Product. Se desarrollan y lanzan pequeñas funcionalidades completas de la aplicación para poder obtener feedback del usuario y decidir si seguir por el camino planteado o probar otro.

## create-react-app package.json
    {
    "name": "lab-tools-app",
    "version": "0.1.0",
    "private": true,
    "dependencies": {
        "cra-template": "1.2.0",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-scripts": "5.0.1"
    },
    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject"
    },
    "eslintConfig": {
        "extends": [
        "react-app",
        "react-app/jest"
        ]
    },
    "browserslist": {
        "production": [
        ">0.2%",
        "not dead",
        "not op_mini all"
        ],
        "development": [
        "last 1 chrome version",
        "last 1 firefox version",
        "last 1 safari version"
        ]
    }
    }
