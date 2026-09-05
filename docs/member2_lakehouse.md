# EchoChain – Member 2: Data Lakehouse

## Role

Member 2 – Data Lakehouse using Databricks and Delta Lake.

## Objective

Build the data lakehouse pipeline for the EchoChain project and prepare
reference-ready datasets for downstream PySpark processing and Power BI analytics.

## Lakehouse Architecture

Scrapy
↓
Databricks / Delta Lake
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer
↓
PySpark Processing
↓
Power BI

## Lakehouse Layers

### Bronze Layer

Stores raw ingested datasets from the marketplace and internal reference data.

Tables:

- bronze_marketplace
- bronze_products
- bronze_bom
- bronze_warranty

### Silver Layer

Contains cleaned and standardized data.

Operations include:

- Removing duplicate records
- Trimming text fields
- Converting price values to numeric format
- Standardizing numeric columns
- Maintaining ingestion timestamps

Tables:

- silver_marketplace
- silver_products
- silver_bom
- silver_warranty

### Gold Layer

Contains reference-ready datasets for downstream processing and analytics.

Tables:

- gold_product_reference
- gold_marketplace_reference
- gold_component_summary
- gold_warranty_summary

## Responsibility Boundary

Member 2 is responsible for the Databricks and Delta Lake lakehouse pipeline.

Marketplace-to-internal-SKU fuzzy matching is handled by Member 3.

Circularity Score, depreciation analysis and Power BI visualization are handled by Member 4.
