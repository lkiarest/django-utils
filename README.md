# django-utils
Django related utility tools

### encoder
JSON serialization helper, decorate model class: add `to_json` method automatically.

```python
# models.py
from utils.encoder import json_encoder

@json_encoder('id', 'name', 'age')
class User(Model):
  name = Model.CharField(max_length=44)
  age = Model.IntegerField()
  
  
# controller
users = User.objects.all()
return HttpResponse(json.dumps([user.to_json() for user in users])
```
