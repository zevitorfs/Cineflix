# codeflix-catalog-admin
Administração de Catálogo - Codeflix - Python

## Regras Category
- [X]Nome da categoria deverá ser obrigatório.
- [x]Nome devera ter no maximo 255 caracteres
- Ao criar uma nova categoria um identificador deve ser gerado no formato (uuid).
- Ao criar uma categoria os campos id, descrição e isActive não serão obrigatórios.
- Caso a propriedade isActive nao seja informada, devera receber como default o valor true.
- Teste _str_
- Teste _repr