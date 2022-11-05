# **O que é Apache Kafka?**

O Apache Kafka é uma plataforma distribuída de transmissão de dados que é capaz de publicar, subscrever, armazenar e processar fluxos de registro em tempo real.

Essa plataforma foi desenvolvida para processar fluxos de dados provenientes de diversas fontes e entregá-los a vários clientes.

Em resumo, o Apache Kafka movimenta volumes imensos de dados não apenas do ponto A ao ponto B, mas também de A a Z e para qualquer outro local que você precisar simultaneamente.

- [Introduction to Kafka](https://www.youtube.com/watch?v=43d7YWY2w0Y)

- [Mais informações](https://www.redhat.com/pt-br/topics/integration/what-is-apache-kafka)

- [Documentação](https://kafka.apache.org/documentation/)

# **Para que serve ?**

Kafka abstrai os detalhes dos arquivos e fornece uma abstração mais limpa do log como um fluxo de mensagens. Isso permite um processamento de baixa latência e suporte mais fácil para várias fontes de dados e consumo de dados distribuídos.

O Kafka permite usar os tópicos como tabelas, permitindo fazer queries para aquisição de dados, isso pode ser usado para uma arquitetura baseada em Eventos. Essa funcionalidade porém não é tão simples como é descrito na documentação.

# **Como funciona ?**

O Kafka foi escrito nas linguagens de programação Java e Scala. Ele realiza as suas transmissões de maneira assíncrona e pode ser considerado como um sistema distribuído.

Em sua estrutura, o Kafka possui consumers e producers. Para definir esses termos, basta traduzir: os producers são os produtores das mensagens (quem envia e distribui os dados); já os consumers são os consumidores das mensagens (eles se inscrevem em um tópico e ficam ouvindo as mensagem que chegarão).

# **Qual é a Arquitetura ?**

![Arquitetura](Images/Arquitetura.png)

A arquitetura do Apache Kafka é organizada em torno de alguns termos chaves, são eles: messages, topics, producers, consumers groups e os brokers. O Apache Kafka é uma plataforma de stream (fluxo de dados) de alto throughput que desacopla os produtores de dados dos consumidores de dados

# **Quais sao suas dependências ?**

## **Zookeeper**

Zookeeper e Kafka trabalha de forma separada se comunicando entre si.

- Apache Zookeeper é um serviço centralizado para manter informações de configurações e nomenclaturas entre serviços distribuídos. O Kafka utiliza o Zookeeper para sincronizar as configurações entre diferentes clusters.

## **Kafka Connections**

**_Kafka Connect_** é a estrutura de integração de dados declarativa e conectável para Kafka. Ele conecta data sinks e fontes ao Kafka, deixando o resto do ecossistema fazer o que faz tão bem com tópicos cheios de eventos

O **_Kafka Connect_** pode criar um cluster de trabalhadores para tornar o processo de cópia de dados escalável e tolerante à falhas. Os trabalhadores precisam armazenar algumas informações sobre seu status, seu progresso na leitura de dados do armazenamento externo e assim por diante. Para armazenar esses dados, eles usam o Kafka como armazenamento.

![Connections](Images/Kafka%20conect.jpg)

[Video Auxiliar](https://www.youtube.com/watch?v=h44GZk2gkCI)

## **Processamento em Kafka Python**

Para a utilização dos recursos do Kafka, será necessário a utilização do Python, mas é importante saber que vamos presisar de dois scripts o `CONSUMER` eo `PRODUCER`.

[Video Pratico](https://www.youtube.com/watch?v=PppMhofKzy4)

# **Componentes ?**

Kafka tem uns componentes arquiteturais que detalharei a seguir e vai ficar fácil de entender: mensagem, offset, tópico, partition, broker.

- [Componentes](https://atitudereflexiva.wordpress.com/2020/03/05/apache-kafka-introducao/)

- [Conceito de cada componente](https://imasters.com.br/software/apache-kafka-entenda-conceitos-arquiteturas-e-componentes)

- [Video Explicativo](https://www.youtube.com/watch?v=uu6F6yvCXzc)

- [Video da fullcycle](https://www.youtube.com/watch?v=ZztfRR2T-N0)

## **Mensagens (Dados)**

Basicamente, o Kafka trabalha com streaming de dados, com o conceito de Tópicos, onde existe o Produtor e o Consumidor. O Produtor envia suas mensagens para o Tópico e elas ficam lá guardadas até o Consumidor ler esse tópico e pegá-las.

- [Video Explicativo](https://www.youtube.com/watch?v=HHYfCkW_ABY)

## **Streaming (Fluxo de dados)**

O Apache Kafka é incorporado a pipelines de transmissão que compartilham dados entre sistemas e/ou aplicações, bem como a sistemas e aplicações que consomem esses dados. O Apache Kafka é compatível com vários casos de uso, em que alta produtividade e escalabilidade são fatores vitais.

- [Video Explicativo](https://www.youtube.com/watch?v=HHYfCkW_ABY)

## **Tópico**

Um tópico é como categorizamos grupos de mensagens dentro do Kafka. Todas as mensagens enviadas para o Kafka permanecem em um tópico. Como comentado sobre Event Sourcing, mensagens são imutáveis e ordenadas. Para manter a ordenação em um ecossistema de Kafka, os tópicos possuem partições e fatores de replicação.

![Topics](Images/topico.png)

- [Explicação detalhada](https://vepo.github.io/posts/anatomia-de-um-topico)

## **Producer**

O produtor Kafka é conceitualmente muito mais simples que o consumidor, pois não precisa de coordenação de grupo. Um particionador produtor mapeia cada mensagem para uma partição de tópico e o produtor envia uma solicitação de produção para o líder dessa partição.

## **Consumer**

Os consumidores Kafka normalmente fazem parte de um grupo de consumidores. Quando vários consumidores estão inscritos em um tópico e pertencem ao mesmo grupo de consumidores, cada consumidor no grupo receberá mensagens de um subconjunto diferente das partições no tópico.

- [Consumindo mensagens](https://www.ibm.com/docs/pt-br/integration-bus/10.0?topic=bus-consuming-messages-from-kafka-topics)

## **Broker**

O conceito de broker na plataforma do Kafka é nada mais do que praticamente o próprio Kafka, ele é quem gerencia os tópicos, define a forma de armazenamento das mensagens, logs.

- [Video Explicativo](https://www.youtube.com/watch?v=ZLrkv53jqPo)

## **Cluster**

Um cluster Kafka é um sistema que consiste em vários Brokers, Topics e Partitions para ambos. O objetivo principal é distribuir cargas de trabalho igualmente entre réplicas e partições.

![](../../Images/Kafka/Multi-cluster-.gif)

## **Log file**

- Os logs do Apache Kafka são uma coleção de vários segmentos de dados presentes em seu disco, tendo um nome como o de uma partição de tópico de formulário ou qualquer partição de tópico específica. Cada log do Kafka fornece uma representação lógica de um particionamento baseado em tópico exclusivo.

- O login no Apache Kafka traz muitos benefícios, não apenas fornece uma solução padrão do setor para anexar logs de dados, mas também fornece uma solução altamente escalável para armazenar logs de dados. Os logs do Apache Kafka fornecem suporte de integração robusto para vários aplicativos pré-existentes, permitindo que os usuários integrem seus aplicativos usando um passo de configuração fácil de seguir.

![](../../Images/Kafka/logk.webp)

## **Particionamento**

- As partitions ou partições como o próprio nome disse é a camada de partição das mensagens dentro de um tópico, este particionamento garante a elasticidade, tolerância a falha e escalabilidade do Apache Kafka, portanto cada tópico pode ter varias partições em diferentes localidades

- Toda partição de um tópico no Kafka pode ser consumida por um ou mais consumidores, desde que estes estejam em grupos de consumidores separados. Devido ao fato do Kafka ser um sistema distribuído, esses grupos de consumidores podem estar em brokers diferentes geograficamente distribuídos

![](../../Images/Kafka/particoes-kafka.png)

[kafka com python](https://timber.io/blog/hello-world-in-kafka-using-python/)

[kafka instalasao](https://www.youtube.com/watch?v=7nMDJzao31c&t=715s)

## **Réplicas**

Replicação significa simplesmente manter cópias dos dados no cluster para promover o recurso de disponibilidade em qualquer aplicativo. A replicação no Kafka está no nível da partição. Cada partição tem 0 ou mais replicações no cluster.

- [Organização dos dados](https://hevodata.com/learn/kafka-replication/)

## **Segmentos**

Os segmentos ficam dentro das partições e segmentam as informações contidas nos logs files daquela partição, todo tópico possui sua partição e sua segmentação, a segmentação serve para gerenciar a ordenação da informação do log file bem como o tempo que ela ira ficar persistida.

![Segmento](Images/segmento.png)

# **Como usar ?**

- Em sua estrutura, o Kafka possui consumers e producers. Para definir esses termos, basta traduzir: os producers são os produtores das mensagens (quem envia e distribui os dados). Já os consumers são os consumidores das mensagens (eles se inscrevem em um tópico e ficam ouvindo as mensagem que chegarão

- É possível usar um nó KafkaConsumer em um fluxo de mensagens para assinar um tópico especificado em um servidor Kafka. Em seguida, o nó KafkaConsumer recebe mensagens que são publicadas no tópico Kafka como entradas para o fluxo de mensagens.

- Você pode usar o nó KafkaProducer para publicar mensagens que são geradas de dentro do seu fluxo de mensagens para um tópico hospedado em um servidor Kafka . As mensagens publicadas ficam, então, disponíveis para serem recebidas pelos consumidores (assinantes) por meio da leitura do tópico. Você pode usar um nó KafkaConsumer em um fluxo de mensagens para se inscrever em um tópico especificado em um servidor Kafka . Para obter mais informações sobre o uso do nó KafkaConsumer , consulte Consumindo mensagens de Kafka tópicos.

- [Integração](https://cicerojmm.medium.com/processamento-e-an%C3%A1lise-de-dados-em-tempo-real-com-kafka-e-python-952be439b0fb)
- [kafka python exemplo](https://selectfrom.dev/apache-spark-structured-streaming-via-docker-compose-3e1f146384b9)

- [confluent Aprendizado kafka](https://www.confluent.io/online-talks/online-training-fundamentals-for-apache-kafka-v1/?utm_medium=display&utm_source=google&utm_campaign=ch.display_tp.rmkt_tgt.key-page-visit-no-hva_rgn.latam_lng.eng_dv.all_con.kafka-fundamentals-3-part-webinar&utm_term=&creative=akfunseries3part-180Days&device=c&placement=www.youtube.com&gclid=Cj0KCQjwpeaYBhDXARIsAEzItbGuI_i-SiX0OJCM5tYeQ9Lal4EntiKFDBNu4He_7cFnYAohTJ2RfmoaApF5EALw_wcB)

- [Conecta a Rede](https://docs.microsoft.com/pt-br/azure/hdinsight/kafka/apache-kafka-connect-vpn-gateway)

- **MongoDB**

  - [Video](https://www.youtube.com/watch?v=_6NuTTQdDn4)

- **Spark**

  - [Integração](https://www.youtube.com/watch?v=zVgPNjSjua0&t=573s)
  - [Video](https://www.youtube.com/watch?v=2z6scTH_C4c)
  - [Modelo ideal](https://wiadrodanych.pl/big-data/predkosc-apache-spark-gps-komunikacji-miejskiej/)

- **Kubernetes**
  - [Deploy Kubernetes](https://levelup.gitconnected.com/how-to-deploy-apache-kafka-with-kubernetes-9bd5caf7694f)
