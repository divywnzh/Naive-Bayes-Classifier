import bs4

def partA(file_name):
    with open(file_name, "r") as file:
        data = file.read()

    soup = bs4.BeautifulSoup(data, "html.parser")
    title = soup.find("title")
    text = soup.find("text")
    space=" "
    new_data = title.text + space + text.text
    with open(file_name, "w") as file:
        file.write(new_data)
    return new_data

i = 1
while i < 1401:
    file_name = f"CSE508_Winter2023_Dataset/cranfield{str(i).zfill(4)}"
    partA(file_name)
    i += 1