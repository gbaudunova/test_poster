# Poster

A Django webapp for posting blogs to the 4 largest resources (Hacker News, Reddit, Habrahabr, Golang News) for IT professionals.

## Getting Started

### Prerequisites
To create an own copy of this application, you have some prerequisites. They are:
- [Python] - installed on your system
- A [Hacker News], [Reddit], [Habrahabr], [Golang News] accounts for authentification

### Installing

1. Download the project and extract it or clone the repo
```
$ git clone https://github.com/gbaudunova/Spamer_blog.
```
2. Create and activate virtual environment
```
$ virtualenv poster
$ source poster/bin/activate
```
3. Install al dependencies using for run the project
```
$ pip install -r requirements.txt
```
4. Before run the project you should create your own admin user
```
$ ./manage.py createsuperuser
```
5. You can start the server using this commands:
```
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
Now, you have your own copy of this application!

### Running the tests
```
$ ./manage.py test
```
### Todos

 - Write MORE Tests

### Authors
 - [Denis Grushkin]
 - [Gulbustan Baudunova]




   [Python]: <http://www.python.org>
   [Hacker News]: <https://news.ycombinator.com>

   [Reddit]: <https://www.reddit.com>
   [Habrahabr]: <https://habrahabr.ru>
   [Golang News]: <https://golangnews.com/>
   [Denis Grushkin]: <https://github.com/denisoed>
   [Gulbustan Baudunova]: <https://github.com/gbaudunova>

