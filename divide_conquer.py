# brak java rodzi problemy...

import findspark
from pyspark.sql import SparkSession

findspark.init()
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext

words_list = ['python', 'java', 'ottawa', 'ottawa', 'java', 'news']
wordsRDD = sc.parallelize(words_list, 4)
print(wordsRDD.collect())

word_pairs = wordsRDD.map(lambda w: (w, 1))
print(word_pairs.collect())

word_counts_collected = word_pairs.reduceByKey(lambda x, y: x+y)
print(word_counts_collected.collect())
