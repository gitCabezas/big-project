# Esquema do Banco de Dados

Este documento detalha a estrutura das tabelas do banco de dados da aplicação, com base nos modelos definidos em `backend/models`.

---

## Tabela: `users`

Armazena as informações dos usuários do sistema.

| Nome da Coluna  | Tipo de Dado      | Restrições/Notas                               |
|-----------------|-------------------|------------------------------------------------|
| `id`            | Integer           | Chave Primária                                 |
| `username`      | String(80)        | Único, Não Nulo                                |
| `email`         | String(120)       | Único, Não Nulo                                |
| `password_hash` | String(256)       | Não Nulo                                       |
| `created_at`    | DateTime          | Padrão: data e hora atuais (UTC)               |

---

## Tabela: `clients`

Armazena os dados dos clientes da tinturaria.

| Nome da Coluna   | Tipo de Dado      | Restrições/Notas                               |
|------------------|-------------------|------------------------------------------------|
| `id`             | Integer           | Chave Primária                                 |
| `name`           | String(120)       | Não Nulo                                       |
| `cnpj_cpf`       | String(18)        | Único, Não Nulo                                |
| `address`        | String(255)       | Opcional                                       |
| `contact`        | String(120)       | Opcional                                       |
| `observations`   | Text              | Opcional                                       |
| `is_active`      | Boolean           | Padrão: `True`, Não Nulo                       |

---

## Tabela: `raw_materials`

Catálogo de matérias-primas (ex: tipos de malha).

| Nome da Coluna            | Tipo de Dado      | Restrições/Notas                               |
|---------------------------|-------------------|------------------------------------------------|
| `id`                      | Integer           | Chave Primária                                 |
| `name`                    | String(100)       | Único, Não Nulo                                |
| `type`                    | String(50)        | Não Nulo (Ex: Algodão, Poliéster)              |
| `supplier`                | String(100)       | Opcional                                       |
| `technical_characteristics` | Text              | Opcional                                       |
| `stock_quantity`          | Float             | Padrão: `0.0`, Não Nulo                        |

---

## Tabela: `dyes`

Catálogo de corantes utilizados nos tingimentos.

| Nome da Coluna      | Tipo de Dado      | Restrições/Notas                               |
|---------------------|-------------------|------------------------------------------------|
| `id`                | Integer           | Chave Primária                                 |
| `commercial_name`   | String(100)       | Não Nulo                                       |
| `code`              | String(50)        | Único, Não Nulo                                |
| `manufacturer`      | String(100)       | Opcional                                       |
| `type`              | String(50)        | Opcional (Ex: Reativo, Direto)                 |
| `concentration`     | Float             | Opcional                                       |
| `validity`          | DateTime          | Opcional                                       |
| `stock_quantity`    | Float             | Padrão: `0.0`, Não Nulo                        |
| `lot_number`        | String(50)        | Opcional                                       |

---

## Tabela: `chemical_inputs`

Catálogo de insumos químicos (produtos auxiliares).

| Nome da Coluna            | Tipo de Dado      | Restrições/Notas                               |
|---------------------------|-------------------|------------------------------------------------|
| `id`                      | Integer           | Chave Primária                                 |
| `name`                    | String(100)       | Único, Não Nulo                                |
| `function`                | String(100)       | Opcional (Ex: Auxiliar, Fixador)               |
| `supplier`                | String(100)       | Opcional                                       |
| `concentration`           | Float             | Opcional                                       |
| `safety_data_sheet_url`   | String(255)       | Opcional                                       |
| `validity`                | DateTime          | Opcional                                       |
| `stock_quantity`          | Float             | Padrão: `0.0`, Não Nulo                        |

---

## Tabela: `colors`

Catálogo de cores, com referências Pantone/RGB e de clientes.

| Nome da Coluna       | Tipo de Dado      | Restrições/Notas                               |
|----------------------|-------------------|------------------------------------------------|
| `id`                 | Integer           | Chave Primária                                 |
| `name`               | String(100)       | Único, Não Nulo                                |
| `pantone_rgb`        | String(50)        | Opcional                                       |
| `client_reference`   | String(100)       | Opcional                                       |

---

## Tabela: `recipes`

Armazena as receitas de tingimento, que unem os demais cadastros.

| Nome da Coluna  | Tipo de Dado      | Restrições/Notas                               |
|-----------------|-------------------|------------------------------------------------|
| `id`            | Integer           | Chave Primária                                 |
| `name`          | String(255)       | Não Nulo                                       |
| `client_id`     | Integer           | Chave Estrangeira para `clients.id`, Não Nulo  |
| `article`       | String(100)       | Opcional                                       |
| `process`       | String(100)       | Opcional                                       |
| `substrate`     | String(100)       | Opcional                                       |
| `machine`       | String(100)       | Opcional                                       |
| `weight_kg`     | Float             | Opcional                                       |
| `status`        | String(50)        | Padrão: `'rascunho'`                           |
| `created_at`    | DateTime          | Padrão: data e hora atuais (UTC)               |
| `updated_at`    | DateTime          | Atualiza na modificação                        |

### Relacionamentos

-   **`recipes.client_id` -> `clients.id`**: Uma receita pertence a um cliente. Um cliente pode ter várias receitas.
