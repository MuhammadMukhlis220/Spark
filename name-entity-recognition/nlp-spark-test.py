from pyspark.sql import SparkSession
from sparknlp.base import *
from sparknlp.annotator import *
import sparknlp
from pyspark.sql.functions import explode, col

spark = SparkSession.builder \
    .appName("NER with GloVe and Spark NLP") \
    .config("spark.driver.memory", "6G") \
    .config("spark.executor.memory", "6G") \
    .config("spark.kryoserializer.buffer.max", "2000M") \
    .getOrCreate()

data = spark.createDataFrame([["Barack Obama was born in Hawaii. While Mukhlis was born in Jakarta, he had a lot fun in Indonesia. They had meeting in Bali after conference in China"]]).toDF("text")

document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

# GLOVE WITH ner_dl

embeddings = WordEmbeddingsModel.pretrained("glove_100d", "en") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")
'''
# BERT WITH ner_dl_bert

embeddings = BertEmbeddings.pretrained(name='bert_base_cased', lang='en') \
    .setInputCols(['document', 'token']) \
    .setOutputCol('embeddings')

'''
ner = NerDLModel.pretrained("ner_dl", "en") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")
'''
# For BERT

ner = NerDLModel.pretrained("ner_dl_bert", "en") \
    .setInputCols(["document", "token", "embeddings"]) \
    .setOutputCol("ner")
'''
ner_converter = NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter
])

model = pipeline.fit(data)
result = model.transform(data)

final_df = result.select(explode("ner_chunk").alias("chunk")).select(
    col("chunk.result").alias("text"),
    col("chunk.metadata")["entity"].alias("label")
)

final_df.show(truncate=False)

