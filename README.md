# Techmergency CodeTheCurve2020 Submission

## The Problem Statement

COVID-19 has put massive pressure on the global health sector and frontline healthcare workers' lives at risk, due to the lack of personal protective equipment (PPE), medical devices, and funding that is needed.

Since the beginning of the outbreak, the Operations Support and Logistics (OSL) unit at WHO has shipped more than 900 000 surgical masks, 62 000 N95 masks, 1 million gloves, 115 000 gowns, 17 000 goggles and 34 000 face shields to 133 countries. OSL has also shipped COVID-19 testing kits to 126 countries.

There is a need to ensure that health workers on the frontlines have access to necessary protective equipment and that infected patients also have access to ventilators because as we speak, physicians in several countries have already begun making the difficult decision of who to save and who not to save!

## Our Solution

The quickest fix? Mobilize funds.

We want to flatten the curve by doing what we know best, coding our way through it.
Our idea is to create a software, an internet-based platform that connects donors with medical institutions around the globe. Companies, individuals, institutions and NGOs can easily, via the platform help to bridge the gap between medical institutes/ health care workers and the needed lifesaving equipment and resources.

## Technology Stack

Our solution will be built using React for the front-end, and consume APIs powered by Node.js. The entirety of the service will be deployed on DigitalOcean droplets.

- Frontend: React
- Backend: Node.js
- Database: MongoDB
- Deployment: Ubuntu environ hosted in DigitalOcean droplets

## Prototype

Click [this link](https://www.figma.com/proto/TIR6cad01j7oFTHvomGjXb/Techmergency?node-id=1%3A2&viewport=173%2C633%2C1&scaling=min-zoom) to browse a high-fidelity prototype of our product.

![Technical Architecture](/Technical_Architecture.jpeg)
![Solution Diagram](/Solution_Diagramm.jpeg)

## Miscellanous

As part of our implementation, Techmergency will design an algorithm that will distribute resources to frontliners based on some defined criteria. We have designed a first version of this algorithm to validate our theories.

The algorithm can be found in the [distribute_resources.py](/distribute_resources.py) file. The easiest way to run this algorith is to visit [this link](https://repl.it/repls/BruisedGregariousAssignment) and click the _run_ button. You will be greeted with some prompts which you should respond to.
