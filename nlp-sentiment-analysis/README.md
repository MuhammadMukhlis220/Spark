# Name Entity Recognition
---

__Just simple example for sentiment analysis using pyspark__

Sentiment Analysis with Spark NLP
Sentiment Analysis is a natural language processing (NLP) task that aims to identify and classify opinions or emotions expressed in text, such as positive, negative, or neutral sentiments. It is widely used in various applications, including:
1. Product and service review analysis
2. Social media monitoring
3. Customer satisfaction assessment
4. Opinion detection in customer feedback

Spark NLP for Sentiment Analysis
<div style="text-align: justify;">Spark NLP is an open-source NLP library built on top of Apache Spark, developed by John Snow Labs. It enables large-scale natural language processing with high accuracy and scalability, making it suitable for production environments.</div> <br> Spark NLP offers pretrained sentiment analysis models and supports training custom models using deep learning techniques. Leveraging the power of Apache Spark, it allows distributed processing of large datasets, enabling efficient sentiment analysis at scale.
Key Features of Spark NLP for Sentiment Analysis:
Pretrained multilingual sentiment analysis models
1. Integration with Spark ML pipelines for modular workflows
2. Annotation framework including DocumentAssembler, Tokenizer, Embeddings, and SentimentDLModel
3. Capability to handle big data with distributed processing using Spark

## Example

__Pre-requisite__
1. Linux OS (Use wsl ubuntu if you using windows)
2. Hadoop cluster
3. Apache Spark
4. Python Library (pyspark 3.5.1 and spark-nlp 6.1.0)
5. Good internet connection (we need download pretrained model)

Take a look in my file [sentiment-analysis-test.py](https://github.com/MuhammadMukhlis220/Spark/blob/main/nlp-sentiment-analysis/sentiment-analysis-test.py), there are some string like "comment" in social media.

Run the file using spark submit: 
```
spark-submit --driver-memory 6G --executor-memory 6G --packages com.johnsnowlabs.nlp:spark-nlp_2.12:6.1.0 sentiment-analysis-test.py
```
I am using pretrained model, so it will automatically download the model in Amazon Web Service. Don't worry about the credential because we use the default credential from spark-nlp to download the model. We only need download once if we don't have the model. ALl model downloaded will store in our hdfs automatically. My directory is: `/user/mukhwsl/cache_pretrained`. Change mukhwsl by your user name.

Here the result:
<br>
![Alt Text](https://github.com/MuhammadMukhlis220/Spark/blob/main/nlp-sentiment-analysis/pic/result_1.png)

It will labelling the entity from inserted string. We can combined it as a big dataframe and send the results to data warehouse or etc for production purposes but remember with your platform resources.

__That all, give it a try!__

