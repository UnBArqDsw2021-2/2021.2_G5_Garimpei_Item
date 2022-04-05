from common.enum import StrEnum


class StatusEnum(StrEnum):
    TYPE_1 = 'type_1'
    TYPE_2 = 'type_2'
    TYPE_3 = 'type_3'

    @classmethod
    def get(cls, value: str) -> str:
        value = value.lower()
        if 'type_1' in value:
            return StatusEnum.TYPE_1
        if 'type_2' in value:
            return StatusEnum.TYPE_2
        if 'type_3' in value:
            return StatusEnum.TYPE_3
        return ''
