# Fundamentos de Sistema Embarcados (FSE) - Projeto 1

## Introdução
Esse projeto é um sistema distribuido de controle e monitoramento de um conjunto de cruzamentos com semafóros.
No projeto têm-se um servidor central que é responsável pelo monitoramento dos dados obtidos pelos sensores e pela alteração de modos(Noturno, Emergencia, Padrão).
Além disso, existe um servidor distribuido responsável pelo controle dos sinais de trânsito e obtenção dos dados.

Para mais informações sobre o projeto acesse o Git Lab: [https://gitlab.com/fse_fga/trabalhos-2022_1/trabalho-1-2022-1](https://gitlab.com/fse_fga/trabalhos-2022_1/trabalho-1-2022-1)

## Instruções de execução

- Clone o repositório e acesse a pasta

```
git clone https://github.com/lucasgbezerra/FSE_T1.git
cd FSE_T1/
```
- Execute os servidores como especificado
### Servidor Central
- Abra um terminal e vá para a pasta
```
cd centralServer/
```
- Execute o servidor com o comando: python3 main.py [IP_SERVIDOR] [PORTA]
    - Para executar no simulador por exemplo, basta estar conectado via SSH na raspbery(164.41.98.17 ou 164.41.98.26), fazer os passos já mostrados e usar o comando
```
python3 main.py 164.41.98.17 10262
```

### Servidor Distribuido

- Abra um novo terminal e vá para a pasta
```
cd distributedServer/src/
```
- Execute o servidor com o comando: python3 main.py [CONFIG.json] [IP_SERVIDOR] [PORTA_SERVIDOR_CENTRAL]
    -  Cada cruzamento tem um arquivo CONFIG.json: cruzamento 1 (crossing1.json) e cruzamento 2 (crossing2.json)
    - Para executar no simulador por exemplo, basta estar conectado via SSH na raspbery(164.41.98.17 ou 164.41.98.26), fazer os passos já mostrados e usar o comando
- Cruzamento 1: 
```
python main.py crossing1.json 164.41.98.17 10262
```
- Cruzamento 2:

```
python main.py crossing1.json 164.41.98.17 10262
```

## Uso
- Executando o projeto
![](https://raw.githubusercontent.com/lucasgbezerra/FSE_T1/54b7b718e4a2504dc9b9319bc6f606bb89efcb26/imgs/img2.png)
![](https://raw.githubusercontent.com/lucasgbezerra/FSE_T1/main/imgs/img.png)
