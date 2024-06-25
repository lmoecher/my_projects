# The Web
This is the section designed to show how *CSS*, *HTML*, and *JavaScript* work together to create the sites we use everyday.

## Logan Moecher

## How it Works

### Web Page Building Blocks

##### CSS is for the styling of the web page

##### HTML is for the structuring of the web page

##### JavaScipt is for the funcitonality of the web page



### URL

* *URL* is short for Uniform Resource Location and is a way to locate a resource on the internet.

#### Example

* *URL*: (https://www.github.com/lmoecher/my_projects/blob/master/the_web/README.md) this is the URL that this  webpage uses. 

* These resources can be Web Pages(HTML documents), Images, Video files, Fonts, etc.


### Client Server Model

* The *Client*(*Browser*) and computers hosting the target website are the *Servers*.

* The *Client* requests a service and the *Server* provides the service. 

* These requests are formatted based on a protocol called *HTTP*.


### HTTP 

* *HTTP* is short for *Hypertext Transfer Protocol* and is a langauge that *clients* and *servers* use to talk to each other.

* NOT a Programming Language, it's just a plain textual langauge for communicating over the internet.

* *HTTPS* which is *HTTP* with encryption. This is so the messages between a *client* and a *server* are encrypted.

* When the *server* figures out what the *client* is asking, it will send a message back.

* The first message is an *HTTP Request* and the second message is an *HTTP Request*.

#### Example 1

* *HTTP Request* 

> GET /index.html HTTP/1.1  (This tends to represent the homepage of websites)
> Host: www.github.com  
> Accept-Language: en-us

* This message tells the browser what it is looking for.

#### Example 2 

* *HTTP Response*

> HTTP/1.1 200 OK   (Here is the version of *HTTP* protocol used, followed by a number which is the Status Code)
> Date: 25 Jun 2024 01:51   (This is the date and time of the response)
> Content-Type: text/html   (This shows what type of content the server is sending "text/html")

* Below the *HTTP Response* usually shows the html code that respresents the home page of whatever website is in use. In this case it would be the github.com homepage.

### DOM

* *DOM* or *Documented Object Model* for short, this a model that respresents objects or elements in an *HTML* document.

