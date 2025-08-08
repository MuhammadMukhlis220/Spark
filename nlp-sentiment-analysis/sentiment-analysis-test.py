import sparknlp
from sparknlp.base import DocumentAssembler
from sparknlp.annotator import UniversalSentenceEncoder, SentimentDLModel
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession

spark = sparknlp.start()

# Document assembler
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

# Sentence embeddings
sentence_embeddings = UniversalSentenceEncoder.pretrained() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence_embeddings")

# Sentiment model
sentiment_dl = SentimentDLModel.pretrained("sentimentdl_use_twitter") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("sentiment")

# Pipeline
pipeline = Pipeline(stages=[
    document_assembler,
    sentence_embeddings,
    sentiment_dl
])

# Contoh data
data = spark.createDataFrame([
    ["OMG I love this!! 😍"],
    ["This sucks so bad 😡"],
    ["Can't wait 4 the weekend!! #excited"],
    ["Ugh, Monday again..."],
    ["Best movie ever!! LOL"],
    ["I hate when this happens 😭"],
    ["Yassss queen!!"],
    ["So tired rn, need coffee"],
    ["Meh, not feeling it today"],
    ["This food tho 🤤"]
], ["text"])


result = pipeline.fit(data).transform(data)
result.select("text", "sentiment.result").show(truncate=False)

