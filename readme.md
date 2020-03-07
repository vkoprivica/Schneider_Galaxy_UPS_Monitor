## Schneider Galaxy 5000 UPS Monitor

Purpose of this Python application is to provide enhanced monitoring of Schneider Galaxy 5000 UPS battery charge and remaining backup time. Currently, SNMP monitor shipped with device does not have a capability of reporting drift of battery change in increments of 10%. This monitor will kick off an email every time drift or increment in battery charge is more than 10% as well as remaining backup time reaches 30 minutes of threshold. 


### Application structure

ups_monitor.py – Python file contains functions necessary to parse data and obtain required parameters. 
ups_program.py – Python file contains monitoring intelligence, error handing, logging and notification features.  


### Instructions

Place ups_program.py and ups_monitor.py files into the same directory. 
Create subfolder for logging named “log”. 
Start ups_program.py or create the cron job to execute the file. 


### Requirements

Python 3.6 



<!-- ### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->
