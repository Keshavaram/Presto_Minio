FROM alpine:latest
RUN apk update && apk upgrade
RUN apk add --no-cache wget tar openjdk8 bash
RUN wget "https://archive.apache.org/dist/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz"
RUN tar -zxf hadoop-3.3.3.tar.gz
RUN wget "https://downloads.apache.org/hive/hive-3.1.2/apache-hive-3.1.2-bin.tar.gz"
RUN tar -zxf apache-hive-3.1.2-bin.tar.gz
RUN rm hadoop-3.3.3.tar.gz
RUN rm apache-hive-3.1.2-bin.tar.gz

ENV HADOOP_HOME=/hadoop-3.3.3
ENV HIVE_HOME=/apache-hive-3.1.2-bin
ENV PATH=$PATH:$HIVE_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HADOOP_INSTALL=$HADOOP_HOME
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_HDFS_HOME=$HADOOP_HOME
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk
ENV HADOOP_OPTS=-Djava.library.path=$HADOOP_HOME/lib/native

RUN export HADOOP_HOME=/home/$USER/hadoop-3.3.3
RUN export HADOOP_INSTALL=$HADOOP_HOME
RUN export HADOOP_MAPRED_HOME=$HADOOP_HOME
RUN export HADOOP_COMMON_HOME=$HADOOP_HOME
RUN export HADOOP_HDFS_HOME=$HADOOP_HOME
RUN export YARN_HOME=$HADOOP_HOME
RUN export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
RUN export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
RUN export HADOOP_OPTS=-Djava.library.path=$HADOOP_HOME/lib/native
RUN export HIVE_HOME=/home/keshavaram/hive/apache-hive-3.1.2-bin
RUN export PATH=$PATH:$HIVE_HOME/bin

RUN wget "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1026/aws-java-sdk-bundle-1.11.1026.jar"
RUN wget "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.3/hadoop-aws-3.3.3.jar"
RUN mv aws-java-sdk-bundle-1.11.1026.jar $HIVE_HOME/lib
RUN mv hadoop-aws-3.3.3.jar $HIVE_HOME/lib

RUN apk add --no-cache openssh-server openssh-client
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN chmod 777 ~/.ssh/authorized_keys

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk" >> $HADOOP_HOME/etc/hadoop/hadoop-env.s

RUN mkdir dfsdata
RUN mkdir /dfsdata/datanode /dfsdata/namenode
RUN chown root /dfsdata/namenode /dfsdata/datanode
RUN chmod 777 /dfsdata/namenode /dfsdata/datanode
RUN cd

RUN truncate -s 0 $HADOOP_HOME/etc/hadoop/core-site.xml
RUN echo '<?xml version="1.0" encoding="UTF-8"?> <?xml-stylesheet type="text/xsl" href="configuration.xsl"?> <configuration> <property> <name>hadoop.tmp.dir</name> <value>/tmpdata</value> </property> <property> <name>fs.default.name</name> <value>hdfs://127.0.0.1:9000</value> </property> <property> <name>hadoop.proxyuser.root.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.root.hosts</name> <value>*</value> </property> <property> <name>hive.server2.enable.doAs</name> <value>false</value> </property> <!-- OOZIE proxy user setting --> <property> <name>hadoop.proxyuser.oozie.hosts</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.oozie.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.httpfs.hosts</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.httpfs.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.llama.hosts</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.llama.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.hue.hosts</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.hue.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.mapred.hosts</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.mapred.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.hive.hosts</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.hive.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.hdfs.groups</name> <value>*</value> </property> <property> <name>hadoop.proxyuser.hdfs.hosts</name> <value>*</value> </property> <property> <name>fs.s3a.connection.ssl.enabled</name> <value>true</value> </property> <property> <name>fs.s3a.endpoint</name> <value>http://192.168.49.2:30659</value> </property> <property> <name>fs.s3a.access.key</name> <value>iBv8O3vKoTlwF8eX</value> </property> <property> <name>fs.s3a.secret.key</name> <value>uTJFwDjVcam2Ot8HaQVtZd7v0hINYvIV</value> </property> <property> <name>fs.s3a.path.style.access</name> <value>true</value> </property> <property> <name>fs.s3a.impl</name> <value>org.apache.hadoop.fs.s3a.S3AFileSystem</value> </property> <property> <name>metastore.storage.schema.reader.impl</name> <value>org.apache.hadoop.hive.metastore.SerDeStorageSchemaReader</value> </property> </configuration>' >> $HADOOP_HOME/etc/hadoop/core-site.xml

RUN truncate -s 0 $HADOOP_HOME/etc/hadoop/hdfs-site.xml
RUN echo '<?xml version="1.0" encoding="UTF-8"?> <?xml-stylesheet type="text/xsl" href="configuration.xsl"?> <configuration> <property> <name>dfs.name.dir</name> <value>/dfsdata/namenode</value> </property> <property> <name>dfs.data.dir</name> <value>/dfsdata/datanode</value> </property> <property> <name>dfs.replication</name> <value>1</value> </property> </configuration>' >> $HADOOP_HOME/etc/hadoop/hdfs-site.xml

RUN truncate -s 0 $HADOOP_HOME/etc/hadoop/mapred-site.xml
RUN echo '<?xml version="1.0"?> <?xml-stylesheet type="text/xsl" href="configuration.xsl"?> <configuration> <property> <name>mapreduce.framework.name</name> <value>yarn</value> </property> </configuration>' >> $HADOOP_HOME/etc/hadoop/mapred-site.xml

RUN truncate -s 0 $HADOOP_HOME/etc/hadoop/yarn-site.xml
RUN echo '<?xml version="1.0"?> <configuration> <property> <name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle</value> </property> <property> <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name> <value>org.apache.hadoop.mapred.ShuffleHandler</value> </property> <property> <name>yarn.resourcemanager.hostname</name> <value>127.0.0.1</value> </property> <property> <name>yarn.acl.enable</name> <value>0</value> </property> <property> <name>yarn.nodemanager.env-whitelist</name> <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PERPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value> </property> </configuration>' >> $HADOOP_HOME/etc/hadoop/yarn-site.xml

ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

RUN export HDFS_NAMENODE_USER=root
RUN export HDFS_DATANODE_USER=root
RUN export HDFS_SECONDARYNAMENODE_USER=root
RUN export YARN_RESOURCEMANAGER_USER=root
RUN export YARN_NODEMANAGER_USER=root

RUN hdfs namenode -format
RUN export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
RUN echo "export HADOOP_HOME=/hadoop-3.3.3" >> $HIVE_HOME/bin/hive-config.sh
CMD schematool -dbType derby -initSchema --verbose;hive	--service metastore --verbose
