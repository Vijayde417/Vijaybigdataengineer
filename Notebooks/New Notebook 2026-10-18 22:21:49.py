# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
Names = ["Vijay", "Durga", "Prasad", "Kadiyam"]
Capital_names = [name.upper() for name in Names]
print(Capital_names)