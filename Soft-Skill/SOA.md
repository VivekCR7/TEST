# Service Oriented Architecture

<br>

# Table of Contents

 1. What is service oriented architecture? 
 2. Why there is need of SOA?  
 3. objectives of SOA? 
 4. Implementation of SOA? 
 5. Applications of SOA? 
 6. Advantages and Disadvantages of SOA? 
 7. References 

<br>
<br>

## 1. what is service oriented architecture?

* Service Oriented Architecture is an architecutral approach in which applications make use of services available in the network.
* It is as well applied in the field of software design where services are provided to the other components, through a communication protocol over a network.
* SOA allows users to combine a large number of facilities from existing services to form applications.
* Each service is an SOA embodies the code and data integration required to execute a complete, discrete business function (e.g., checking a customer's credit, calculating the monthly loan).
* **There are 2 major role within SOA:**
  * **Service provider:**
    * The service provider is the maintainer of the service and the organization that makes one or more services to use.
    * To advertise services, the provider can publish them in a registery, together with a service contract, that specifies how to use it, the requirements of the services, and the fees charged.
  * **Service Consumer:**
    * The service consumer can locate the service metadata in the registery and develop the required client components to bind and use the service.

<br>

<!-- ![IMAGE](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-245.png) -->

<p align = "center">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-245.png" width=500 height=200>
</p>

<br>

## Why there is need of SOA ?
<br>

* As the buisnesses grow more complex and the world needs for global systems to meet their goals increased SOA was introduced and was the go-to solution.
* when the monolith solutions started to hit there limit, to make the system organized with seperate modular pieces and abstract those functionalities and make them accessible at specific well-defined endpoints. that's the reason soa is used.
* Distributed systems, the main reason for SOA adoption, cause it allows the software components reusable via service interfaces. These interfaces utilize common communication standards in such a way that they can be rapidly incorporated into new applications without having to perform deep integration each time.
* Different owners, this is also main reason for soa adoption as, businesses and software systems grow and more teams take part in software development, SOA presents ideal solutions for such cases.
* Hetroginity, global and large complex systems tend to lack of harmony different platforms and technologies are used to solve different problems in the system, this introduces many challenges. SOA helps back through smooth integration of different parts into one single systems.
* with the use of SOA, it's possible to reduce costs while still "maintaining a desired level of output". It allows busisnesses to limit the amount of analysis required when developing custom solutions.
* The most important is scalability of a buisness to meet the expectations of clients. to do so SOA cuts back on the client-service interaction, which allows for greater scalability.
* Most important and fast development which is resuability of code, not only does this cut down the pace of the development but there is no reason to reinvent the coding wheel every time. SOA allows for using multiple coding languages because everything runs through a central interface. That makes the development very fast.

<br>

## Objectives of SOA ?
<br>

* The main objective is to structure procedures or software components as services. These services are designed to be loosely coupled to applications, so they are only used when needed.They are also designed to be easily used by software developers, who have to work on applications in a consistent way.
* The second objective is to provide a mechanism for publishing available services, which includes their functionality and I/O requirements.Services are published in a way that allows developers to easily incorporate them into applications.
* The last objective but not least of SOA is to control the use of these services to avoid security and governance problems.

<br>

<!-- ![IMAGE](https://miro.medium.com/max/1400/1*Xot9nbkQAGbGaYwi84Kh-w.png) -->

<p align = "center">
    <img src="https://miro.medium.com/max/1400/1*Xot9nbkQAGbGaYwi84Kh-w.png" width=400 height=350>
</p>

<br>

## Implementation
<br>

* When it comes to implementing service-oriented architecture (SOA), there is a wide range of technologies that can be used, depending on what your end goal is and what you’re trying to accomplish.
* Typically, Service-Oriented Architecture is implemented with web services, which makes the “functional building blocks accessible over standard internet protocol
* An example of a web service standard is SOAP, which stands for Simple Object Access Protocol. In a nutshell, SOAP “is a messaging protocol specification for exchanging structured information in the implementation of web services in computer networks. Although SOAP wasn’t well-received at first, since 2003 it has gained more popularity and is becoming more widely used and accepted. Other options for implementing Service-Oriented Architecture include Jini, COBRA, or REST.
* It’s important to note that architectures can “operate independently of specific technologies,” which means they can be implemented in a variety of ways, including messaging, such as ActiveMQ; Apache Thrift; and SORCER.

<br>


<!-- ![](https://miro.medium.com/max/1220/1*QpkU690MioKK7lHwLE0_Bg.png) -->

<p align = "center">
    <img src="https://miro.medium.com/max/1220/1*QpkU690MioKK7lHwLE0_Bg.png" width=500 height=350>
</p>

<br>

## Applications of SOA ?
<br>

* SOA infrastructure is used by many armies and air force to deploy situational awareness systems.
* SOA is used to improve healthcare delivery.
* SOA allows Mobile apps and games to use the mobile device's built-in functions, such as GPS.
* SOA helps maintain museums a virtualized storage pool for their information and content.
  
<br>

## Advantages and Disadvantages ?
<br>

**Advantages**

* **Service reusability:** In SOA, applications are made from existing services. Thus, services can be reused to make many applications.
* **Easy maintenance:** As services are independent of each other they can be updated and modified easily without affecting other services.
* **Platform independent:** SOA allows making a complex application by combining services picked from different sources, independent of the platform.
* **Availability:** SOA facilities are easily available to anyone on request.
* **Reliability:** SOA applications are more reliable because it is easy to debug small services rather than huge codes.
* **Scalability:** Services can run on different servers within an environment, this increases scalability.


**Disadvantages**

* **High overhead** A validation of input parameters of services is done whenever services interact this decreases performance as it increases load and response time.
* **High investment:** A huge initial investment is required for SOA.
* **Complex service management:** When services interact they exchange messages to tasks. the number of messages may go in millions. It becomes a cumbersome task to handle a large number of messages.

<br>

## References

* https://www.geeksforgeeks.org/service-oriented-architecture/
* https://medium.com/@SoftwareDevelopmentCommunity/what-is-service-oriented-architecture-fa894d11a7ec
* https://searchapparchitecture.techtarget.com/definition/service-oriented-architecture-SOA
* https://www.ibm.com/docs/en/rbd/9.5.1?topic=overview-service-oriented-architecture-soa
* https://www.ibm.com/in-en/cloud/learn/soa
* https://en.wikipedia.org/wiki/Service-oriented_architecture