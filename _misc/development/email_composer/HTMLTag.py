from __future__ import annotations
from typing import List

class HTMLTag():
    """Documentation...!"""
    def __init__(self, tag: str, cont: str, attrs: dict = {}) -> None:
        self.is_singleton = tag in ["img", "br", "hr", "input", "link", "meta"]
        self.__parent = None
        self.__children = None
        self.initialize_tag(tag, cont, attrs)
                
    def initialize_tag(self, tag: str, cont: str, attrs: str) -> None:
        # Checking that singleton tags have no content assigned.
        print(cont)
        if self.is_singleton and cont:
            raise Exception(f"Content given to singleton tag: <{tag}>")
        # Initializing 
        else:
            self.tag = tag
            self.cont = cont
            self.attrs = attrs
                
    def compose_attrs(self) -> str:
        return " ".join([f'{i}="{self.attrs[i]}"' for i in self.attrs.keys()])
    
    def compose_tag(self) -> str:
        if self.is_singleton:
            return f'<{self.tag} {self.compose_attrs()}/>'
        else:
            return f'<{self.tag} {self.compose_attrs()}>{self.cont}</{self.tag}>'
        
    def compose_tree(self) -> str:
        tree = f" ╔═{self.__parent.compose_tag()}\n" if self.__parent else ""
        tree += f"{self.compose_tag()}"
        if self.__children:
            for i, child in enumerate(self.__children):
                sym = "╠═" if i+1 < len(self.__children) else "╚═"
                tree += f"\n {sym}{child.compose_tag()}"
        return tree
    
    def get_parent(self):
        return self.__parent
    
    def set_parent(self, parent: HTMLTag) -> None:
        if parent.is_singleton:
            raise Exception("A singleton cannot be a parent")
        if self.__children:
            if not parent in self.__children:
                self.__parent = parent
            else:
                raise Exception("Circular dependency, a parent cannot be any of children")
        else:
            self.__parent = parent
        
    def get_children(self):
        return self.__children
    
    def set_children(self, children: List[HTMLTag]) -> None:
        if self.is_singleton:
            raise Exception("Singletons cannot have children")
        if self.__parent:
            if not self.__parent in children:
                self.__children = children
            else:
                raise Exception("Circular dependency, a parent cannot be any of children")
        else:
            self.__children = children
    
    def __str__(self) -> str:
        return self.compose_tree()