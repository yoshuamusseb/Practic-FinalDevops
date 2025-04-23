from bs4 import BeautifulSoup

def test_hola_mundo():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    h1 = soup.find("h1")
    p = soup.find("p")
    assert h1 and "Hola Mundo" in h1.text
    assert p and "proyecto final" in p.text
