# This file is the Driver Program
# The Cluster Manager is not created in code, but could be configured with a SparkConf object
# The Executor are not in the code, but are running in the Worker Nodes when the Driver Program is executed

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Creation of Spark Session
spark = SparkSession.builder.appName("EcommerceDataAnalysis").getOrCreate()

# Read CSV file into a DataFrame
df = spark.read.csv("./ecommerce_sales_data.csv", header=True, inferSchema=True)

# Show DataFrame
df.show()

# Cast column units_sold to integer
df = df.withColumn("units_sold", col("units_sold").cast("int"))

# Analysis example: Calculate the total sales per category
total_sales_category = df.groupBy("category").agg(
    sum("units_sold").alias("total_sales")
)

total_sales_category.show()

# Stop Spark Session
spark.stop()
