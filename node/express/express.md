## Install Express
    npm i nodemon eslint eslint-config-prettier eslint-plugin-prettier prettier -D

## Config project

package.json

    {
      "name": "my-store",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "dev": "nodemon index.js",
        "start": "node index.js",
        "lint": "eslint"
      },
      "keywords": [],
      "author": "",
      "license": "MIT",
      "devDependencies": {
        "eslint": "^8.39.0",
        "eslint-config-prettier": "^8.8.0",
        "eslint-plugin-prettier": "^4.2.1",
        "nodemon": "^2.0.22",
        "prettier": "^2.8.8"
      }
    }

.editor.config

    # Editor configuration, see https://editorconfig.org
    root = true

    [*]
    charset = utf-8
    indent_style = space
    indent_size = 2
    insert_final_newline = true
    trim_trailing_whitespace = true

    [*.js]
    quote_type = single

    [*.md]
    max_line_length = off
    trim_trailing_whitespace = false

.eslintrc.json

    {
      "parserOptions": {
        "ecmaVersion": 2018
      },
      "extends": [
        "eslint:recommended",
        "prettier"
      ],
      "env": {
        "es6": true,
        "node": true,
        "jest": true
      },
      "rules": {
        "no-console": "warn"
      }
    }
