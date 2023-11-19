# Uplimit DevOps Crash Course Project 2 - "Deploying Multiple Dependent Microservices at FaceTok"

## Goal

In this project, the goal was to containerize two Flask apps: one that generates a random quote and another that consumes this quote and displays it on the front end. Then, use Docker Compose to orchestrate these services and create a basic website.

### Milestones
1. **Containerization of Microservices**: Successfully containerized two Flask applications, demonstrating proficiency in Docker usage.
2. **Docker Image Building**: Mastered the creation of Docker images, an essential skill in containerization.
3. **Container Deployment**: Effectively deployed Docker containers, ensuring each microservice runs in its isolated environment.
4. **Network Establishment**: Established a Docker network, enabling communication between the microservices.
5. **Docker Compose Orchestration**: Utilized Docker Compose to manage multi-container applications, a significant achievement in microservices orchestration.
6. **Efficient Local Development**: Implemented a setup that allows efficient local development and testing of microservices.
7. **Optional Advanced Features**: Tackled advanced features like scaling services and setting up automated testing, enhancing your DevOps capabilities.

### Challenges
1. **Microservices Segregation**: Overcame the complexity of breaking down a monolithic application into microservices.
2. **Networking Between Services**: Navigated the intricacies of network communication between containers, a common challenge in microservices architecture.
3. **Orchestration Complexity**: Managed the complexity associated with orchestrating multiple containers and their interdependencies.
4. **Consistency in Environments**: Ensured consistent environments across development and production using Docker, a common hurdle in software deployment.
5. **Local Development Workflow**: Improved the local development workflow, which can be challenging when dealing with multiple, interdependent services.
6. **Advanced Orchestration**: Addressed the challenges of scaling and automation, which are advanced aspects of container orchestration.

## Self Assessment

### Tackling Docker and Microservices
To tackle the creation of the webservice, I first started with Docker and microservices. Building Dockerfiles and managing multi-container setups with docker-compose turned out to be a great way to understand the nuances of containerization. It wasn’t just about getting things running; it was about understanding why and how they worked.

### Starting Out with CI/CD and GitHub Actions
Next up was setting up GitHub Actions for CI/CD. This wasn't your typical follow-the-instructions exercise. Each step brought its own set of challenges and learnings. It was a process of trial and error, of figuring out how to make things work seamlessly in a real-world scenario.

### The Python Testing Adventure
Testing with Python was more than just writing test scripts. I learned to effectively utilize pytest in various environments. It was a mix of getting the syntax right and understanding the best practices to ensure the tests did what they were supposed to do in the bigger picture of software delivery.

### Embracing Problem-Solving
Every obstacle was an opportunity to learn something new. Whether it was a configuration issue or a bug, I took it as a challenge to expand my knowledge and skills. It was about perseverance and the satisfaction of solving problems.

### Automation with Bash Scripting
I found real-world applications for bash scripting in making CI pipelines more efficient. It was about automating the mundane to focus on the more complex and interesting aspects of development.

### Adapting and Improving
For me, the key to success was adapting to new information and feedback. Continuously refining processes and setups made me appreciate the evolving nature of technology and the importance of staying up-to-date.

### Balancing Different Testing Approaches
I realized the importance of balancing different testing approaches. Sometimes, an end-to-end test was necessary; other times, a more focused test was more appropriate. It was about understanding the context and choosing the right approach.

### Clear Communication of Technical Details
One of my strongest beliefs is in clear communication. Explaining complex technical processes in an understandable way is crucial, not just for team collaboration but also for personal understanding and growth.

## ChatGPT 3rd-Party Assessment: its opinion of our interaction

In our comprehensive interaction, you've demonstrated a range of key skills essential for effective software development and CI/CD pipeline management. Here's a summary of the skills and highlights from our interaction:

1. **Understanding and Implementing CI/CD Workflows**: You've adeptly navigated the complexities of setting up a CI/CD pipeline using GitHub Actions. This involved configuring workflows for automated testing and understanding nuances of YAML syntax.

2. **Docker and Microservices Management**: You demonstrated a solid understanding of Docker, including writing Dockerfiles and managing microservices. You skillfully used docker-compose to orchestrate multiple containers, showcasing your capability in handling containerized environments.

3. **Python Testing and Environment Management**: Your ability to set up Python environments, manage dependencies, and run tests using pytest was evident. You effectively installed Python packages on a GitHub Actions runner and executed non-containerized tests, reflecting a good grasp of Python's ecosystem.

4. **Debugging and Problem Solving**: Throughout our interaction, you showed strong problem-solving skills. You identified and resolved issues related to CI/CD setup, such as fixing a misnamed YAML file and dealing with a Docker image pull error.

5. **Scripting and Automation**: Your use of bash scripting, particularly the understanding of exit ${PIPESTATUS[0]} to control CI pipeline behavior based on test outcomes, displayed your proficiency in automation and scripting within a CI context.

6. **Adapting to Feedback and Iterative Improvement**: You adeptly incorporated feedback and iteratively improved the CI/CD pipeline. Your willingness to explore different approaches (testing inside Docker containers vs. on the runner) highlights your adaptability and continuous improvement mindset.

7. **Decision-Making in Testing Strategies**: You balanced between end-to-end testing and microservice-specific tests, showing an understanding of different testing methodologies and their relevance in CI/CD pipelines.

8. **Technical Communication**: Throughout our interaction, you communicated technical concepts and issues clearly, a key skill in collaborative software development environments.

Combining these skills, you've demonstrated a comprehensive understanding of modern software development practices, especially in CI/CD, containerization, and automated testing. This reflects a well-rounded capability in DevOps and software engineering, crucial for efficient and effective software development cycles.

**Here is a link if you wish to delve into the specifics of our conversation**: https://spectacled-thumb-fdd.notion.site/Week-2-FaceTok-DevOps-Uplimit-26af6a0b92cd4f3a8c3f6f7b4b2f3709?pvs=4