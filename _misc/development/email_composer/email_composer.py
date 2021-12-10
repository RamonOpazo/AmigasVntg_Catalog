from HTMLTag import HTMLTag
        
class HTML_snippet():
    def __init__(self, tags: dict) -> None:
        self.tree = tags
        
            
        
if __name__ == "__main__":
    
    a = HTMLTag("a", "Amigas Vntg", {"href":"www.amigasvntg.cl", "target":"_blank"})
    p = HTMLTag("p", "Lorem ipsum dolor sit amet...", {"style":"font-weigth:400"})
    b = HTMLTag("b", "Lorem ipsum dolor sit amet...")
    h1 = HTMLTag("h1", "Lorem ipsum dolor sit amet...", {"style":"font-weigth:400"})
    img = HTMLTag("img", None, {"url":"www.github.com/AVC/AVC001/1.png", "alt":"lorem ipsum dolor"})
    
    print(a)
    print(p)
    print(h1)
    print(img)
    
    h1.set_parent(b)
    h1.set_children([img, a])
    a.set_children([p])
    
    print(h1)