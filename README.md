# README
---
# Character Archetype Generation Microservices

Written in reference to QAC - Practical Project Specification (DevOps). This project is for the purpose of fulfilling the specification definition for the project assignment due Week 8 of the DevOps February 17 2020 intake cohort. The official working title of the project is SFIA Project 2 (independent), often reformatted to sfia_project_2 for tagging usage.

## Table of Contents

1. [Project Brief](#project-brief)
    + [Proposal](#proposal)
2. [Trello Board](#trello-board)
    + [MoSCoW Analysis](#moscow-analysis)
    + [Start Point](#start-board)
    + [Rolling Changes](#rolling-changes)
    + [End Point](#end-point)
3. [Risk Assessment](#risk-assessment)
4. [Project Architecture](#project-architecture)
    + [Entity Relationship Diagram](#entity-relationship-diagram)
    + [Architecture Diagram](#architecture-diagram)
    + [Issues Encountered](#issues-encountered)
5. [Design Considerations](#design-considerations)
    + [Front End](#front-end)
    + [Back End](#back-end)
    + [UI](#ui)
6. [Testing](#testing)
    + [Pytest Testing](#pytest)
    + [Selenium Testing](#selenium)
    + [Final Report](#final-report)
7. [Deployment](#deployment)
    + [Toolset](#toolset)
    + [CI Server Implementation](#ci-server-implementation)
    + [Branch and Merge Log](#branch-and-merge-log)
8. [Front End Considerations](#front-end-considerations)
9. [Improvements for Future Versions](#improvements-for-future-versions)
10. [Installation and Setup Guide](#installation-and-setup-guide)
+ [Authors](#authors)
+ [Acknowledgements](#acknowledgements)

## Project Brief

The project requires a set of four microservices of RESTful architecture, utilising dual implementations, capable of persisting data to a database. The services must be containerised using Docker. The project must be deployed via a CI/CD server, Jenkins, tested thoroughly, then deployed to a production environment that has been configured using Ansible.

### Proposal

My proposal focuses on the creation of a website for the generation of game character archetypes, predominantly in a fantasy setting. The services will be split as follows:

+ Service 1: the frontend of the website. Responsible for the display and persistence of the generated data. A lightweight flask app with a single page minimal HTML template. Communicates with the other services. Has a form input to enable the dual implementation of the other generators.

+ Service 2: generates a "skill" for the character, based on the inputs of service 1.

+ Service 3: generates a "modifier" for the skill, based on the inputs of service 1.

+ Service 4: generates a title at random for the character, based on the inputs of service 1. Receives and formats all of the generated data from the other 3 services, returning it to service 1 for display.

![A blockframe mockup of how I envisioned the service 1 display to look, as a wireframe](https://i.imgur.com/2im679x.png)

This shows a blockframe style mockup of how I envisioned the user-facing aspect of the project to appear at the start of the project.

## Trello Board

I used a kanban board on Trello to manage my workflow during the project, the board was set to public to enable overview and broadcast. Agile methodology was implemented in line with the brief, in terms of product and task backlog, although due to the individual nature of the project, no scrum working practices were implemented. Due to the short nature of the project, the entire workflow was considered to constitute a single sprint.

Running parallel to the board's progressing, a MoSCoW prioritisation analysis was started, as demonstrated below.

As the project progressed, items of work passed through the progress and testing columns for final assignment in either 'done' or 'issues'. Those items which reached issues could be reassessed at morning standups, in order for their importance to be reevaluated. Those which were of high importance, with reference to the MoSCoW analysis, could be reintroduced into the workflow. Those of low importance could be left in 'issues' for inclusion in future versions of the project.

### MoSCoW Analysis

#### Must Have

+ Microservice oriented architecture comprising at least 4 services.
    + Service 1 handles Jinja2 templates, communicates with other services, and persists data.
    + Services 2 and 3 randomly generate an object.
    + Service 4 generates an object based on the results of 2 and 3.
    + Services 2, 3, and 4 must be capable of dual implementations, switching without interrupting user experience.
+ A KanBan board with full expansion on tasks needed to complete the project.
+ An Applicationfully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
+ The project must be deployed using containerisation and an orchestration tool.
+ An Ansible Playbook that will provision the environment that your application needs to run.

#### Should Have

+ Web hooks should be used so that Jenkins recreatesand redeploys the changed application.
+ The project passes through a testing environment.
+ The project is deployed to a _separate_ deployment environment.
+ Docker swarm is used over compose to enable deployment to multiple nodes.
+ Product is robust, and documentation covers enough information for project to be portable.
+ Documentation includes clear design process for both planning and design.
+ Documentation includes progression throughout the project.

#### Could Have

+ Full CRUD functionality is included in service 1.
+ Front end testing is included in the testing phase.
+ Deployment to multiple VMs, reflected in both Jenkins configuration, and playbook complexity.
+ Security measures taken for project, sensitive data not version controlled, firewalls configured appropriately.
+ Installation and handling instructions included in documentation.
+ Documentation and charts included to outline future project improvements.

### Start Point

![A picture of the trello board, started on the first week. Only the product backlog has been added. No tasks have been entered.](https://i.imgur.com/CvLeQD2.png)

At the start of the project, I focussed on tasks that would not interfere with training, and the construction of the services: Starting the Kanban board [itself](https://trello.com/b/xlkzbGt0/qasfiaproject2), starting this documentation to streamline my future workflow, instituting a github repository for the project, which can be found [here](https://github.com/THC-QA/sfia_project_2), and initialising the risk assessment for the project in line with my initial understanding.

### Rolling Changes

+ 4 services were constructed, using Flask, and their interaction tested at a local level.
+ Dual implementations were added to the services where needed, and the shifting tested to be seamless.
+ A MySQL database was created, and connections added to allow for data persistency. The firewall rules were ammended to allow for this.
+ Basic URL and database tests were instituted to check for the presence of the project, and data architecture of the persistence.
+ Dockerfiles were created for the services, enabling containerisation. The services were appropriately tagged, and pushed to dockerhub.
+ A docker-compose file was created, with appropriate networking rules to allow for the deployment of the project using single commands. This was tested with docker-compose, before being further ammended to allow for docker swarm functionality.
+ Jenkins was set up on a separate VM, to handle the integration and deployment of the project.
+ A jenkinsfile was created to allow for pipeline functionality, to start with a local deployment to the jenkins server. To facilitate the testing of the project, a separate compose file was created to input different environment variables for the testing database.
+ To allow jenkins deployment environment files were moved to the jenkins server, without being uploaded, to keep the security of the files paramount.
+ Docker swarm was troubleshooted to enable deployment to other VMs.
+ SSH implementation was started for jenkins, to enable it to connect with the eventual deployment nodes. To allow this, the pipeline was re-architected to distribute jobs to different nodes. The firewall rules for all 3 VMs were updated to allow for swarm functionality, and to allow communication between the servers.
+ An ansible playbook, complete with roles was created, to configure the servers. It was tested locally before being added to the jenkins pipeline.
+ Once the playbook had been troubleshooted, and the node deployment on swarm configured, the MVP of the project had been completed, along with some of the 'should have' requirements.
+ To round off the markscheme, the documentation was started early; full CRUD functionality was added to service 1, tested, and deployed; and selenium testing was started, requiring a new round of configuration requirements for the jenkins server.

### End Point

![A picture of the endpoint of the Trello KanBan board, shortly before the presentation](https://i.imgur.com/pC5hnQx.png)

By the completion date of the project, the remaining task was once again related to the implementation of Selenium. Despite the linking to a headless version of Chrome, and correct implementation of chromedriver functionalities, neither the find_element_by_id() or find_element_by_name() methods would work. X-path sourcing was chosen instead, but this is a sub-standard testing protocol, as any redesign of the web templates would break the testing procedures.

#### What Went Well

+ Project completed on time, to well above spec.
+ Deployment to multiple non-local VMs achieved.
+ Full CRUD functionality included in app.
+ Learning exceeded project bounds.

#### What Could Be Improved

+ POST methods were learnt, but implementation was found not to fit the requirements. More could be done to learn the appropriate use cases for HTML methods.
+ Sessions and Cookies were explored as options for passing information between services, but could not be correctly implemented. As these are common tools in the webdev set, more could be done to learn their usage.
+ The issues encountered installing and using Selenium demonstrated that far more can be learnt about both web and browser architecture, but also about the structural usage of operating systems, particularly Linux.

## Risk Assessment


|Risk No.|Risk|Description|Hazard|Likelihood|Impact|Solution|
|---|---|---|---|---|---|---|
|1.0.1|Overrun on time.|Due to poor time management, the project is not completed.|Worst case scenario, marks are lost due to lack of coverage of brief.|2|5|Make good use of Kanban to manage workflow, and efficient time use of office resources.|
|1.0.2|Data breach on workstation.|Due to accident or malicious action, workstation is compromised.|Worst case scenario, severe progress loss.|1|5|Change passwords on workstation, keep e-services logged off when not in use.|
|1.0.3|Catch coronavirus.|Due to illness, significant amounts of work or learning time are lost.|Worst case scenario, the project cannot be completed.|4|5|Avoid human contact, follow NHS best practice.|
|1.0.4|Exposure of secrets.|Environment variables, SSH keys, or configuration files are uploaded.|Worst case scenario, all data is accessible to malicious actors.|3|4|Protect personal data, make use of ignore files and obfuscation.|
|1.1.1|Overrunning on GCP free data limits.|An instance is left running, or an account breach enables the resources on the account to be drained.|Worst case scenario, databases are unaccessable.|1|3|Continue monitoring GCP usage. Copy databases offline as final backup.|
|1.1.2.1|Database security: SQL|The GCP server is breached in some way, compromising data integrity.|Worst case scenario, data is lost|2|2|Keep firewall rules updated, regularly monitor instances for signs of breach.|
|1.1.2.2|Database security: SSH|Unmanaged connections cause data leak or damage, keys are lost or stolen.| Worst case scenario, GDPR noncompliance or total data compromisation.|2|4|Minimise the number of keys in play, and carefully safeguard them.|
|1.2.1|Flask sql iteration.|Flask's handling of mySQL commands requires reliable data structure.|Worst case scenario, repeated mySQL errors thrown due to column incompatability.|3|3|Ensure data handling by ID rather than content, by better use of Jinja2.|
|1.3.1|Jenkins pipeline integration|Jenkins compatability with GitHub webhooks.|Worst case scenario builds are not triggered, resulting in inconsistent builds.|3|1|Maintain webhooks and pull/push requests, ensure branches merged correctly.|
|1.3.2|Jenkins server exposed.|Port 8080 open to webtraffic is poor working practice.|Worst case scenario, introduce systemic vulnerabilities into build server.|5|2|Set firewall rules to only allow specific access.|
|1.4.1|Ansible can't gain access to nodes.|Jenkins configuration tool cannot gain access to nodes.|The pipeline stops working as swarm initialisation is incomplete.|2|5|Manage nodes and SSH keys carefully using configuration files.|

![A risk assessment matrix for the beginning of the project](https://i.imgur.com/Y7Lg0G3.png)

As the matrix demonstrates, at the beginning of the project, the majority of presumed risks were in the yellow band. This represents a medium level of combined risk, that requires ongoing management, and measures put in place to mitigate the effects. The one risk that represented a high level of combined risk to the project was the ongoing global pandemic, an assessment that would prove to be unfortunately prophetic, as I fell ill during the second week.

After implementation of the proposed solutions from the first table, the results of the project are expanded upon below.

|Risk No.|Risk Occured|Effects|Incidences (days across 3 week span)|Impact|Proposed Revision|
|---|---|---|---|---|---|
|2.0.1|Coronavirus was caught.|Reduced working efficiency for a week, extremely fortunate due to relatively mild symptoms.|7|3|Largely unavoidable, invest in PPE?|
|2.0.2|Back pain due to working conditions.|Regular breaks for exercise.|14|2|Unforeseen due to change in quarantine rules, set up a better office space.|
|2.0.3|GCP impact due to pandemic.|Installation phase had to be commented out of pipeline and manually implemented.|5|5|Unforeseen due to impact of global pandemic, if budget available, switch to paid tier access.|
|2.1.0|HTML method issues.|Spent an extra 2 days learning first POST, then cookies.|2|4|Do further research into HTML arguments vs alternative implementations to ascertain market standard.|
|2.2.0|Selenium issues.|Installation, set up, and finding was all a complete mess.|1|4|Find someone with selenium experience to explain correct usage, as online tutorials not helpful.|

There are three potential takeaways from the discrepancies between the first and second risk assessments:

1. The lack of reoccurance of risks, with the exception of coronavirus, implies that the preventative solutions implemented were effective in avoiding the risks in question.
2. The appearance of new risks suggests that the initial assessment was not sufficiently wide, nor forward thinking in its scope, and better foresight could be implemented in future projects.
3. The largely unforeseeable nature of the encountered risks demonstrates the old adage:

> _"No plan survives first contact with the enemy."

To further illustrate the renewed risk assessment, a modified risk matrix is displayed below.

![A risk assessment matrix for the completion of the project.](https://i.imgur.com/KNw8rFl.png)

From this it can be seen that the majority of the risks encountered fell into the 'moderate' band, being manageable with maintenance and added measures. 

## Project Architecture

### Entity Relationships

![The entity relationship diagram for the project, as envisaged for the MVP requirements](https://i.imgur.com/PYEeK2w.png)

The data persistence required for the project was extremely simplistic. In this instance the textual representation of the JSON object generated by the microservices is passed to the MySQL database directly.

To demonstrate how an expanded version of the project might look, I have included a further ERD, demonstrating improvements that could be made.

![The entity relationship diagram for an expanded view of the project, as envisaged for a future iteration.](https://i.imgur.com/GBBl5cn.png)

The roll-out for this extended view of the project could be broken into three stages, as demonstrated by the colour coding of the diagram.

#### Green Expansion

+ Trivial effort.
+ Data split into JSON headings, stored in expanded character table.
+ Can be called with greater specificity, and edits made to the table without effecting data structure.

#### Yellow Expansion

+ Non-trivial effort.
+ A user login feature is implemented, making correct use of sessions and cookies.
+ User data is correctly protected and stored in a basic user table.
+ A many to many relationship is implemented, allowing users to persist characters linked to their accounts.

#### Red Expansion

+ Extensive effort.
+ An admin system is instituted to allow non-architect management of the project.
+ Admin data is stored, protected, in an admin table.
+ Admin permissions are assigned and monitored.
+ SQL access privileges are assigned over the other tables.
+ Backend access is granted, and correctly assigned, to allow admins to monitor and maintain the project.

### Overall Architecture

#### Interaction and Services

This section aims to demonstrate how user interaction with the app is structured, as well as the interplay between the services that make up the swarm.

![User interaction diagram showing swarm architecture.](https://i.imgur.com/eNKu4SI.png)

As can be seen from the diagram, from a user perspective, they are only faced with the output of the frontend container, as balanced by the swarm manager. There are five containers in total (including NGINX), and each of the containers runs on 3 replicas. Odd numbers of replicas are preferred in order to achieve quorum during polling.

Replicas have been set at 3 due to hardware constraints on the available VMs.

Not shown on the diagram is the connection between the frontend container and the database, as it is opaque to the user. An explanation of its functionality is included in the back end design considerations.

#### Deployment

The deployment of the project ties together the toolsets which were covered in training, focusing on the portability of the application, and its ability to space optimise for cloud run environments. To show a typical look at the deployment pipeline, two diagrams are included below.

![Deployment CI/CD Diagram, showing typical process flow.](https://i.imgur.com/bTKOcs1.png)

In complement to the pipeline diagram, the three build environments are split within the database as well. Operations that take place on the testing stack are sent to a 'testing' database, which is wiped before and after every process. By contrast operations that take place on the production environment of the manager/worker nodes are sent to a project database that persists the data from the website.

Due to the inclusion of full CRUD functionality in the final edition of the project, the relationship between the database and the production environment has become multi-dimensional.

NGINX, listed as the tool used for 'live' production, is also a container, running as part of the swarms, and administering reverse proxy between Port 80 of the servers, and port 5000 of the frontend container.

The process flow I have used for this project mirrors closely that used by DevOps engineers in genuine enterprise environments, and to detail this, I have included a DevOps pipeline diagram, imagining the project as a part of a team oriented production environment.

![DevOps toolchain and process flow diagram for imagined enterprise environment.](https://i.imgur.com/t9O0jJE.png)

As can be seen from the representation, if compared to the previous documentation, a genuine business environment is not significantly different. In the imagined extension, the inclusion of postman testing would enable monitoring after deployment builds, and better use of GCP cloud management architecture could be used to ensure operations ran smoothly.

### Issues Encountered

+ Innumerable issues with GCP due to the strain put on services by the pandemic situation. In the end _all_ installation steps had to be commented out of my pipeline, as the downloads and data integrity couldn't be guaranteed. The lag put on services has caused a number of run on issues across the board.
+ Due to peculiarites of docker stack implementation, if you remove a stack, then immmediately rebuild it, it will crash, as it attempts to recreate the stack in the order it was removed. This causes build failure due to the lack of a supporting network. The quick and dirty solution is to introduce a lag until all containers drop from the `$ docker ps -a` list, but this introduces seconds of downtime into the service. One proposed solution would be to run multiple stacks, managed by a much larger load balancing system. That way downtime could be procedurally delayed across the entirety of the network.
+ Getting Selenium to function at all caused a full day's worth of issues. For some reason, potentially because of the afforementioned GCP problems, installing chrome and it's accompanying webdriver has become extremely difficult. In addition, the find_element_by_\[id/name]() function isn't working at all, for completely unknown reasons.
+ Despite modifying the `hosts` file in the OS of the Jenkins server, my original plan for obfuscating the Ansible configuration file had to be abandoned, and it was ported directly to the server, rather than being version controlled in an obfuscated format. The reason for this is unknown.

## Design Considerations

### Front End

In addition to the blockframe diagram shown in the proposal, a further blockframe diagram was produced to demonstrate the expansion of the project during its course.



### Back End

#### Generation

![Flow chart demonstrating process flow for the generators](https://i.imgur.com/fHCiX9z.png)

Code representation:

```{code goes here}
```

explanation of process flow and code

#### Service Interaction

![Flow chart demonstrating process flow for the interaction between services](https://i.imgur.com/fHCiX9z.png)

explanation of microservice architecture

#### Testing Structure

![Flow chart demonstrating process flow for the testing pipeline](https://i.imgur.com/fHCiX9z.png)

![Flow chart demonstrating process flow for the testing](https://i.imgur.com/fHCiX9z.png)

Code representation:

```{code goes here}
```

explanation of process flow and code

### UI

Potential logo

![CharGen Logo](https://i.imgur.com/8S5k1lK.gif)

#### Potential Expansions

explanation of site architecture

![Expanded blockframe diagram.](image)

Exploration of future versions.

## Testing

### Pytest

There are two main branches within the Pytest testing stream; url_testing, and db_testing.

Each of these are reflected in a separate stage within the Jenkinsfile pipeline instructions.

+ **url_testing**

The URL testing block pings each of the web pages in turn after a build to ensure that the site is up and callable, then verifies the results by pinging an absent 'negative' page.

7 tests are run.

1 for each page.

1 for an empty call.

Due to the complexity of called modules, coverage hovers around 46%.

+ **db_testing**

The database testing block spins a mirrored set of the mySQL tables in a separate database 'testing' on the instance. The database is wiped, and then each aspect of CRUD functionality is tested, mirroring the SQL structure of the flask functions.

17 tests are run.

The database is wiped.

Each table is CREATED, then checked for structure.

Each table is INSERTED into, then the UNIQUE keyword is tested.

Each table has a database entry UPDATED.

The FOREIGN KEY constraints are tested, before all entries are clean deleted.

Coverage averages 38%.

### Selenium

Selenium testing pending HTML [id] assignment.

### Final Report

Testing log stored on Jenkins server. Problems were encountered attempting to get the server to return testing documents to GitHub. It would be necessary to store GitHub login files as environmental variables on the server, which will be avoided for the project build. Currently the server is vulnerable to port mapping and injection, so account details will not be stored.

## Deployment

### Toolset

As of 2020/03/19.

+ GCP Instance development environment

+ GitHub Webhook

+ Jenkins Server

+ Pipeline build coded in Groovy and Shell.

+ Testing in Pytest using the Coverage module.

+ ~Front end testing in Selenium.~ [Not cooperating with mysql_db, fix pending]

+ 2 build run using debug mode and a GUnicorn 6 node mirror.

+ Final build deployment onto separate instance (currently inactive due to cost).

### CI Server Implementation

A jenkins server runs pipeline builds of the project, automating the testing functions, before deploying the website.

### Branch and Merge Log

Placeholder: polled Developer branch on 2020/

```branch and merge log for project
```

Discussion of VC server usage, and webhooks

## Front End Considerations

discussion

## Improvements for Future Versions

mop up discussion of improvements

## Installation and Setup Guide

#### Authors

THC - current QA Academy Trainee.

#### Acknowledgements

Thank you to everyone who offered help from the Cohort, and the various trainers whom I terrified with pointed questions.
