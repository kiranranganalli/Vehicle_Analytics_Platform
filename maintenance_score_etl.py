import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType

def compute_score(temp, pressure, voltage):
    score = 100
    if temp > 110: score -= 20
    if pressure < 2.5: score -= 30
    if voltage < 11.5: score -= 25
    return max(score, 0)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.json("s3://your-bucket/telemetry/")
score_udf = udf(compute_score, IntegerType())
df = df.withColumn("maintenance_score", score_udf(col("engine_temp_c"), col("oil_pressure"), col("battery_voltage")))
df.write.format("parquet").save("s3://your-bucket/processed/")