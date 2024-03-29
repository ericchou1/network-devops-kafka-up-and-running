# Kafka Up and Running for Network DevOps
*Set Your Network Data in Motion* 

This is the respository companion to the book: 
**Kafka Up and Running for Network DevOps**

- [LeanPub](https://leanpub.com/network-devops-kafka-up-and-running)
- [Amazon Kindle](https://www.amazon.com/gp/product/B09LRC5YZT/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B09LRC5YZT&linkCode=as2&tag=pythfornetwen-20&linkId=9966132dc2cbcfb5d996ac1d1a0b519c)
- [Paperback](https://www.amazon.com/gp/product/1957046031/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1957046031&linkCode=as2&tag=pythfornetwen-20&linkId=a2cf2cd4972a57ccf220138838a8023b)

![Network DevOps Series: Kafka Up and Running Book Cover](/images/Kafka_Book_Cover.png)

## Introduction

Welcome to the world of data! Unless you lived under a rock for the last few years, you know data processing, machine learning, and artificial intelligence are taking over the world. We are now used to check traffic information from online cameras before we leave the house, use always-on thermometers to automatically adjust house temperatures, and leverage WiFi-enabled lights to match the lighting with our mood.

These cameras, lights, thermometers rely their own onboard sensors, small compute units, and embedded devices to gather and process data. By aggregating all of these disperse data across millions of devices, we are able to derive useful information that help us with our daily lives.

But have you ever wonder how are these data being exchanged between data producers and consumers? Do each of the devices provide an API (Application Programming Interface) to be queried? Do they have local databases that persist the data? What about data integrity, transmission latency, or scalabity?
There are many tools and projects that address these issues. One of the most popular and widely used tool by companies large and small alike, is Kafka1.

## Kafka Use Cases

There are many uses cases for Kafka in network engineers:

- We can use Kafka to stream data, such as logs and netflow data, once and be consumed by multiple receivers.
- We can separate data into logical petitions called Topics and allow an event-driven architecture, such as trigger events based on different type of events.
- We can build a centralized pipeline for network data processing instead of having disperse teams processing bits and pieces of data separately.

These are just some of the use cases of Kafka. By the end of this book, I am sure we will be able to find much more creative use cases.

