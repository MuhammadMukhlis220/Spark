# Name Entity Recognition
---

__Just simple example for NER using pyspark__

Named Entity Recognition (NER) is a subtask of Information Extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories such as:
1. Person names
2. Organizations
3. Locations
4. Dates and times
5. Numerical values (e.g., money, percentages)
6. Others, depending on the domain

NER is commonly used in:
- Search engines
- Chatbots
- Customer feedback analysis
- Document classification

## Spark NLP for NER (Named Entity Recognition)

<div style="text-align: justify;"> Spark NLP is an open-source NLP library built on top of Apache Spark, developed by John Snow Labs. It allows large-scale natural language processing with high accuracy and scalability, making it suitable for production environments. </div>
<br>
Spark NLP provides pretrained NER models and also supports custom NER model training using deep learning (e.g., BiLSTM-CRF architecture). The library allows you to run distributed NER processing across large datasets using the power of Apache Spark.

Key Features:
1. Pretrained multilingual NER models
2. Integration with Spark ML pipelines
3. Annotation framework using DocumentAssembler, Tokenizer, Embeddings, and NERModel
4. Support for medical NER with Spark NLP for Healthcare

## Example

__Pre-requisite__
1. Ubuntu OS (Use wsl if you using windows)
2. Hadoop cluster
3. Apache Spark
4. Python Library (pyspark 3.5.1 and spark-nlp 6.1.0)
5. Good internet connection (we need download pretrained model)

Take a look in my fie [nlp-spark-test.py](https://github.com/MuhammadMukhlis220/Spark/blob/main/name-entity-recognition/nlp-spark-test.py), i already insert string `Barack Obama was born in Hawaii. While Mukhlis was born in Jakarta, he had a lot fun in Indonesia. They had meeting in Bali after conference in China` in there.

Run the file using spark submit `spark-submit --driver-memory 6G --executor-memory 6G --packages com.johnsnowlabs.nlp:spark-nlp_2.12:6.1.0`. I am using pretrained model, so it will automatically download the model in Amazon Web Service. Don't worry about the credential because we use the default credential from spark-nlp to download the model. We only need download once if we don't have the model. ALl model downloaded will store in our hdfs automatically. My directory is: `/user/mukhwsl/cache_pretrained`. Change mukhwsl by your user name.

Here the result:
<br>
![Alt Text](https://github.com/MuhammadMukhlis220/Spark/blob/main/nlp-name-entity-recognition/pic/result_1.png)

It will labelling the entity from inserted string. We can combined it as a big dataframe and send the results to data warehouse or etc for production purposes but remember with your platform resources.

__That all, give it a try!__
