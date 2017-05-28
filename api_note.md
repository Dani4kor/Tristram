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
        'image': {
            'type': 'media',
        }
    }
```
