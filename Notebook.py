# Databricks notebook source
# MAGIC %sh ls -lsa /dbfs/user/hive/warehouse/

# COMMAND ----------

# MAGIC %sh cd /.fuse-mounts/wsfs/Repos/rlaplaud@vectice.com/databricks

# COMMAND ----------

# MAGIC %sh ls -lsa

# COMMAND ----------

# MAGIC %pip install GitPython

# COMMAND ----------

from git import Repo

# Provide the path to the cloned repository within DBFS
repo_path = '.'

# Open the repository
repo = Repo(repo_path)

