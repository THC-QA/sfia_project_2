# README
---
# Character Archetype Generation Microservices

Written in reference to QAC - Practical Project Specification (DevOps). This project is for the purpose of fulfilling the specification definition for the project assignment due Week 8 of the DevOps February 17 2020 intake cohort. The official working title of the project is SFIA Project 2 (independent), often reformatted to sfia_project_2 for tagging usage.

**If you're trying to install this project, and are disinterested in its creation and background, find the installation guide link in the table of contents, or follow it [here](#installation-and-setup-guide).**

## Table of Contents

1. [Project Brief](#project-brief)
    + [Proposal](#proposal)
2. [Trello Board](#trello-board)
    + [MoSCoW Analysis](#moscow-analysis)
    + [Start Point](#start-point)
    + [Rolling Changes](#rolling-changes)
    + [End Point](#end-point)
3. [Risk Assessment](#risk-assessment)
4. [Project Architecture](#project-architecture)
    + [Entity Relationship Diagram](#entity-relationships)
    + [Architecture Diagram](#overall-architecture)
    + [Issues Encountered](#issues-encountered)
5. [Design Considerations](#design-considerations)
    + [Front End](#front-end)
    + [Back End](#back-end)
    + [UI](#ui)
6. [Testing](#testing)
    + [Pytest Testing](#pytest)
    + [Selenium Testing](#selenium_testing)
    + [Final Report](#final-report)
7. [Deployment](#deployment)
    + [Toolset](#toolset)
    + [CI Server Implementation](#ci-server-implementation-and-configuration)
    + [Security](#security)
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

The data persistence required for the project was extremely simplistic. In this instance the textual representation of the JSON object generated by the microservices is passed to the MySQL database directly. Across the span until deployment, the persistence layer of the project didn't change, so the structure as demonstrated in this diagram remains.

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

In addition to the blockframe diagram shown in the proposal, a further blockframe diagram was produced to demonstrate the expansion of the project during its course. The expansion was largely to match the extension of the brief to include full CRUD functionality for the frontend container, whilst maintaining a single-page design.

[Blockframe diagram demonstrating the progression of the front end design.](https://i.imgur.com/MjCSrTp.png)

Notice the inclusion of UPDATE and DELETE sections to the existing form structure. Each of these follows a MySQLdb populated drop down menu, which fulfills the READ utility of the page. The pre-existing structure of the data persistence layer covers CREATE. In this way full CRUD functionality has been achieved.

As front end design was not a core consideration of the project, basic HTML structure was adhered to, resulting in the following end product. Notice the similarity to the expanded blockframe diagram.

[Demonstration capture of the final design state of the website homepage.](https://i.imgur.com/O2JVMmD.png)

A very simplistic design, but entirely covering the brief. For the purposes of avoiding leaking the server locations or user created data, a capture was taken of the test swarm homepage, and the URL was obscured. The advantages being that the website is easy to operate, and demonstrates a clear proof of concept. Further design could be carried out by a qualified web-designer, which I am not.

### Back End

#### Generation

To demonstrate the compliance with a dual-implementation generation brief, and demonstrate the complexity of the operation, the code and process flow from service 4 are layed out here. The API service call to services 2 and 3 in the flowchart each pass through a process flow similar to the one below, which can be examined in the flask apps found [here](https://github.com/THC-QA/sfia_project_2/blob/dev/service_2/application/__init__.py) and [here](https://github.com/THC-QA/sfia_project_2/blob/dev/service_3/application/__init__.py).

![Flow chart demonstrating process flow for the generator in service 4](https://i.imgur.com/ar5uW3W.png)

Code representation:

```@app.route('/', methods=['GET', 'POST'])
def home():
    enemies = ["Kings", "Dragons", "Demons", "Maidens", "Trolls", "Goblins", "Unicorns", "Beastmen", "Vampires", "the Undead", "Taxmen", "the Poor", "Passing Innocents"]
    titles = ["the Brave", "the Bold", "the Beautiful", "of Ill Repute", "Drunkard and Wastrel", "Inveterate Flirt", "the Terrible", "the Destroyer", "'Blackheart'", "Slayer of {0}".format(choice(enemies))]
    name = request.args.get("name")
    print(name)
    if 'test' not in name:
        if name == "Dave":
            name = name + ", " + titles[-1]
        name = name + ", " + choice(titles)
    perk = request.args.get("perk")
    print(perk)
    combat = request.args.get("combat")
    print(combat)
    modifier = get("http://modifier:5002/?perk={0}".format(perk)).text
    print(modifier)
    skill = get("http://skill:5001/?combat={0}".format(combat)).text
    print(skill)
    character={"Name":name,"Role":" ".join([perk,combat]),"Signature Skill":" ".join([modifier,skill])}
    return character
```

As can be seen from the chart and accompanying code block, if an API request is made to the service, a three part evaluation is made to the 'name' field, to decide the appropriate title to be appended. This section was intended as something of an 'easter egg', hence the arbitrary nature of the decision made.

Following this, the perk and combat fields are requested, and the data sent to services 2 and 3 by way of an API call using HTML arguments. The returns of these values are stored in variables, before the entire dataset is packaged as a python dictionary object; this object, on GET, will appear in service 1 as a JSON object, as the formatting is the same.

#### Service Interaction at Frontend

At the front end of the service, NGINX redirects port 80 webtraffic to port 5000 of the 'frontend' container. At this point the process flow that marks the entry to the API for the microservice swarm begins, as shown by the flowchart below.

![Flow chart demonstrating process flow for the interaction between services](https://i.imgur.com/NMhsHWF.png)

Code representation:

```@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        details = request.form
        content = "Please Submit"
        if "name" in details:
            name = details["name"]
            combat = details["type"]
            perk = details["perk"]
            content = get("http://title:5003/?name={0}&combat={1}&perk={2}".format(name,combat,perk)).text
            cur = mysql.connection.cursor()
            cur.execute("INSERT IGNORE INTO characters(data) VALUES (%s);", [content])
        elif "new_data" in details:
            data = details["data"]
            new_data = details["new_data"]
            cur = mysql.connection.cursor()
            cur.execute('UPDATE characters SET data = "{0}" WHERE id = {1};'.format(new_data,data))
        else:
            data = details["datad"]
            cur = mysql.connection.cursor()
            cur.execute('DELETE IGNORE FROM characters WHERE id = {};'.format(data))
        mysql.connection.commit()
        cur.execute("SELECT * FROM characters;")
        characters = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('home.html', content=content, characters=characters)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM characters;")
    characters = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('home.html', content="Please Submit", characters=characters)
```

This demonstrates how the microservice architecture is accessed from incoming API calls, when combined with the previous flowchart, it provides a high level overview for the algorithmic architecture of the service interactions. In a very real way this process marks as close as the programmatic aspects of the service provision gets to an end user.

As can be seen from the diagram, the webpage essentially has only 2 display states, as the rightmost two endpoints are identitcal. However, as they are accessed via different calls, it seemed appropriate to demonstrate the different choice structures that would navigate there, demonstrating three distinct branches for the function.

#### Testing Structure

Below is a quick overview of the structure of the testing environment, first from the perspective of the Jenkins pipeline itself, and then a deeper introspective on the structure of one of the Selenium module tests.

![Flow chart demonstrating process flow for the testing pipeline](https://i.imgur.com/y4OQWTN.png)

As can be seen from the flowchart, the testing environment is set up to be broadly similar to that of production. Docker swarm is similarly used to deploy the containers, but different environmental variables are supplied to keep the data persistence and CRUD functionality separate from deployment.

The tests follow a logical order; first checking the presence of the services, then checking the consistency of the database structure, before finally conducting front end tests on the website itself. This is achieved by using a chrome instance running in 'headless' mode, which will be explored further below. Once the testing has completed, the pipeline is ready to move on to configuring the deployment nodes using Ansible.

![Flow chart demonstrating process flow for the testing](https://i.imgur.com/GzZB95e.png)

Code representation:

```def test_character_deletion():
    with app.app_context():
        cur = mysql.connection.cursor()
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        driver.get("https://127.0.0.1/")
        multiselect_set_selections(driver, "datad", "PLACEHOLDER")
        driver.find_element_by_id("submit_delete").click()
        sleep(3)
        cur.execute("SELECT * FROM characters;")
        present = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert not present
        assert url_for('/') in driver.current_url
        driver.quit()
```

The code block can be split into three main segments, the setup of the drivers and connections required for the testing, the processing of the driver instructions and database polling, and then the assessment of the data collected. Of interest is the running of chrome (executable found at the .binary_location) in `'--headless'` mode. This is essentially a non-visual running of the chrome browser shell, suitable for the running of webdrivers on a terminal based system. For further information on running the process, please see [this](https://developers.google.com/web/updates/2017/04/headless-chrome) guide from a Google dev. For an in depth discussion of the use cases of this implementation, [this article](https://www.imperva.com/blog/headless-chrome-devops-love-it-so-do-hackers-heres-why/) may be of interest.

### UI

Potential logo

![CharGen Logo](https://i.imgur.com/8S5k1lK.gif)

#### Potential Expansions

A reasonable amount of added functionality would be required of the site architecture itself to count as a customer ready product. Already mentioned are a user and admin system, with the supporting backend architecture, and the implementation of sessions and cookies to hold user preferences and temporary data.

The deployment of the project could also be further improved by the addition of monitoring tools to the deployment stage, and also by stress testing the servers that the container nodes are deployed to.

To visualise how some of these expansions might be reflected in the design of the site, an extended blockframe has been included below.

![Expanded blockframe diagram.](https://i.imgur.com/7aCAnh4.png)

This blockframe aptly demonstrates an imagined future functionality for the website. Note the use of a navbar for the expanded pages, and a login feature for users or admins. An expanded backend could provide expanded or even adaptive generation sets, giving greater flexibility to users. This could fuel a pseudo-community, with more creative freedom given to users to create and populate character archetypes, potentially for use in shareware games or ttrpg projects.

## Testing

### Pytest

There are three main branches within the Pytest testing stream; url_testing, db_testing, and selenium_testing.

Each of these are reflected in a separate stage within the Jenkinsfile pipeline instructions.

#### url_testing

The URL testing block pings each of the web pages in turn after a build to ensure that the site is up and callable, then verifies the results by pinging an absent 'negative' page.

2 tests are run.

1 for the homepage.

1 for an empty call.

Due to the complexity of called modules, coverage hovers around 45%.

A typical coverage result is demonstraged below:

```+ python3 -m coverage run -m pytest tests/url_testing.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /var/lib/jenkins/workspace/sfia_project_2
collected 2 items

tests/url_testing.py ..                                                  [100%]

[...]

--------------------------------------------------------------------------------
TOTAL                                                        18855  10454    45%
```

#### db_testing

The database testing block spins a mirrored set of the mySQL tables in a separate database 'testing' on the instance. The database is wiped, and then each aspect of CRUD functionality is tested, mirroring the process flows of the frontend container. The testing set forms a stable loop, whereby a data object is created, updated, then deleted, returning the testing database its original state.

6 tests are run.

The database is wiped.

A testing table is CREATED, then checked for structure.

A data objected is INSERTED to the table.

The object is then UPDATED.

No FOREIGN KEYs are present in this iteration of the database, so the object is then DELETED.

Coverage averages 38%.

A typical coverage report is briefly outlined below:

```+ ./obfscripts/dbTesting.sh
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /var/lib/jenkins/workspace/sfia_project_2
collected 6 items

tests/db_testing.py ......                                               [100%]

[...]

--------------------------------------------------------------------------------
TOTAL                                                        35568  22219    38%
```

#### selenium_testing

As discussed previously, the selenium testing process runs a parallel set of tests to the database tests, but rather than running them directly through the mysqldb connection to the testing database, the front end of the app itself is tested by way of the chrome webdriver. Unfortunately, due to current issues with GCP, the selenium tests do not always complete on the Jenkins server, so an excerpt from a locally run test is included below.

5 tests are run.

The database is wiped, to avoid conflicts.

A 'character' table is created, to interface with the currently running `test_character_stack` swarm.

The character generation table is used to generate a JSON object to be persisted, the object is tested for coherence, then the persistence success is evaluated.

The data update table is used to update the recently created object to the value 'PLACEHOLDER', and the update is checked.

The data deletion table is used to delete the object with value 'PLACEHOLDER', and the deletion is checked.

Coverage is typically 40%.

A typical (abreviated) coverage report is shown below:

```+ ./obfscripts/seleniumTesting.sh
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /var/lib/jenkins/workspace/sfia_project_2
collected 5 items

tests/selenium_testing.py ..FFF                                          [100%]

[...]

---------------------------------------------------------------------------------
TOTAL                                                         41999  25217    40%
```

### Final Report

Testing log stored on Jenkins server. As with the previous project, no demand was made for the export of testing documents, beyond their local persistence. As such it was not implemented.

As an engineer's note, the means by which the coverage module calculates its values is entirely opaque, and makes very little sense. Higher scores can be achieved seemingly by importing app objects from the original codebase, and from specifying the scope of the testing environment to _only_ project local files. However, this could be considered cheating the coverage tests, so they have been left as found.

## Deployment

### Toolset

As of 2020/04/11.

+ GCP Instance development environment
+ GitHub Webhook
+ Jenkins Server
+ Pipeline build coded in Groovy and Shell.
+ Testing in Pytest using the Coverage module.
+ Front end testing in Selenium. {The webdriver on the Jenkins server is currently taking too long to respond, due to ongoing GCP issues.}
+ Configuration of deployment nodes using Ansible.
+ Final build deployment onto two separate instances, utilising Docker Swarm.
+ Security by way of GCP Firewall rules, and NGINX reverse proxy setup.

### CI Server Implementation and Configuration

A Jenkins server runs pipeline builds of the project, automating the testing functions, before deploying the website. It's open source nature makes it perfect for utilisation on a free tier project such as this, and ready integration with the other toolsets used, particularly by way of Git webhooks, is particularly advantageous.

The twin concepts of continuous integration and deployment are central to the DevOps ethos, and this project demonstrates some of the core functionality behind it. By way of project contribution, builds can be triggered automatically, and testing performed locally before deployment to nodes.

The use of Ansible is key to preparing the nodes by way of non-local install, and configuring them to initialise a docker swarm layer between the servers. This can then be connected to via Jenkins itself for deployment.

### Security

In order for the project to remain secure, a number of precautions were taken over its lifespan, as detailed below:

+ The SQL server is configured to only accept connections from the 3 active VMs.
+ All of the VMs are configured to accept swarm port traffic only from each other. Details found [here](https://docs.docker.com/engine/swarm/swarm-tutorial/#open-protocols-and-ports-between-the-hosts).
+ The Manager and Worker node are configured to act as http servers, to enable the swarm to display content.
+ The Jenkins server allows in and outbound port 80 traffic for the dual purpose of receiving webhooks and testing swarm content.
+ Port 8080 on the Jenkins server allows content from the workstation, to allow configuration and builds.
+ `test.env` was copied directly to the Jenkins server to avoid exposure.
+ `api.env` was copied directly to the Jenkins server to avoid exposure.
+ `inventory.cfg` was copied directly to the Jenkins server to avoid exposure.
+ The above configuration and environment files were replicated in the hosts and .bashrc file as precaution.
+ The above configuration and environment files were filtered by the .gitignore and .dockerignore files to avoid exposure.

### Branch and Merge Log

Log at time of README update: polled Developer branch on 2020/04/11

```* 0b8647f (HEAD -> dev, origin/dev) name
* e1f724e url
* d5fd3c2 chrome location
* ec2f063 selenium2
* 24b72c5 selenium
* 6b672e7 replicas
* f3ad34b permissions
* 332b740 no stack
* 9b5e462 specificity
* 733bae4 chmod
* c5ef40d syntax
* 9a0bf91 no install
* cd503ea none
* 0940e7b foo
* 1c9ef8f agents
* c08a370 further adventures of errors
* 637cccd confusing errors
* c51d16f docker issues
* b957d07 purge
* 2a9267f remove
* 9d6bca7 containerd
* ea95afd servers 'all'
* 7e1c48f cfg removal
* af02361 source
* 857bb4b config
* c1e9a5f titles
* 3d1e8d2 -y
* bac8080 no get
* f8908ea sudo vs pip
* 5939379 ansible and node test
* d69adf1 full CRUD
* 47f2260 values
* 07cfba4 back to bash
* 658783b secrets
* 6c9d662 primary key
* 27081ee brackets
* ec991fc square brackets
* ccaa2e7 more source issues
* ee086fd config issues
* 9b637a3 bashrc
* 10cbb1b paths
* c704643 permissions redux
* 65fc417 obfuscation
* fd03905 source
* acc3bed env
* ab11700 sleep
* 487880a urltest
* 25336a8 urltest
* 06ae3ef swarm
* 42c574b venv
* 2437c49 test
* 966384a commenting
* 565ee68 groupadd
* 316796f groupcheck
* 4ef6bd2 user
* d0fa50a whoami
* 0562d9d pipeline issues
* 982c1be selenium start
* d662302 rearrange
* 36daeb4 absolute paths 2, the absolutening
* 1e5a112 version zero doesn't exist
* 2fa782a recursive
* c8a622e the further adventures of absolute paths
* dc62623 non source shell
* 6f4c21b even more absolute path
* 8eb6127 absolute path
* 4065d49 permissions
* 2d4cd84 pipeline order
* d9c6304 capitalisation
* 3b82024 docker issues
* 6783882 newgrp password
* 0d28e18 of course the pipeline isn't working
* 6a6fbec pipeline trial run
* f98fe77 fixed swarm, pipeline started, playbook initialised
* 634bce3 compose updated for swarm
* 5fe376c pre swarm compose
* c4e1c75 removed venv
* 3d788c7 cookie version, not working
* 9e6accc services 1-3 working
* 0285b22 dev branch started, post concerns
* 58b66e9 (origin/master, master) missed one
* 414ad84 first commit
```

Git as a version control service is used for 4 primary functions in this project:

1. To safeguard the build history of the files, and enable the gradual integration of working features. This is running alongside the similar version control of the DockerHub system. To this end the master branch of this repository is currently (2020/04/11) at the stage where it could be run in terminal at a local level, whereas the developer branch has been used for building the CI/CD, configuration management and testing functionality of the project. A versioned history of the containers built from the services is available at my [DockerHub page](https://hub.docker.com/repository/docker/thcqa), though prior versions of the containers themselves have not been tagged, to avoid confusion during the projects progression. Merges are unlikely to happen until after the completion of this project, as Jenkins is polling the dev branch.
2. To enable webhook triggers for pipeline builds, a webhook system has been enabled between the dev branch of the repository here and the Jenkins server. Unlike an enterprise environment, the completed builds don't trigger merges, so in a sense the CI/CD functionality of the project can be considered incomplete. Mirroring this system, as mentioned in the [security](#security) section, the firewall rules of the Jenkins server have been ammended to allow the webhook to function.
3. To allow diverse location working on the project, from home, work, and whilst travelling. So long as an internet connection is present, the project can be pulled for revision.
4. GitHub itself, as a public hosting for the project, and to make it available for open source cooperation or download, in line with the ethos behind the movement.

## Front End Considerations

discussion

## Improvements for Future Versions

To summate the potential improvements mentioned over the course of the README:

+ The data persistence layer could be increased first in complexity, and then to enable further functionality from the website itself. Detailed [here](#entity-relationship-diagram).
+ Services such as user login and admin maintenance could be added, along with the supporting front end provision. Detailed [here](#ui).
+ Expanded functionality could be given to the CI/CD and deployment process itself:
    + Deploy to more nodes.
    + Change update method to incorporate polling DockerHub webhooks.
    + Expand after-deployment processing to automate merge requests.
    + Include team messaging reports to slack or MSTeams.
    + Include operations management using GCP tools.
    + Include Postman monitoring for deployment.
+ Testing could be expanded to include stress testing of containers.
+ Testing could be expanded to include stress testing of VMs.
+ Testing could be expanded to include stress testing of frontend, by expanding Selenium functionality.

An example KanBan board is included below to outline what a sprint might look like, focussing on the potential tasks necessary to expand the data persistence layer. As opposed to the simplistic single user approach to the brief, user stories have been used to illustrate the necessities brought forward by the increased scope.

![An imagined kanban board for the database sprint of an updated project](https://i.imgur.com/OhgluoH.png)

To pair with this imagined sprint, a potential risk assessment has been provided, in simplified form, below:

|Risk Code|Potential Risk|Potential Impact|Hypothetical Preventative Measure|
|---|---|---|---|
|0.0.1|Sensitive data is stored incorrectly.|4|Personal data should be encrypted, and passwords hashed prior to persistence.|
|0.0.2|Data is collected unnecessarily.|5|Appropriate legislation, such as GDPR, should be researched and adhered to.|
|0.0.3|Permissions over data is incorrectly assigned.|4|Carefully manage privileges, and make use of a suitable logging system.|
|0.0.4|Scheduling conflicts cause untenable workflow.|3|Schedule the sprint for a point where all interested parties have enough free time.|
|0.0.5|Run out of free tier GCP usage.|2|Switch to a different provider, source funds from interested parties.|

## Installation and Setup Guide

1. Make sure you have access to at least 2 webservers, preferrably 3. The servers should ideally be running Ubuntu server edition 18.04, as this project is intended for that setup. You will also need a MySQL server, for the data persistence layer.
2. Using ssh-keygen (guide found [here](https://www.ssh.com/ssh/keygen/)), generate keys for using SSH to connect to the servers, and ensure they have copies of your public key in the list of allowed clients.
3. On one of them, install Jenkins, following the guide found [here](https://www.techrepublic.com/article/how-to-install-jenkins-on-ubuntu-server-18-04/). You will need port 8080 exposed in order to access the Jenkins client. Configure this in your firewall rules. For the rest of the guide, the server with Jenkins on it will be referred to as the 'Jenkins server'.
4. SSH to the Jenkins server, and run the command `sudo su jenkins` to run as the Jenkins user. Navigate to the root directory using `cd ~` and create the file .bashrc using the command `touch .bashrc`. This will be used later.
5. Follow your preferred method from the range [here](https://embeddedartistry.com/blog/2017/11/16/jenkins-running-steps-as-sudo/) to allow Jenkins to run as a sudo user.
6. Install chrome using the terminal section of the guide found [here](https://www.linuxbabe.com/ubuntu/install-google-chrome-ubuntu-18-04-lts).
7. Install chrome webdriver using step three of the guide found [here](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/).
8. SSH to the other server(s) and install the most up to date version of jdk, to allow Jenkins to later access them. Follow the guide found [here](https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html).
9. Using a copy of your private key, set the other servers up as Jenkins nodes, following the wiki instructions found [here](https://www.howtoforge.com/tutorial/ubuntu-jenkins-master-slave/).
10. Fork a copy of this repository, and edit the jenkinsfile to reflect your naming conventions for nodes. In the default version of this project, the nodes are expected to be named 'manager-node' and 'worker-node'.
11. Using the guide found [here](https://embeddedartistry.com/blog/2017/12/21/jenkins-kick-off-a-ci-build-with-github-push-notifications/) configure your copy of the repository to allow webhooks.
12. Completing the procedure, use the guide found [here](https://dzone.com/articles/adding-a-github-webhook-in-your-jenkins-pipeline) to add the webhook to your Jenkins server.
13. Configure the firewall rules to match those found in the [security](#security) section of this README.
14. Push your project, triggering a first build, which will fail. This is intended.
15. SSH back to the Jenkins server and create two files in the cloned repository: api.env, and inventory.cfg
16. The contents of the api.env file should be filled with the following environment variables: SECRETKEY, MYSQLHOST, MYSQLUSER, MYSQLPASSWORD, and MYSQLDB. These should be configured to allow access to your SQL server instance. No quotation marks are required, but no spaces are allowed. As an example `MYSECRETKEY=thisisanexamplesecretkey`, note the lack of spaces.
17. Copy the contents of this file to the .bashrc file created earlier. Add quotation marks to your variables, change the MYSQLDB variable to point toward your testing database, and add the word 'export' before the variables. An example should look like `export MYSECRETKEY="thisisanexamplesecretkey"`, note the space before the variable.
18. Edit the inventory.cfg file to include connection instructions for 'manager-node' and 'worker-node'. For formatting guidelines, follow the guide found [here](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html). The ssh commands will need to be provided, and a path to the same version of the ssh key placed in step 9.
19. Congratulations, your build of this project should be ready to run. The project is available completely under the GNU General Commons license, a copy of which is included for posterity with this repository. It is also linked [here](https://www.gnu.org/licenses/gpl-3.0.en.html).

#### Authors

THC - current QA Academy Trainee.

#### Acknowledgements

Thank you to everyone who offered help from the Cohort, and the various trainers whom I terrified with pointed questions.
