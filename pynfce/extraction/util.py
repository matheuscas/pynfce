

def find_element(html, xpath, first=True):
    return html.find(xpath, first=first).text
