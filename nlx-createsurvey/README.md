# nlx-createsurvey
This is a microservice suvey-making tool in python (prototype). Surveys can either be made in python (created by [@Jim Schwoebel](https://github.com/jim-schwoebel)) or in the [react/Node.JS template]() (created by [@Drew Morris](https://github.com/drewry) and [@Russell Ingram](https://github.com/russell-ingram)).

![](https://media.giphy.com/media/3oz8xYfQd5358zpL0s/giphy.gif)

Please feel free to contact me @ js@neurolex.co with any questions.

Happy survey-making!!

-Jim 

## Should I use the Python or Node.JS template?

For some applications (e.g. collecting voice samples in a primary care clinic with pre-loaded ML models), online sampling may not be necessary and it may be more secure to sample offline. In other applications (e.g. market research survey interview), online sampling is necessary to scale across multiple states and geographies.

To begin, first ask yourself whether you need to create a survey in an online or offline capacity. If the survey can be deployed in an offline capacity, use the python/html survey template. If the survey needs to be deployed online, use the Node.JS React template. 

Each of these templates are described in greater detail below in terms of how to set them up.

## Getting Started: Python template 

The Python/HTML survey is intended to be used in **offline applications** or in **applications where the kafka architecture does not need to be used.** It is tied to NeuroLex's shared server on [Site 5 backstage](https://customers.site5.com/clientarea.php). 

To begin, you can install all the dependencies by:

    cd ~
    git clone git@github.com:NeuroLexDiagnostics/nlx-createsurvey.git
    cd nlx-createsurvey
    python3 setup.py 

Now you should be good to go if you are working with the .html survey. You can now run this script in the terminal:

    python3 nlx-createsurvey.py
    
You should then be prompted a list of questions to create a survey like:
    
    what is your company name?
    what is the purpose of the survey (e.g. to improve future events)?
    how many open-ended (20 second) questions do you want for your survey?
    what is the open-ended question number 1? 
    how long do you want as a response (in seconds)? (30 second max)
    ....
    [will go until the end of the survey is reached]

Note that voice recognition is integrated into the survey and survey responses are collected in the nlx-createsurvey/sample survey folder. These are labeled as a surveyID_quesition#.wav. 

Note that there are also a lot of configuration files for the survey; for example:

    0.htlm
    1.html
    baseline.html
    baseline2.html
    finish.html
    startup.html
    logo.wav
    terms.wav 

These configuration files are needed to load the survey into the future. 

A sample ID is also created for the survey to track results into the future. To extract results from the survey ID you can just look into the designated folder on the site 5 server. 

For additional documentation, read through the wiki [here](https://github.com/NeuroLexDiagnostics/nlx-createsurvey/wiki).

## Getting Started: React/Node.JS template

The Node.JS / React survey is used for **online applications** or in applications where **voice and standard surveys need to be done together.**

First, check to see if you have node installed using:

    node -v

If you get the response below you need to install node:

    -bash: node: command not found
    
You can install node with Homebrew:

    brew install node 
    
If you do not need to install node, you can move to the next section.

To develop locally, clone the repo:

```
cd ~
git clone git@github.com:NeuroLexDiagnostics/pilot-survey-react.git
```    

You can then run the npm install command:
```
npm install
```

The default port in `webpack.config.js` is `8080` but can be changed.

To launch:
```
npm start
```

Then visit `localhost:PORT` to view the project.

We have a python script to quickly make surveys. To do this follow these steps in the terminal:

    cd ~
    cd pilot-survey-react 
    python3 create-survey-react.py

You will then be asked a few questions to customize the survey, such as:
  
    what is the company name? (leave blank to use neurolex as company)
    what is the link to a logo for the company? (leave blank for neurolex logo link)
    what is the name of the survey?
    what is the purpose of the survey
    ...

The result will output the survey in the react folder as config.js and questions.js files. 

Now launch the server:

    npm install
    npm start

Now view the live link @ localhost:8080 in a google chrome browser. 

If there are no errors, you should see your survey pop up.

You can see more documentation about the setup of this template [here](https://github.com/NeuroLexDiagnostics/pilot-survey-react).

## References

Most of our references are from existing pilots or customers. Here are some:

### Python template

* [Voice donations / StressLex]()

### Node.JS template

* [Cambridge Analytica]()
* [Mental Health America]()
* [Schizophrenia.com]()
