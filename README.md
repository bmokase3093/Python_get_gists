## :warning: Please read these instructions carefully and entirely first
* Clone this repository to your local machine.
* Use your IDE of choice to complete the assignment.
* When you have completed the assignment, you need to  push your code to this repository and [mark the assignment as completed by clicking here](https://app.snapcode.review/submission_links/78150c53-46c4-4ef8-8120-4399a76e5518).
* Once you mark it as completed, your access to this repository will be revoked. Please make sure that you have completed the assignment and pushed all code from your local machine to this repository before you click the link.

## Operability Take-Home Exercise

Welcome to the start of our recruitment process for Operability Engineers. It was great to speak to you regarding an opportunity to join the Equal Experts network!

Please write code to deliver a solution to the problems outlined below.

We appreciate that your time is valuable and do not expect this exercise to **take more than 90 minutes**. If you think this exercise will take longer than that, I **strongly** encourage you to please get in touch to ask any clarifying questions.

### Submission guidelines
**Do**
- Provide a README file in text or markdown format that documents a concise way to set up and run the provided solution.
- Take the time to read any applicable API or service docs, it may save you significant effort.
- Make your solution simple and clear. We aren't looking for overly complex ways to solve the problem since in our experience, simple and clear solutions to problems are generally the most maintainable and extensible solutions.

**Don't**

Expect the reviewer to dedicate a machine to review the test by:

- Installing software globally that may conflict with system software
- Requiring changes to system-wide configurations
- Providing overly complex solutions that need to spin up a ton of unneeded supporting dependencies. We aspire to keep our dev experiences as simple as possible (but no simpler)!
- Include identifying information in your submission. We are endeavouring to make our review process anonymous to reduce bias.

### Exercise
If you have any questions on the below exercise, please do get in touch and we’ll answer as soon as possible.

#### Build an API, test it, and package it into a container
- Build a simple HTTP web server API in any general-purpose programming language[^1] that interacts with the GitHub API and responds to requests on `/<USER>` with a list of the user’s publicly available Gists[^2].
- Create an automated test to validate that your web server API works. An example user to use as test data is `octocat`.
- Package the web server API into a docker container that listens for requests on port `8080`. You do not need to publish the resulting container image in any container registry, but we are expecting the Dockerfile in the submission.
- The solution may optionally provide other functionality (e.g. pagination, caching) but the above **must** be implemented.

Best of luck,  
Equal Experts
__________________________________________
[^1]: For example Go, Python or Ruby but not Bash or Powershell.  
[^2]: https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28


# How to Run GitHub Gists API Server
This Project Build a simple HTTP web server API that retrieves public gists for a specified GitHub user.

## Features
- **Fetch Public Gists**: Retrieve a list of public gists for any GitHub user.
- **Pagination Support**: Use query parameters to specify `page` and `per_page` for controlling the number of gists returned.
- **Caching**: Utilizes caching to minimize calls to the GitHub API and improve response times.

## Requirements
- **Docker**: Ensure Docker is installed on your machine. Follow the [Docker installation guide](https://docs.docker.com/get-docker/) for your specific operating system.

## Installation and running project. It include test file
1. **Clone the repository**: Open your terminal and run the following commands
    - git clone https://github.com/your-username/equal-experts-hospitable-sharp-elated-truth-f24f5424ee66.git
    - cd equal-experts-hospitable-sharp-elated-truth-f24f5424ee66

2. **Build the docker image**
    - docker build -t <image_name> .

3. **Run the docker container**
     - docker run -d -p 8080:8080 <image_name>

### Accessing the app
The API will be accessible at 
- http://localhost:8080/octocat

## With Pagenation
http://localhost:8080/octocat?page=1&per_page=5"
- page: The number of pagination
- per_page: Number of gists to return per page

## Result example
![alt text](image.png)

### Acknowledgements
- Flask - A micro web framework for Python.
- Requests - A simple and elegant HTTP library for Python.
- Flask-Caching - Provides caching capabilities for Flask applications.