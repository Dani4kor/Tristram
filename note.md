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

/api/v1/image
```json
{
	"schema": {
        "filename": {
            "type": "string",
            "minlength": 1,
            "maxlength": 32,
            "required": true,
            "unique": true,
        },
        "tag": {
            "type": "string",
            "minlength": 1,
            "maxlength": 10,
        },
        "image": {
            "type": "media",
        }
    }
```
