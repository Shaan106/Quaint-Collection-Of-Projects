
# BCI simulator

Shaan Yadav, Muhammed Ugur, Raghav Pothukuchi, Abhishek Bhattacharjee \
Duke University, Yale University

## Background

Brain computer interfaces (BCIs) provide opportunities to treat neurological disorders, better understand how the brain functions and seamlessly interface the brain with the digital world. BCIs today are created as hyper specific ASICs that are efficient at solving a singular problem. More general-purpose architectures are needed to expand the computational abilities of BCIs, leading to greater benefits and wider adoption, however, traditionally these systems are not able to meet the strict performance and power constraints of BCIs.

## The Problem

The HALO architecture created in Professor Bhattacharjee's lab at Yale provides a general-purpose architecture for implantable BCIs, capable of treating many neurolgical disorders while keeping under the strict 15mW power limit. However, the development of more general purpose BCIs is heavily limited due to the lack of infrastructure to develop BCIs and be able to evaluate their performance quickly and efficiently, especially when it comes from taking high-level ideation to tape outs of custom hardware.

## The Solution

We aim to build a highly modular simulator that allows for rapid development and evaluation of BCI 'pipelines'. This tool will allow professionals to come in with ideas, such as for seizure detection, and make use of pre-built accelerator set architectures to quickly evaluate their ideas, first at a high level then using rtl implementations. The tool will allow the user to get detailed information and visualization such as for power estimation, and that will allow for informed changes to aspects of their pipeline, such as the clock frequency of different componenets or buffer sizes or compression ratios.

## Processing Elements [fft]

The simulator is built to be very modular, and 'processing elements' are the main building block used in the simulator. Each element has a very specific function and is developed in python first for quick prototyping and proofs of concepts, and then in rtl to get more accurate evaluation metrics. Each processing element has strict data validation techniques ensuring the correct shape and type, visualizations of the input/output data as well as important performance metrics pre and post RTL such as power estimation and expected latency.

## Pipelines [Seizure]

h

## Multi-Pipeline designs

## Computation graph

## Future
optimisation of a collection of architectures
fast computation as the data scales up (SCALO)

## References
HALO paper
Shiao paper