
# Ethereum Key To Ganache

Loads [ethereum keystore](https://goethereumbook.org/keystore/) file and converts
it to [`--account`](https://github.com/trufflesuite/ganache-cli#options) option 
entry accepted by [ganache-cli](https://github.com/trufflesuite/ganache-cli).

## Setup

1. Install: 
   - [pyenv](https://github.com/pyenv/pyenv#installation)
   - [pipenv](https://pipenv.kennethreitz.org/en/latest/#install-pipenv-today)

1. Execute:
    ```sh
    pyenv install 3.7.3
    pipenv --python 3.7.3
    pipenv install
    ```

## Usage
Execute command:
```sh
pipenv run python key_file_convert.py { path_to_key_file }
```

Sample output:
```sh
Private key: 
0x0d93d656fdb84ce4caf35a081bb0561c7d3ce928f39176505899c78d9d030176
Ganache argument:
--account="0x0d93d656fdb84ce4caf35a081bb0561c7d3ce928f39176505899c78d9d030176,100000000000000000000"
```

Use generated value in `ganache-cli` command, e.g.:
```zsh
ganache-cli \
  --account '0x0d93d656fdb84ce4caf35a081bb0561c7d3ce928f39176505899c78d9d030176,100000000000000000000' \
  --account '0xaa317fc7d3e754448de03fd53373d3df1651c21524e2f57424f543b572867d82,100000000000000000000'
```
