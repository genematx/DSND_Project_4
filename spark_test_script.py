from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
        Test script for submitting an application on AWS EMR.
    """

    spark = SparkSession\
        .builder\
        .appName('FirstTestApp')\
        .getOrCreate()

    user_log = [
        "User1",
        "User2",
        "User3",
        "User2",
        "User3",
        "User2",
        "User4",
        "User2",
        "User5",
        "User3"
    ]

    distributed_user_log = spark.sparkContext.parallelize(user_log)

    print(distributed_user_log.map(lambda x : x.lower()).collect())

    spark.stop()
