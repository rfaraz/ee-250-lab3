# ee-250-lab3

## Team Members
Rida Faraz <faraz@usc.edu>

Leyaa George <leyaageo@usc.edu>

## ***What is REST?***

### Question 1: Why are RESTful APIs scalable? 
RESTful APIs are scalable because the REST server does not store any data. In other words, the API is "stateless". The statelessness of this architecture removes all server load. This allows requests to be made to the server while minimizing communication between endpoints. This allows the service to be horizontally scalable. The URL component of RESTful APIs also allows for custom endpoint creation, making it easy to scale these APIs. With the base URL, an endless number of routes can be created to carry out different functionalities. 

### Question 2: According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients? 
A resource is any information that is given to a client by the application. In the context of our lab, all of the actual input is dependent on the user, but over time, this information is stored in the RESTful API server. The resources are then different attributes of a mail items that are sent to a client. This includes the entire inbox or collection of mail sent by a specific user, or more specific attributes such as sender, receiver, email subject, and body. 

### Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
One common REST method that our mail server does not implement is the PUT method. The PUT method is in charge of updating existing resources on the server. One way we can use PUT in our mail server is to create editability. This could mean allowing clients to edit a sent email, or more specifically, a client can edit the sender field if they update their username or account. This would reflect real mail app functionality. 

### Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question! 
The API keys are an essential part of RESTful APIs to provide security. If a company is deploying a RESTful API on their own server, an extremely high amount of incoming requests could be harmful and use up all resources on the server. In other cases, RESTful APIs might interface directly with private and sensitive data stored by a company, so allowing any user on the internet to either access or edit the data can have extremely harmful consequences. Requiring an API key allows for a level of authentication, meaning only the target clients can access certain functionalities. API keys, from a business perspective, can also help with managing subscriptions. An API key will track user activity like number of requests and can limit the amount of requests that a client is allowed to send. 

