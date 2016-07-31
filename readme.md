# ```$_Hacks```

dead simple restful api framework

## $ Get Start
### New a project
<code>$ hack new demoAPI</code>

### Generate restful api
(example for user resource) <br/>
<code>$ hack generate api users</code>

## $ Enjoy Your API:)
(example for user resource)
### Start

    $ python manage.py runserver

recommended [postman app](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop) do api development<br/>

### Read
**GET**  <code>http://localhost:5486/api/users/</code>

### Create
**POST** <code>http://localhost:5486/api/users/</code>

    {
        "username": "neo1218",
        "email": "neo1218@yeah.net"
    }


### Update
**PATCH** ```http://localhost:5486/api/users/<id:1>/``` <br/>
***update a field:***

    { "email": "hacks1218@yeah.net" }

### Delete
***delete a user*** <br/>
**DELETE** ```http://localhost:5486/api/users/<id:1>/``` <br/>

### Pagination
**GET** ```http://localhost:5486/api/users/?page=1```

### Search
**GET** ```http://localhost:5486/api/users/?<field>=<value>```

## $ Hack Your API
you can custom your api by adding/deleting field: <br/>
**add a new field** <br/>
**POST** <code>http://localhost:5486/api/?rescs=users</code>

    {
        "field": "nickname",
        "type": "String(164)"
    }

***all field types:***

+ String(length)
+ Integer
+ Text
+ DateTime(default is utcnow)

after launch the POST request, you need to migrate and upgrade your database to
the latest table structure.

    $ python manage.py db migrate
    $ python manage.py db upgrade

## $ Learn More Hacks
Hacks based on flask and flask plugins

+ [flask website](http://flask.pocoo.org/)
+ [flask plugins](http://flask.pocoo.org/extensions/)

## $ Notes
Currently, Hacks simply generate a **prototype api**, which means the api **did
not** have: 

1. **authentication mechanism**
2. **relationship between each api resource**,
3. **rate limit**
4. **http caching** 
5. **user side config**
6. **invoke your own code**

and obviously, it ***not ready to go into production***;
<hr/>
But, I will continue to feed more on Hacks, and finally let Hacks become a
**production-oriented**  but **deadly simple** restful api framework.

## $ LICENSE
MIT, check LICENSE file for detail
