

Please install on your system

- git
- build-essential

for legacy version also you are going to need:

- libssl-dev
- libgmp-dev

On Debian based systems, run this commands to update your current enviroment
and install the tools needed to compile it

```
apt update && apt upgrade
apt install git -y
apt install build-essential -y
apt install libssl-dev -y
apt install libgmp-dev -y
```

To clone the repository

```
git clone https://github.com/albertobsd/keyhunt.git
```


```
cd keyhunt
```

First compile:

```
make
```

if you have problems compiling the `main` version you can compile the `legacy` version

```
make legacy
```


and then execute with `-h` to see the help

```
./keyhunt -h
```

BSGS : 

I also need to make some test in testnet network if you have some Testnet balance can you help me with donations in my testnet address:

Address: msKcxhizYWVvxCACFEG4GCSK1xYrEkib5A

Thank you.
