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
1. Hadoop cluster
2. Apache Spark
3. Python Library (pyspark 3.5.1 and spark-nlp 6.1.0)

