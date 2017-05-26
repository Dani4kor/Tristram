## API schema 

Version = __v1__

Enterpoint = __/api/VERSION__

---

/api/v1/datetime
```json
{
  "mimetype": "application/json",
  "datetime": "datetime"
}

```

---
/api/v1/pic
```json
{
	'schema': {
	        'filename': {
	            'type': 'string',
	            'minlength': 1,
	            'maxlength': 32,
	            'required': True,
	            'unique': True,
	        },
	        'tag': {
	            'type': 'string',
	            'minlength': 1,
	            'maxlength': 10,
	        },
	        'pic': {
	            'type': 'media',
	            'content_type': 'type',
	            'name': 'string',
	            'length': 'int',
	        },
	        'born': {
	            'type': 'datetime',
	        },
	        'active': {
	            'type': 'boolean',
	            'default': True
	        }
	    }
}
```
