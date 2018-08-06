## Chapter 8 setup instructions

This is the only chapter with custom installation requirements. Here are some step-by-step instructions on how to install and configure everything.

### MongoDB 
You can instal mongodb with homebrew:
```
brew install mongodb
mkdir -p /data/db
sudo chmod 777 /data/db
```
All you need to run a local server is to type in this into the CLI:
```
mongod
```

### Kafka
You can install kafka with homebrew:
```
brew install kafka
```
To run a kafka server all you need to do is:
```
# run zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# run kafka 
bin/kafka-server-start.sh config/server.properties 
```

### Kubernetes
To install kubernetes, use homebrew:
```
brew install kubernetes-cli
```
To run kubernetes:
```
kubectl run [imagename]
```

### Robo 3T 
You can install Robo 3T directly from website: https://robomongo.org/download

### Docker  
You can install Docker directly from website: https://docs.docker.com/docker-for-mac/install/

### Google cloud SDK
You can install the Google Cloud SDK download and follow instructions on website: https://cloud.google.com/sdk/docs/quickstart-macos
