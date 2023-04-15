FROM alpine:latest
RUN apk update && apk upgrade
RUN apk add --no-cache --update wget tar openjdk11 bash python3 snappy diffutils less
RUN mkdir Presto
ADD presto-server-0.280 /Presto
ADD presto /Presto
RUN mkdir /Presto/node_data
WORKDIR Presto/bin
RUN chmod +x launcher
CMD ./launcher run
