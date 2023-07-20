# EWP Models

![GitHub release (latest by date)](https://img.shields.io/github/v/release/CIAT-DAPA/lswms_models) ![](https://img.shields.io/github/v/tag/CIAT-DAPA/lswms_models)

## Features

- Built using Mongoengine for MongoDB
- Supports Python 3.x

## Getting Started

To use this Models, it is necessary to have an instance of MongoDB running.

### Prerequisites

- Python 3.x
- MongoDB

## Usage

This ORM can be used as a library in other Python projects. The models are located in the my_orm/models folder, and can be imported like any other Python module. To install this orm as a library you need to execute the following command:

````bash
pip install git+https://github.com/CIAT-DAPA/lswms_models
````

If you want to download a specific version of orm you can do so by indicating the version tag (@v0.0.0) at the end of the install command 

````bash
pip install git+https://github.com/CIAT-DAPA/lswms_models@v0.2.0
````

## Models

### Adm1

Represents a Adm1 (Zone) in the database.

Attributes:

- name: `str` Name of the Adm1(Zone).
- ext_id: `str` external id from the Adm1(Zone). Mandatory.
- trace: `dictfiel` dictfiel with created time, updated and a status from the Adm1(Zone). Mandatory.

### Adm2

Represents a Adm2 (Woreda) in the database.

Attributes:

- name: `str` Name of the Adm2(Woreda).
- ext_id: `str` external id from the Adm2(Woreda). Mandatory.
- trace: `dictfiel` dictfiel with created time, updated and a status from the Adm2(Woreda). Mandatory.
- adm1: `ObjectId` Adm1 Reference id (zone). Mandatory.

### Adm3

Represents a Adm3 (Kebele) in the database.

Attributes:

- name: `str` Name of the Adm3(Kebele).
- ext_id: `str` external id from the Adm3(Kebele). Mandatory.
- trace: `dictfiel` dictfiel with created time, updated and a status from the Adm3(Kebele). Mandatory.
- adm2: `ObjectId` Adm2 Reference id (woreda). Mandatory.


### watershed

Represents a watershed in the database.

Attributes:

- name: `str` Name of the watershed. Mandatory.
- area: `float` Area of the watershed. Mandatory.
- trace: `dictfiel` dictfiel with created time, updated and a status from the watershed. Mandatory.
- adm3: `ObjectId` Adm3 Reference id (kebele). Mandatory.
    

### waterpoint

Represents an waterpoint in the database.

Attributes:

- name: `str` Name of the waterpoint. Mandatory.
- lat: `float` Latitude of the geographical location where the water point is located. Mandatory.
- lon: `float` Longitude of the geographical location where the water point is located. Mandatory.
- area: `float` Area of the waterpoint. Mandatory.
- trace: `dictfiel` dictfiel with created time, updated and a status from the waterpoint. Mandatory.
- ext_id: `str` External identifier for the waterpoint.Mandatory.
- other_attributes: `array` Additional attributes of the waterpoint. Optional.
- climatology: `array` Array with the historical data for the waterpoint. Mandatory.
- watershed: `ObjectId` Watershed Reference id. Mandatory.

### monitored

Represents an the monitored values from waterpoint in the database.

Attributes:

- date: `datetime` Date from the historical data. Mandatory.
- values: `array` Values of the monitored values. Mandatory.
- waterpoint: `ObjectId` Waterpoint Reference id. Mandatory.

### type_content

Represents an type of content in the database.

Attributes:

- name: `str` Name of the type of content. Mandatory.

### wp_content

Represents an waterpoint content in the database.

Attributes:

- content: `array` Array with the diferent content of the waterpoint. Mandatory.
- waterpoint: `ObjectId` Waterpoint Reference id. Mandatory.
- type: `ObjectId` type_content Reference id. Mandatory.

### ws_content

Represents an watershed content in the database.

Attributes:

- content: `array` Array with the diferent content of the waterpoint. Mandatory.
- watershed: `ObjectId` Watershed Reference id. Mandatory.
- type: `ObjectId` type_content Reference id. Mandatory.
