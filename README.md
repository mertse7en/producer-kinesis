# Kinesis-Producer

### Sample data 

```

{
    "Data":{
        "name":"Kevin",
        "surname":"De Bruyne",
        "age":99
    },
    "PartitionKey":"1"
}

```

# Produce via API-GATEWAY

### You can easily define api gateway for your kinesis stream with [following link](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html) and send your data with POST request.
You will get endpoint like : https://****.***.com/****/****/**/**

### You must set your AWS credential before move on otherwise you'll get missing authentication err. Following example shows sample values, replace them with your own values.
```

$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json

```

### As you already have implemented gateway and set your credentials you can manually send your PUT requests.
