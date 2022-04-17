from common.enums import StrEnum


class ItemStatusEnum(StrEnum):
    
    CREATED = "CREATED"
    REJECTED = "REJECTED"
    APPROVED = "APPROVED"
    SOLD = "SOLD"
    DELETED = "DELETED"
