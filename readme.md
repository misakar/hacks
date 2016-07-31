# ```$_Hacks```

deadly simple restful api framework

## Get Start
### New a project
<code>$ hack new demoAPI</code>

### Generate restful api
(example for user resource) <br/>
<code>$ hack generate api users</code>

## Enjoy Your API:)
(example for user resource) <br/>
### Read
**GET**  <code>http://localhost:5486/api/users/</code>

### Create
**POST** <code>http://localhost:5486/api/users/</code>

    {
        "username": "neo1218",
        "email": "neo1218@yeah.net"
    }


### Update
**PATCH** <code>http://localhost:5486/api/users/?id=1</code> <br/>
***update a field:***

    { "email": "hacks1218@yeah.net" }

***add a field:***

    { "comefrom": "MuxiStudio" }

### Delete
***delete a user*** <br/>
**DELETE** <code>http://localhost:5486/api/users/?id=1</code> <br/>

***delete a field*** <br/>
**DELETE** <code>http://localhost:5486/api/users/?id=1&field=comefrom <br/>

### Pagination
**GET** <code>http://localhost:5486/api/users/?page=1</code>

### Search
**GET** <code>http://localhost:5486/api/users/?<field>=<value></code>

## Notes
Currently, Hacks simply generate a **prototype api**, which means the api **did
not** have **authentication mechanism**, **relationship between each api resource**,
**rate limit**, **http caching** and sadly...can't **invoke your own code**. Obviously,
it ***not ready to go into production***.
<hr/>
But, I will continue to feed more on Hacks, and finally let Hacks become a
**production-oriented**  but **deadly simple** restful api framework.

## Learn More Hacks

## LICENSE
