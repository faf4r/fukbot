from abc import ABC


class BaseAgent(ABC):
    """Agent基类"""

    priority: int = 9999
    name: str = "BaseAgent"
    description: str = ""
    help: str = ""
    usage: str = ""
    alias: list[str] = ["BaseAgent"]

    def __init_subclass__(cls) -> None:
        required_class_vars = ["name", "description", "help", "usage"]
        for var in required_class_vars:
            if var not in cls.__dict__:
                raise NotImplementedError(f"{cls.__name__} must define {var}.")

    def __eq__(self, other: object) -> bool:
        """比较插件是否相同"""
        if not isinstance(other, BaseAgent):
            raise TypeError(f"Cannot compare {type(self)} with {type(other)}")
        return self.name == other.name and self.priority == other.priority

    def __lt__(self, other: object) -> bool:
        """比较插件优先级"""
        if not isinstance(other, BaseAgent):
            raise TypeError(f"Cannot compare {type(self)} with {type(other)}")
        return self.priority < other.priority

    def __gt__(self, other: object) -> bool:
        """比较插件优先级"""
        if not isinstance(other, BaseAgent):
            raise TypeError(f"Cannot compare {type(self)} with {type(other)}")
        return self.priority > other.priority

    def __repr__(self) -> str:
        return f"<plugin name={self.name}, priority={self.priority}>"
