# Logging via [betterstack](betterstack.com)

- [betterstack](https://betterstack.com/)
- [documentation](https://betterstack.com/docs/logs/python/#logging-from-python)

## Usage

```python
from apps.services.betterstack_service import betterstack_logger

betterstack_logger.info(
    "User logged in",
    extra={
        "user_id": 123,
        "debug_info": {"function": "get_backend_info", "status": "OK"},
    }
)
```
