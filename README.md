# Registro de Eventos Ambientais

Script Python que coleta dados de eventos ambientais (como queimadas e desmatamentos) e gera um relatório de análise ao final.

## O que o script faz

1. Pergunta quantos eventos serão registrados
2. Para cada evento, coleta: tipo, país, região, cidade, área afetada e intensidade
3. Valida os dados de entrada (área > 0 e intensidade entre 1 e 10)
4. Calcula métricas gerais e exibe um relatório no terminal

## Como usar

```bash
python script.py
```

Sem dependências externas — roda com Python 3 puro.

## Métricas geradas

- Área total afetada (km²)
- Média de intensidade dos eventos
- Região com mais ocorrências
- Densidade média (ocorrências/km²)
- Evento mais crítico (maior intensidade)

## Observação

Em caso de empate na intensidade máxima, a área é levada em conta, em terceiro caso o primeiro evento registrado é considerado o mais crítico.
