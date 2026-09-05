# -----------------------------
# Gold Product Reference
# -----------------------------
gold_product_reference = (
    spark.table("workspace.default.silver_products")
    .select(
        "sku",
        "brand",
        "model",
        "category",
        "original_price"
    )
)

gold_product_reference.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.gold_product_reference"
)


# -----------------------------
# Gold Marketplace Reference
# -----------------------------
gold_marketplace_reference = (
    spark.table("workspace.default.silver_marketplace")
    .select(
        "product_name",
        "brand",
        "processor",
        "ram",
        "storage",
        "screen_size",
        "price",
        "product_url",
        "source",
        "scraped_date"
    )
)

gold_marketplace_reference.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.gold_marketplace_reference"
)


# -----------------------------
# Gold Component Summary
# -----------------------------
gold_component_summary = (
    spark.table("workspace.default.silver_bom")
    .select(
        "sku",
        "component",
        "quantity",
        "component_cost"
    )
)

gold_component_summary.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.gold_component_summary"
)


# -----------------------------
# Gold Warranty Summary
# -----------------------------
gold_warranty_summary = (
    spark.table("workspace.default.silver_warranty")
    .select(
        "sku",
        "component",
        "failure_count",
        "warranty_claims"
    )
)

gold_warranty_summary.write.format("delta").mode("overwrite").saveAsTable(
    "workspace.default.gold_warranty_summary"
)

print("Gold layer tables created successfully.")
