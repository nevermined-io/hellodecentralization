[![banner](https://raw.githubusercontent.com/nevermined-io/assets/main/images/logo/banner_logo.png)](https://nevermined.io)

# Hellodecentralization Nevermined Workshop
> Nevermined: Leveraging Blockchain to Unlock Data for Federated Learning

In this workshop we will be presenting the [Nevermined](nevermined.io) data ecosystem being developed by [Keyko](keyko.io). This will be a follow along session and so we encourage all attendees to perform the setup describe in this repo prior to the workshop. We will start by giving and overview of what Nevermined is and what it can do and we will follow that with a follow along coding session focused on the Data In-Situ Computation (DISC) capabilities of Nevermined.

This workshop will be based on the [Credit Card Fraud Detection Demo](https://medium.com/nevermined-io/nevermined-credit-card-fraud-detection-91aef362d98) which we wrote about previously.

- [Hellodecentralization Nevermined Workshop](#hellodecentralization-nevermined-workshop)
    - [Agenda](#agenda)
    - [Setup](#setup)
      - [Requirements](#requirements)
      - [Setup and start nevermined](#setup-and-start-nevermined)
      - [Setup the workshop repo](#setup-the-workshop-repo)

---

### Agenda

1. Introducing Keyko
2. Overview of Nevermined
3. Follow along workshop
   1. Data publish and consume flow with the marketplace
   2. Publishing data for compute
   3. Publishing algorithms
   4. Running a distributed compute job over multipe datasets with Federated Learning
4. Q & A

### Setup

#### Requirements

- python
- [python virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- docker
- docker-compose

We need to setup both nevermined and the environment for this workshop

#### Setup and start nevermined

1. Clone the [nevermined-tools repo](https://github.com/nevermined-io/tools)
```bash
$ git clone git@github.com:nevermined-io/tools.git
$ cd tools/
```

2. Start Nevermined
```bash
$ ./start_nevermined.sh --events-handler --compute --latest
```

3. Wait for all the services to be up and running. This may take a few minutes
```bash
$ ./scripts/wait_for_compute_api.sh
```

#### Setup the workshop repo

0. If you don't have virtualenv you can install it with
```bash
$ pip install virtualenv --user
```

1. Create a new virtual environment for the workshop
```bash
$ virtualenv venv
$ source venv/bin/activate
```

2. The new dependency resolution in pip creates problems with the nevermined sdk so we are going to use a previous version
```bash
$ pip install pip==20.2.4
```

