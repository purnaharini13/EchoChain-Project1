from pyspark.sql.functions import current_timestamp

# Base path for uploaded EchoChain datasets
base_path = "/Volumes/workspace/default/echochain_data"

# Read raw marketplace data
marketplace_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/final_marketplace_dataset.csv")
    .withColumn("ingestion_timestamp", current_timestamp())
)

# Read internal product data
products_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/products.csv")
    .withColumn("ingestion_timestamp", current_timestamp())
)

# Read BOM data
bom_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/bom.csv")
    .withColumn("ingestion_timestamp", current_timestamp())
)

# Read warranty data
warranty_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{base_path}/warranty.csv")
    .withColumn("ingestion_timestamp", current_timestamp())
)

# Store raw datasets as Delta tables
marketplace_df.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.bronze_marketplace"
)

products_df.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.bronze_products"
)

bom_df.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.bronze_bom"
)

warranty_df.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.bronze_warranty"
)

print("Bronze layer tables created successfully.")
