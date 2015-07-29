Tournament Results
=============

###Getting Started

You will need [Vagrant](http://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/wiki/Downloads).

If you have trouble, check out this [wiki entry from the helpful folks @ Udacity](https://www.udacity.com/wiki/ud197/install-vagrant)

###To Run

1. Download or clone this repository
2. `cd` into  `/vagrant/tournament` 
3. Start Vagrant and `cd` into `/vagrant`
    ```
    vagrant up
    vagrant ssh
    cd vagrant
    ```
4. Use psql to generate SQL DB
  ```
  psql
  \i tournament.sql
  \q
  ```
5. Run Tests
  ```
  python tournament_test.py
  ```
  
