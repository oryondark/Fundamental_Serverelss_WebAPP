# Fundamental Serverless Deep Learning Platform
##  Motivation
In this project, Server based Pattern Image Analysis using Deep learning System migrate to fully managed service of serverless platform.<br>

## Architecture
![Fundamental Serverelss Architecture](Figures/Fundamental_Serverless_Arch.png)

## Pre-required
It platform must use runtime of *python3.6+*.
Note that you should be understood the limit of FaaS like AWS Lambda, Google Function, Azure Function.<br>
Since the resources limit of AWS Lambda, we should be choose the low-version deep learning framework and candidate *Pytorch-1.0*.<br>
And then, we had been implemented of KNN mining system using *Scikit-Learn* that involved scipy.<br>
<br>
As well, You have to build RESTful Endpoint using *AWS API Gateway*, that need for CORS(cross origin resource sharing) policy because our system prefer to use web application leveraged *Ajax*.<br>
If you want to see the our web application, please check in followed link. <br>
[Our WebApp Link using Route53](http://crc.kmubigdata.cloud/)



*Summary:*<br>
Pytorch3.6+ <br>
AWS Lambda base <br>
AWS API gateway base <br>
AWS S3 to build your web app<br>
Ajax ( Asynchronous JavaScript and XML )

## To DevOps
[you can see the wiki here! <click>](https://github.com/oryondark/Fundamental_Serverelss_WebAPP/wiki)

## Platform Contributor
### Platform DevOps
**Hyunjune Kim.** - email is '4u_olion@naver.com'<br>
**Kyungyong Lee.** - my professor is him, an assistant professor in Kookmin University.<br>

### Modeling
Heetae Kim. - Deep Learning Algorithm Scientist.<br>
Dasom Lee. - CSS Design<br>
Soyong Lee. - CSS Design<br>

## Stopwatch
the StopWatch will make immediacy and readability for your code. <br>
create by Hyunjune KIM.

## Event
![Showcase](Figures/crc_showcase.jpg)
[![FashionSearch](Figures/embed_vedio.png)](https://www.youtube.com/watch?v=-YGAbbVvgZw)
