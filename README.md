# 🚀 Uplimit DevOps Crash Course Project 2 - "Deploying Multiple Dependent Microservices at FaceTok"

![Demonstration of App](/assets/demo.gif)

## 🎯 Goal

In this project, the aim was to containerize 📦 two Flask apps: one for generating random quotes 📜 and another for displaying them 🖥️. The challenge was to orchestrate these services using Docker Compose, creating a basic yet functional website.

### <span style="color:orange"><strong>🌟 Milestones</strong></span>
1. <span style="color:orange"><strong>🐳 Containerization of Microservices</strong></span>: Mastered the art of containerizing Flask apps, showcasing Docker proficiency.
2. <span style="color:orange"><strong>🏗️ Docker Image Building</strong></span>: Excelled in Docker image creation, a crucial skill in containerization.
3. <span style="color:orange"><strong>🚢 Container Deployment</strong></span>: Deployed containers effectively, ensuring isolated environments for each service.
4. <span style="color:orange"><strong>🔗 Network Establishment</strong></span>: Established seamless Docker networks for inter-service communication.
5. <span style="color:orange"><strong>🧩 Docker Compose Orchestration</strong></span>: Demonstrated skill in orchestrating multi-container applications with Docker Compose.
6. <span style="color:orange"><strong>🛠️ Efficient Local Development</strong></span>: Developed a setup for efficient local development and testing of microservices.
7. <span style="color:orange"><strong>⚙️ Optional Advanced Features</strong></span>: Tackled advanced Docker features like service scaling and automated testing.

### <span style="color:violet"><strong>🚧 Challenges</strong></span>
1. <span style="color:violet"><strong>🔀 Microservices Segregation</strong></span>: Overcame the complexity of transitioning from a monolithic structure to microservices.
2. <span style="color:violet"><strong>🌐 Networking Between Services</strong></span>: Successfully managed networking challenges between containerized services.
3. <span style="color:violet"><strong>🎭 Orchestration Complexity</strong></span>: Skillfully managed the complexities of orchestrating multiple dependent containers.
4. <span style="color:violet"><strong>🪞 Consistency in Environments</strong></span>: Maintained environment consistency across development and production stages.
5. <span style="color:violet"><strong>🔧 Local Development Workflow</strong></span>: Improved the workflow for local development, a challenge with interdependent services.
6. <span style="color:violet"><strong>📈 Advanced Orchestration</strong></span>: Overcame advanced orchestration challenges like scaling and automation.

## Self Assessment

### 🐋 Tackling Docker and Microservices
To tackle the creation of the webservice, I first started with Docker and microservices. Building Dockerfiles and managing multi-container setups with docker-compose turned out to be a great way to understand the nuances of containerization. It wasn’t just about getting things running; it was about understanding why and how they worked.

### 🛠️ Starting Out with CI/CD and GitHub Actions
Next up was setting up GitHub Actions for CI/CD. This wasn't your typical follow-the-instructions exercise. Each step brought its own set of challenges and learnings. It was a process of trial and error, of figuring out how to make things work seamlessly in a real-world scenario.

### 🐍 Python Unit Tests and E2E Tests for Each Microservice
Testing with Python was more than just writing test scripts. I learned to effectively utilize pytest in various environments. It was a mix of getting the syntax right and understanding the best practices to ensure the tests did what they were supposed to do in the bigger picture of software delivery.

### 🧠 Embracing Problem-Solving
Every obstacle was an opportunity to learn something new. Whether it was a configuration issue or a bug, I took it as a challenge to expand my knowledge and skills. It was about perseverance and the satisfaction of solving problems.

### 🖥️ Automation with Bash Scripting
I found real-world applications for bash scripting in making CI pipelines more efficient. It was about automating the mundane to focus on the more complex and interesting aspects of development.

### 🔄 Adapting and Improving
For me, the key to success was adapting to new information and feedback. Continuously refining processes and setups made me appreciate the evolving nature of technology and the importance of staying up-to-date.

### ⚖️ Balancing Different Testing Approaches
I realized the importance of balancing different testing approaches. Sometimes, an end-to-end test was necessary; other times, a more focused test was more appropriate. It was about understanding the context and choosing the right approach.

### 🗣️ Clear Communication of Technical Details
One of my strongest beliefs is in clear communication. Explaining complex technical processes in an understandable way is crucial, not just for team collaboration but also for personal understanding and growth.

## 🤖 ChatGPT 3rd-Party Assessment: its opinion of our interaction

In our comprehensive interaction, you've demonstrated a range of key skills essential for effective software development and CI/CD pipeline management. Here's a summary of the skills and highlights from our interaction:

1. **🌐 Understanding and Implementing CI/CD Workflows**: You've adeptly navigated the complexities of setting up a CI/CD pipeline using GitHub Actions. This involved configuring workflows for automated testing and understanding nuances of YAML syntax.

2. **🐳 Docker and Microservices Management**: You demonstrated a solid understanding of Docker, including writing Dockerfiles and managing microservices. You skillfully used docker-compose to orchestrate multiple containers, showcasing your capability in handling containerized environments.

3. **🐍 Python Testing and Environment Management**: Your ability to set up Python environments, manage dependencies, and run tests using pytest was evident. You effectively installed Python packages on a GitHub Actions runner and executed non-containerized tests, reflecting a good grasp of Python's ecosystem.

4. **🔍 Debugging and Problem Solving**: Throughout our interaction, you showed strong problem-solving skills. You identified and resolved issues related to CI/CD setup, such as fixing a misnamed YAML file and dealing with a Docker image pull error.

5. **📜 Scripting and Automation**: Your use of bash scripting, particularly the understanding of exit ${PIPESTATUS[0]} to control CI pipeline behavior based on test outcomes, displayed your proficiency in automation and scripting within a CI context.

6. **🔄 Adapting to Feedback and Iterative Improvement**: You adeptly incorporated feedback and iteratively improved the CI/CD pipeline. Your willingness to explore different approaches (testing inside Docker containers vs. on the runner) highlights your adaptability and continuous improvement mindset.

7. **⚖️ Decision-Making in Testing Strategies**: You balanced between end-to-end testing and microservice-specific tests, showing an understanding of different testing methodologies and their relevance in CI/CD pipelines.

8. **🗣️ Technical Communication**: Throughout our interaction, you communicated technical concepts and issues clearly, a key skill in collaborative software development environments.

Combining these skills, you've demonstrated a comprehensive understanding of modern software development practices, especially in CI/CD, containerization, and automated testing. This reflects a well-rounded capability in DevOps and software engineering, crucial for efficient and effective software development cycles.

🔗 [Dive into the specifics of our conversation](https://spectacled-thumb-fdd.notion.site/Week-2-FaceTok-DevOps-Uplimit-26af6a0b92cd4f3a8c3f6f7b4b2f3709?pvs=4)
