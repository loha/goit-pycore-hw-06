from uuid import uuid4

class Field:
  def __init__(self) -> None:
    self.field_name= None
    self.value = None

  def get_field_name(self):
    return self.field_name
  
  def get_field_value(self):
    return self.value

  def set_field_name(self, name):
    self.field_name = name
  
  def set_value(self, value):
    self.value = value

class Name(Field):
  def __init__(self, value) -> None:
    super().__init__()
    self.set_field_name("Name")
    self.set_value(value)

class Phone(Field):
  def __init__(self, value) -> None:
    super().__init__()
    self.set_field_name("Phone")
    self.set_value(value)

class Id(Field):
  def __init__(self) -> None:
    super().__init__()
    self.set_field_name("ID")
    self.set_value(str(uuid4()))

class Record:
  def __init__(self) -> None:
    self.fields = []

  def add_field(self, field):
    self.fields.append(field)

  def get_field_by_name(self, field_name):
    for field in self.fields:
      if field.get_field_name() == field_name:
        return field.get_field_value()
    return None

  def __str__(self) -> str:
    res = ""

    for field in self.fields:
      res += f"{field.field_name}: {field.value}. "
    
    return res

class AddressBook:
  def __init__(self) -> None:
    self.records = []

  def add_record(self, *fields):
    record = Record()

    for field in fields:
      record.add_field(field)
    
    self.records.append(record)

    return record
  
  def update_record_by_id(self, id, new_name, new_phone):
    record = self.get_record_by_id(id)

    if record:
      for field in record.fields:
        field_name = field.get_field_name()

        if field_name == "Name":
          field.set_value(new_name)

        if field_name == "Phone":
          field.set_value(new_phone)

      return True
    else:
      return False
  
  def get_record_by_id(self, id):
    for record in self.records:
      for field in record.fields:
        if field.get_field_name() == "ID" and field.get_field_value() == id:
          return record
    return None
  
  def get_record_by_field(self, search_field, search_value, returned_field):
    for record in self.records:
      for field in record.fields:
        if field.get_field_name() == search_field and field.get_field_value() == search_value:
          if returned_field:
            return record.get_field_by_name(returned_field)
          else:
            return record
    
    return None

  
  def get_records(self):
    return list(map(lambda record: str(record).strip(), self.records))