from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InventoryRecord(_message.Message):
    __slots__ = ["Inventory_ID", "Name", "Description", "Price", "Quantity_in_Stock", "Quantity_in_Reorder", "Discontinued"]
    INVENTORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_IN_STOCK_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_IN_REORDER_FIELD_NUMBER: _ClassVar[int]
    DISCONTINUED_FIELD_NUMBER: _ClassVar[int]
    Inventory_ID: str
    Name: str
    Description: str
    Price: float
    Quantity_in_Stock: int
    Quantity_in_Reorder: int
    Discontinued: bool
    def __init__(self, Inventory_ID: _Optional[str] = ..., Name: _Optional[str] = ..., Description: _Optional[str] = ..., Price: _Optional[float] = ..., Quantity_in_Stock: _Optional[int] = ..., Quantity_in_Reorder: _Optional[int] = ..., Discontinued: bool = ...) -> None: ...

class InventoryRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class InventorySearchRequest(_message.Message):
    __slots__ = ["key_name", "key_value"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value: str
    def __init__(self, key_name: _Optional[str] = ..., key_value: _Optional[str] = ...) -> None: ...

class InventoryRangeRequest(_message.Message):
    __slots__ = ["key_name", "key_value_start", "key_value_end"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_START_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_END_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value_start: str
    key_value_end: str
    def __init__(self, key_name: _Optional[str] = ..., key_value_start: _Optional[str] = ..., key_value_end: _Optional[str] = ...) -> None: ...

class DistributionRequest(_message.Message):
    __slots__ = ["key_name", "percentile"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PERCENTILE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    percentile: float
    def __init__(self, key_name: _Optional[str] = ..., percentile: _Optional[float] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ["key_name", "key_value", "val_name", "val_val_new"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    VAL_NAME_FIELD_NUMBER: _ClassVar[int]
    VAL_VAL_NEW_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value: str
    val_name: str
    val_val_new: str
    def __init__(self, key_name: _Optional[str] = ..., key_value: _Optional[str] = ..., val_name: _Optional[str] = ..., val_val_new: _Optional[str] = ...) -> None: ...

class DistributionResponse(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
