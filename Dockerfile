# Base image
FROM apache/airflow:2.6.0

# Switch to root user to install system-level dependencies
USER root

# Install Java, procps, and other required utilities
RUN apt-get update && apt-get install -y \
    default-jdk \
    procps \
    && apt-get clean

# Set JAVA_HOME environment variable for all users
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Switch to the airflow user to install Python packages
USER airflow

# Install the Airflow Papermill provider
RUN pip install apache-airflow-providers-papermill

# Install PySpark for use in Airflow tasks
RUN pip install pyspark

# Switch back to root to ensure directory permissions are properly set
USER root
RUN echo "airflow ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Ensure airflow directory permissions
RUN chmod -R 777 /opt/airflow

# Switch back to the airflow user
USER airflow