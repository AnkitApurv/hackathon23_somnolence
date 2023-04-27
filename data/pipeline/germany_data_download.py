import pandas as pd

def download() -> None:
    dfs: list[pd.DataFrame] = pd.read_html(io = "https://www.destatis.de/EN/Themes/Labour/Labour-Market/Unemployment/Tables/press-month2.html?view=main[Print]")
    dfs[0].to_excel("../raw/from_competition/germany.xlsx")
    return

if __name__ == '__main__':
    download()
