# shopping-cart

## Installation

Download this repo locally

Navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd shopping-cart
```

## Setup

Setup an virtual environment:

```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
```

Install some packages:

```sh
pip install -r requirements.txt
```

### Configuring Environment Variables

You will have to create your own local .env file. So you should add a new ".env" file to this repo, and put the following inside:


```
PLAYER_NAME="Guest 1"
```

## Usage

Run the game script:

```py
python shopping_cart.py