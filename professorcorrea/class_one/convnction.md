# Convenções de Nomenclatura em Python

Este guia resume as convenções mais utilizadas na comunidade Python, seguindo **PEP 8**.

## Nomenclatura de texto

Serve para unir várias palavras sem utilizar espaços...

Lucas Correa

### kebab-case
lucas-correa
### snake_case
lucas_correa
### PascalCase
LucasCorrea
### camelCase
lucasCorrea


## Regras

### Arquivos

Utilize **snake_case**

* exemplos: 
```text
user_service.py
database.py
email_sender.py
config_loader,py
```

* errado;

```text
UserService.py
user-service.py
User_Service.py
```

### Pastas/Diretórios

Utilize **snake_case**, preferencialmente com nomes curtos.

* certo:

```text
models/
services/
repositories/
utils/
```

* errado

```text
exemplo de pasta/
errado dois/
```
