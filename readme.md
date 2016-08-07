# ```$_Hacks```

dead simple restful api framework.
in development

## $ Get Start
### New a project
<code>$ hack new demoAPI</code>

### Generate restful api
<code>$ hack generate api users</code>

### Videos
+ [hacks framework](https://www.youtube.com/watch?v=aimpIJjk824)

<hr>
## $ Enjoy Your API:)
(example for users resource)
### Start

    $ hack boot

recommended [postman app](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop) do api development<br/>

### Read
**GET**

+ <code>http://localhost:5486/api/users/</code>
+ ```http://localhost:5486/api/users/<int:id>```

### Create
**POST** <code>http://localhost:5486/api/users/</code>

    {
        "name": "neo1218"
    }


### Update
**PATCH** ```http://localhost:5486/api/users/<int:id>/``` <br/>
***update a field:***

    { "name": "substack" }

### Delete
***delete a user*** <br/>
**DELETE** ```http://localhost:5486/api/users/<int:id>/``` <br/>

### Pagination
pagination setting at ```apis/configs/usersConfig.py``` <br/>
**GET** ```http://localhost:5486/api/users/?page=2```

### Search
**GET** ```http://localhost:5486/api/users/?<field1>=<value1>&<field2>=<field2>```

<hr>
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

    $ hack migrate

<hr>
## $ Learn More Hacks
Hacks hacking on top of flask and flask plugins

+ [flask website](http://flask.pocoo.org/)
+ [flask plugins](http://flask.pocoo.org/extensions/)

<hr>
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

<hr>
## $ Todo
+ [x] integrated the [pony orm](https://github.com/ponyorm/pony)
+ [ ] build api resources relationship
+ [ ] configurations
    + [ ] restful api config
    + [ ] resource bp config

<hr>
## $ LICENSE
MIT, check LICENSE file for detail
