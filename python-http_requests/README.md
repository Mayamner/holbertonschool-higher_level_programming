## This Project will be a brief summery about Restful and web as services requests

### The differences between HTTP and HTTPS: 

#### The only difference between the two protocols is that HTTPS uses TLS

#### HTTP: Stands for Hypertext transfer protocal whitch is the foundation of the World Wide Web and its used to load webpages using hypertext links 

#### HTTPS: Stands for Hypertext transfer protocal Secure whitch is the secure vertion of HTTP only 


#### HTTP Request has:

#### Method (e.g. GET, POST) — what action to take
#### Path (e.g. /index.html) — the resource being requested
#### Headers — metadata like Host, User-Agent, Accept, Content-Type
#### Body (optional) — data sent with the request, e.g. form data on a POST

### | Method | Description | Use case |
### |---|---|---|
### | GET | Retrieves data | Fetching a web page or data from an API |
### | POST | Sends new data to the server | Submitting a form, creating a new resource |
### | PUT | Updates/replaces an existing resource | Updating a user's full profile |
### | DELETE | Removes a resource | Deleting a post or account |

### | Code | Description | Scenario |
### |---|---|---|
### | 200 | OK | Request succeeded |
### | 201 | Created | A POST request successfully created a new resource |
### | 301 | Moved Permanently | Resource has a new permanent URL |
### | 404 | Not Found | Requested page isn't available on the server |
### | 500 | Internal Server Error | Something went wrong on the server's end |