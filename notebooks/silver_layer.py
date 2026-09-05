from pyspark.sql.functions import col, trim, regexp_replace

# -----------------------------
# Silver Marketplace
# -----------------------------
silver_marketplace = (
    spark.table("workspace.default.bronze_marketplace")
    .withColumn("product_name", trim(col("product_name")))
    .withColumn("brand", trim(col("brand")))
    .withColumn("processor", trim(col("processor")))
    .withColumn("ram", trim(col("ram")))
    .withColumn("storage", trim(col("storage")))
    .withColumn("screen_size", trim(col("screen_size")))
    .withColumn(
        "price",
        regexp_replace(col("price"), "[₹,]", "").cast("double")
    )
    .dropDuplicates(["product_url"])
)

silver_marketplace.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.silver_marketplace"
)


# -----------------------------
# Silver Products
# -----------------------------
silver_products = (
    spark.table("workspace.default.bronze_products")
    .withColumn("sku", trim(col("sku")))
    .withColumn("brand", trim(col("brand")))
    .withColumn("model", trim(col("model")))
    .withColumn("category", trim(col("category")))
    .withColumn("original_price", col("original_price").cast("double"))
    .dropDuplicates(["sku"])
)

silver_products.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.silver_products"
)


# -----------------------------
# Silver BOM
# -----------------------------
silver_bom = (
    spark.table("workspace.default.bronze_bom")
    .withColumn("sku", trim(col("sku")))
    .withColumn("component", trim(col("component")))
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("component_cost", col("component_cost").cast("double"))
    .dropDuplicates(["sku", "component"])
)

silver_bom.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.silver_bom"
)


# -----------------------------
# Silver Warranty
# -----------------------------
silver_warranty = (
    spark.table("workspace.default.bronze_warranty")
    .withColumn("sku", trim(col("sku")))
    .withColumn("component", trim(col("component")))
    .withColumn("failure_count", col("failure_count").cast("int"))
    .withColumn("warranty_claims", col("warranty_claims").cast("int"))
    .dropDuplicates(["sku", "component"])
)

silver_warranty.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.silver_warranty"
)

print("Silver layer tables created successfully.")
